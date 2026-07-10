import streamlit as st

# ==============================
# CSS
# ==============================
st.markdown("""
<style>

.title{
    font-size:3rem;
    font-weight:800;
    text-align:center;
    margin-bottom:0.2rem;
}

.subtitle{
    text-align:center;
    color:#666;
    font-size:1.1rem;
    margin-bottom:2rem;
}

.footer{
    text-align:center;
    color:gray;
    font-size:0.9rem;
}

div[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:18px;
    padding:10px;
    box-shadow:0 6px 20px rgba(0,0,0,.08);
    background:white;
    border:1px solid #ececec;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# タイトル
# ==============================
st.markdown(
    '<div class="title">📈 株兄さん</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">投資を学び・理解し・判断するための総合学習アプリ</div>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("📌 機能一覧")

# ==============================
# 1行目
# ==============================
col1, col2 = st.columns(2, gap="large")

with col1:

    with st.container(border=True):

        st.subheader("📚 学習")

        st.write(
            "投資の基礎知識から応用まで体系的に学習できます。"
        )

        st.page_link(
            "views/quiz.py",
            label="学習を始める",
            icon="📚"
        )

with col2:

    with st.container(border=True):

        st.subheader("🧠 診断")

        st.write(
            "質問に回答し、自分に合った投資タイプを診断できます。"
        )

        st.page_link(
            "views/diagnosis.py",
            label="診断を始める",
            icon="🧠"
        )

# ==============================
# 2行目
# ==============================
col3, col4 = st.columns(2, gap="large")

with col3:

    with st.container(border=True):

        st.subheader("👤 マイページ")

        st.write(
            "学習履歴や診断結果などを確認できます。"
        )

        st.page_link(
            "views/mypage.py",
            label="マイページへ",
            icon="👤"
        )

with col4:

    with st.container(border=True):

        st.subheader("📊 シミュレーション")

        st.write(
            "資産運用をシミュレーションし、将来の資産形成を確認できます。"
        )

        st.page_link(
            "views/simulation.py",
            label="シミュレーションへ",
            icon="📊"
        )

st.divider()

st.subheader("📖 このアプリについて")

st.write("""
**株兄さん**は、投資をこれから始める方や投資について学びたい方を対象とした学習アプリです。

ホーム画面から各機能へアクセスし、投資の基礎知識の学習、投資タイプ診断、資産運用シミュレーションなどを利用できます。
""")

st.divider()

st.markdown(
    '<div class="footer">© 2026 株兄さん</div>',
    unsafe_allow_html=True
)