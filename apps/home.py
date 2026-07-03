import streamlit as st

st.set_page_config(
    page_title="株兄さん",
    page_icon="📈",
    layout="wide"
)

# タイトル
st.title("📈 株兄さん")
st.caption("投資を学び、診断し、資産形成をサポートするアプリ")

st.divider()

st.markdown("""
## ようこそ！

株兄さんでは、

- 📚 投資の基礎を学ぶ
- 🧠 あなたに合った投資タイプを診断
- 👤 診断結果や情報を管理
- 📈 将来の資産をシミュレーション

することができます。

ぜひ興味のある機能からご利用ください。
""")

st.divider()

st.subheader("メニュー")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):

        st.markdown("## 📚 学習")

        st.write("投資初心者向けに基礎知識を分かりやすく学べます。")

        if st.button("学習する", use_container_width=True):
            st.switch_page("pages/quiz.py")

with col2:
    with st.container(border=True):

        st.markdown("## 🧠 診断")

        st.write("質問に答えてあなたの投資タイプを診断します。")

        if st.button("診断する", use_container_width=True):
            st.switch_page("pages/diagnosis.py")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):

        st.markdown("## 👤 マイページ")

        st.write("診断結果や登録情報を確認できます。")

        if st.button("確認する", use_container_width=True):
            st.switch_page("pages/mypage.py")

with col4:
    with st.container(border=True):

        st.markdown("## 📈 シミュレーション")

        st.write("資産運用を行った場合の将来予測を確認できます。")

        if st.button("開始する", use_container_width=True):
            st.switch_page("pages/simulation.py")

st.divider()

st.caption("Version 1.0.0")

# 