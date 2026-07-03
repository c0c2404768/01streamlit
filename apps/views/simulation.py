import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.markdown("<h2 style='color:#FF6B6B;'>📊 過去シミュレーター</h2>", unsafe_allow_html=True)

all_stocks = []
for p in st.session_state.INVESTMENT_PROFILES.values():
    all_stocks.extend(p["stocks"])

target_stock = st.selectbox("シミュレーションする銘柄を選んでね", [s["name"] for s in all_stocks])
selected_stock = next(s for s in all_stocks if s["name"] == target_stock)

amount = st.slider("投資金額 (万円)", 10, 300, 100, 10)

try:
    with st.spinner('データを取得中...'):
        data = yf.Ticker(selected_stock["ticker"]).history(period="5y", interval="1mo")
        if not data.empty:
            start_p = data['Close'].iloc[0]
            data['Value'] = (data['Close'] / start_p) * amount
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['Value'], fill='tozeroy', line=dict(color='#FF6B6B')))
            fig.update_layout(title=f"{target_stock} の資産推移", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            
            final = data['Value'].iloc[-1]
            st.metric("5年後の資産価値", f"{final:.1f} 万円", f"{(final-amount):.1f} 万円")
except Exception:
    st.error("データの取得に失敗したぜ…時間を置いて試してくれ！")