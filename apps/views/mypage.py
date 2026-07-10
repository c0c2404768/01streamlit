import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.parse
from datetime import datetime

st.markdown("<h2 style='color:#FF6B6B;'>📂 キミの専用マイページ</h2>", unsafe_allow_html=True)

if "memos" not in st.session_state:
    st.session_state.memos = []

# -----------------------------------------------------------------------------
# 1. 🏆 診断結果の記録と共有
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
    
    share_text = f"株兄さんで診断した結果、私は「{user_type}」だったぜ！✨ #株兄さん #新NISA"
    share_url = "https://your-app-url.streamlit.app/"
    
    col_sns1, col_sns2 = st.columns(2)
    with col_sns1:
        x_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(share_text)}&url={share_url}"
        st.link_button("𝕏 (Twitter)で結果を自慢する", x_url, use_container_width=True)
    with col_sns2:
        line_url = f"https://social-plugins.line.me/lineit/share?url={urllib.parse.quote(share_url)}&text={urllib.parse.quote(share_text)}"
        st.link_button("LINEで仲間に送る", line_url, use_container_width=True)
else:
    st.info("まだ診断を受けていないようだな！「投資診断」ページへGOだぜ！🚀")


# -----------------------------------------------------------------------------
# 2. ⭐ 他のページから追加されたお気に入りの表示と管理
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### ⭐ お気に入り銘柄リスト")

# もし他ページでエラーが起きてもマイページが壊れないように安全装置を配置
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if not st.session_state.favorites:
    st.info("まだお気に入りがないぜ！診断やお宝銘柄を見つけてこいよな！")
else:
    st.write("現在のお気に入りリスト（個別削除もできるぜ）：")
    
    # リスト表示と個別削除
    for fav in st.session_state.favorites:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- <span class='stock-badge'>{fav}</span>", unsafe_allow_html=True)
        with col2:
            # 個別削除ボタン（キーが重複しないように銘柄名を仕込む）
            if st.button("削除", key=f"delete_{fav}"):
                st.session_state.favorites.remove(fav)
                st.rerun()


# -----------------------------------------------------------------------------
# 3. 📊 気なる銘柄を比較・確認
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 銘柄比較チャート")

if len(st.session_state.favorites) < 2:
    st.warning("比較するには、他のページで2つ以上の銘柄をお気に入りに追加してくれ！")
else:
    selected_favs = st.multiselect("比較したい銘柄を選んでね", st.session_state.favorites, default=st.session_state.favorites[:2])
    
    if selected_favs:
        compare_data = []
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
            xaxis_title="評価項目",
            yaxis_title="レベル (1-5)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)


# -----------------------------------------------------------------------------
# 4. 📝 メモ機能
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📝 メモ")
st.caption("気づきや次に買いたい銘柄を、ここにそのまま残せるぜ。")

with st.form("memo_form", clear_on_submit=True):
    memo_title = st.text_input("メモのタイトル", placeholder="例: 今週の気づき")
    memo_body = st.text_area("メモの内容", placeholder="例: 配当利回りを先に確認する")
    submitted = st.form_submit_button("メモを保存")

    if submitted:
        if memo_title.strip() or memo_body.strip():
            st.session_state.memos.insert(
                0,
                {
                    "title": memo_title.strip() or "タイトルなし",
                    "body": memo_body.strip(),
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
            )
            st.toast("メモを保存したぜ！")
            st.rerun()
        else:
            st.warning("タイトルか内容のどちらかは入れてくれ！")

if not st.session_state.memos:
    st.info("まだメモはないぜ。診断の気づきや気になる銘柄を書いてみよう。")
else:
    for index, memo in enumerate(st.session_state.memos):
        with st.container(border=True):
            col_left, col_right = st.columns([4, 1])
            with col_left:
                st.markdown(f"**{memo['title']}**")
                if memo["body"]:
                    st.write(memo["body"])
                st.caption(memo["created_at"])
            with col_right:
                if st.button("削除", key=f"delete_memo_{index}"):
                    st.session_state.memos.pop(index)
                    st.rerun()