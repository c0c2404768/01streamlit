import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf


st.markdown("<h2 style='color:#FF6B6B;'>📊 過去5年の指数積立シミュレーション</h2>", unsafe_allow_html=True)
st.caption("指定した株価指数に毎月同じ金額を積み立てた場合の、過去5年間の推移を確認できます。")

st.markdown(
    """
    <style>
    .sim-card {
        background: #ffffff;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
        margin-bottom: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


INDEX_OPTIONS = {
    "日経平均株価": "^N225",
    "全世界株式(オールカントリー)": "2559.T",
    "S&P500": "^GSPC",
    "NASDAQ100": "^NDX",
}


def build_history_projection(history: pd.DataFrame, monthly_yen: int) -> pd.DataFrame:
    records = []
    accumulated_units = 0.0
    total_invested = 0.0
    data = history.copy().dropna(subset=["Close"])

    for date, row in data.iterrows():
        price = float(row["Close"])
        if price <= 0:
            continue

        accumulated_units += monthly_yen / price
        total_invested += monthly_yen
        balance = accumulated_units * price

        records.append(
            {
                "date": date,
                "close": price,
                "invested": total_invested,
                "balance": balance,
                "gain": balance - total_invested,
                "units": accumulated_units,
            }
        )

    return pd.DataFrame(records)


col1, col2 = st.columns([1.1, 0.9])

with col1:
    selected_index_name = st.selectbox("シミュレーションする株価指数", list(INDEX_OPTIONS.keys()))
    monthly_man = st.slider("毎月の積立額（万円）", min_value=1.0, max_value=10.0, value=3.0, step=0.5)
    years = 5



monthly_yen = int(monthly_man * 10000)
selected_ticker = INDEX_OPTIONS[selected_index_name]

try:
    with st.spinner("過去データを取得中..."):
        history = yf.Ticker(selected_ticker).history(period="5y", interval="1mo")
    if not history.empty:
        # 先にCloseが欠損（NaN）している行を綺麗に削除する
        history = history.dropna(subset=["Close"])
        
        if len(history) > 1:
            # 1. 最後の行の日付が「今月（実行月）」の場合は、データが未確定なので無条件で削除する
            current_month = pd.Timestamp.now().strftime("%Y-%m")
            if history.index[-1].strftime("%Y-%m") == current_month:
                history = history.iloc[:-1]
            
            # 2. 念のため、それでも最後の行が前月比で30%以上急落している場合は異常値として削除する
            if len(history) > 1 and history["Close"].iloc[-1] < (history["Close"].iloc[-2] * 0.7):
                history = history.iloc[:-1]

    projection = build_history_projection(history, monthly_yen)

    if projection.empty:
        st.warning("試算できるデータがありません。別の指数を選んでね。")
        st.stop()

    final_balance = float(projection["balance"].iloc[-1])
    total_invested = float(projection["invested"].iloc[-1])
    gain = final_balance - total_invested
    gain_rate = (gain / total_invested * 100) if total_invested else 0.0
    tax_saved = gain * 0.20315
    annualized_return = (
        (final_balance / total_invested) ** (1 / years) - 1
        if total_invested > 0 and final_balance > 0
        else 0.0
    ) * 100

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=projection["date"],
            y=projection["balance"] / 10000,
            fill="tozeroy",
            line=dict(color="#FF6B6B", width=3),
            name="資産評価額",
            hovertemplate="<b>%{x|%Y年%m月}</b><br>資産: ¥%{y:.2f}万円<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=projection["date"],
            y=projection["invested"] / 10000,
            line=dict(color="#64748b", width=2, dash="dash"),
            name="これまでの投資額",
            hovertemplate="<b>%{x|%Y年%m月}</b><br>投資額: ¥%{y:.2f}万円<extra></extra>",
        )
    )

    fig.update_layout(
        title=f"📊 {selected_index_name} を毎月{monthly_man:.1f}万円積み立てた場合の過去5年シミュレーション",
        xaxis_title="時期",
        yaxis_title="金額（万円）",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        height=450,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:
        st.metric("最終評価額", f"{final_balance / 10000:,.1f} 万円", delta=f"+{gain / 10000:,.1f} 万円")

    with metric_col2:
        st.metric("積立元本", f"{total_invested / 10000:,.1f} 万円")

    with metric_col3:
        st.metric("5年間の増加率", f"{gain_rate:.1f}%")


    with st.expander("📚 積立のポイント"):
        st.write(
            f"""
            - 毎月同じ額を入れると、価格が高いときは少なく、安いときは多く買いやすい。
            - これがドルコスト平均法で、長期積立との相性がいい。
            - NISAは運用益が非課税なので、複利の伸びをそのまま活かしやすい。
            - この試算は {selected_index_name} の過去5年データに基づく単純モデルです。
            """
        )

except Exception:
    st.error("データの取得に失敗したぜ…時間を置いて試してくれ！")


