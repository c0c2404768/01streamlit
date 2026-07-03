import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.parse

# タイトル
st.markdown("<h2 style='color:#FF6B6B;'>📂 キミの専用マイページ</h2>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. タイプ診断結果の共有
# -----------------------------------------------------------------------------
st.markdown("### 🏆 診断結果の記録")
if "user_type" in st.session_state:
    user_type = st.session_state.user_type
    profile = st.session_state.INVESTMENT_PROFILES[user_type]
    
    st.markdown(f"""
        <div class='result-card'>
            <h4 style='color:#FF6B6B;'>現在の診断タイプ：{user_type}</h4>
            <p>{profile['description']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # SNS共有ボタンの作成
    share_text = f"株兄さんで診断した結果、私は「{user_type}」だったぜ！✨ #株兄さん #新NISA"
    share_url = "https://your-app-url.streamlit.app/" # 本番URLが決まったら書き換えてください
    
    col_sns1, col_sns2 = st.columns(2)
    with col_sns1:
        x_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(share_text)}&url={share_url}"
        st.link_button("𝕏 (Twitter)で結果を自慢する", x_url, use_container_width=True)
    with col_sns2:
        line_url = f"https://social-plugins.line.me/lineit/share?url={urllib.parse.quote(share_url)}&text={urllib.parse.quote(share_text)}"
        st.link_button("LINEで仲間に送る", line_url, use_container_width=True)
else:
    st.info("まだ診断を受けていないようだな!「投資診断」ページへGOだぜ!🚀")

# -----------------------------------------------------------------------------
# 2. お気に入りの管理（個別削除機能付き）
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### ⭐ お気に入り銘柄リスト")

if not st.session_state.favorites:
    st.write("まだお気に入りが登録されていないぞ。")
else:
    # 削除ボタンとリストを並べる
    for fav in st.session_state.favorites:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"<span class='stock-badge' style='display:inline-block; margin-bottom:10px;'>{fav}</span>", unsafe_allow_html=True)
        with col2:
            if st.button("削除", key=f"del_{fav}"):
                st.session_state.favorites.remove(fav)
                st.rerun()

# -----------------------------------------------------------------------------
# 3. 気になる銘柄を比較・確認
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 銘柄比較チャート")

if len(st.session_state.favorites) < 2:
    st.warning("比較するには2つ以上の銘柄をお気に入りに追加してくれ！")
else:
    selected_favs = st.multiselect("比較したい銘柄を選んでね", st.session_state.favorites, default=st.session_state.favorites[:2])
    
    if selected_favs:
        # データの準備
        compare_data = []
        # 全銘柄リストから選択された銘柄のステータスを抽出
        all_stocks_data = []
        for p in st.session_state.INVESTMENT_PROFILES.values():
            all_stocks_data.extend(p["stocks"])
            
        for name in selected_favs:
            stock_info = next((s for s in all_stocks_data if s["name"] == name), None)
            if stock_info:
                compare_data.append({
                    "名前": name,
                    "安全": stock_info["stats"][0],
                    "成長": stock_info["stats"][1],
                    "お得": stock_info["stats"][2]
                })
        
        df_compare = pd.DataFrame(compare_data)
        
        # Plotlyでレーダーチャート、または棒グラフで比較
        fig = go.Figure()
        metrics = ["安全", "成長", "お得"]
        
        for name in selected_favs:
            row = df_compare[df_compare["名前"] == name].iloc[0]
            fig.add_trace(go.Bar(
                name=name,
                x=metrics,
                y=[row["安全"], row["成長"], row["お得"]]
            ))
            
        fig.update_layout(
            barmode='group',
            title="銘柄別ステータス比較",
            xaxis_title="評価項目",
            yaxis_title="レベル (1-5)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)