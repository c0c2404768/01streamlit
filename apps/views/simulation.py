import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.markdown("<h2 style='color:#FF6B6B;'>📊 過去シミュレーター</h2>", unsafe_allow_html=True)

all_stocks = []
for p in st.session_state.INVESTMENT_PROFILES.values():
    all_stocks.extend(p["stocks"])

target_stock = st.selectbox("シミュレーションする銘柄を選んでね", [s["name"] for s in all_stocks])
selected_stock = next(s for s in all_stocks if s["name"] == target_stock)

monthly_amount = st.slider("毎月の投資額（万円）", 1, 10, 10, 1)
annual_amount = monthly_amount * 12

try:
    with st.spinner('データを取得中...'):
        data = yf.Ticker(selected_stock["ticker"]).history(period="5y", interval="1mo")
        if not data.empty:
            accumulated_shares = 0
            total_invested = 0
            
            # 積立投資の計算
            data_copy = data.copy()
            data_copy['AccumulatedValue'] = 0.0
            data_copy['TotalInvested'] = 0.0
            
            for idx, (date, row) in enumerate(data_copy.iterrows()):
                price = row['Close']
                accumulated_shares += monthly_amount / price
                total_invested += monthly_amount
                data_copy.loc[date, 'AccumulatedValue'] = accumulated_shares * price
                data_copy.loc[date, 'TotalInvested'] = total_invested
            
            # グラフ描画
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=data_copy.index,
                y=data_copy['AccumulatedValue'],
                fill='tozeroy',
                line=dict(color='#FF6B6B', width=3),
                name='資産価値',
                hovertemplate='<b>%{x|%Y年%m月}</b><br>資産: ¥%{y:.1f}万<extra></extra>'
            ))
            fig.add_trace(go.Scatter(
                x=data_copy.index,
                y=data_copy['TotalInvested'],
                fill=None,
                line=dict(color='gray', width=2, dash='dash'),
                name='投資額累計',
                hovertemplate='<b>%{x|%Y年%m月}</b><br>投資額: ¥%{y:.1f}万<extra></extra>'
            ))
            
            fig.update_layout(
                title=f"📊 {target_stock} の積立投資シミュレーション（過去5年）",
                xaxis_title="時期",
                yaxis_title="金額（万円）",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                hovermode='x unified',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # 結果表示
            final_value = data_copy['AccumulatedValue'].iloc[-1]
            total_invested_final = data_copy['TotalInvested'].iloc[-1]
            profit = final_value - total_invested_final
            profit_rate = (profit / total_invested_final) * 100 if total_invested_final > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "5年後の資産価値",
                    f"{final_value:.1f} 万円",
                    delta=f"{profit:.1f} 万円",
                    delta_color="normal" if profit >= 0 else "inverse"
                )
            
            with col2:
                st.metric(
                    "投資総額",
                    f"{total_invested_final:.0f} 万円",
                    delta=None
                )
            
            with col3:
                st.metric(
                    "運用益率",
                    f"{profit_rate:.1f}%",
                    delta=None
                )
            
            # 補足情報
            st.markdown("---")
            with st.expander("📚 積立投資のメリット"):
                st.write(f"""
                ✅ **投資方法**: 毎月{monthly_amount}万円を積立投資
                
                📈 **結果**:
                - 投資総額: {total_invested_final:.0f}万円
                - 資産価値: {final_value:.1f}万円
                - 運用益: {profit:.1f}万円 ({profit_rate:.1f}%)
                
                 **積立投資のコツ**:
                - 毎月同じ額を投資するので、価格が安い時は多く、高い時は少なく買える
                - これを「ドルコスト平均法」と言って、初心者向けの最強戦法だ
                - 相場の上下に一喜一憂せず、淡々と続けることが成功の秘訣
                - 複利効果で雪だるま式に資産が増える
                """)
except Exception:
    st.error("データの取得に失敗したぜ…時間を置いて試してくれ！")