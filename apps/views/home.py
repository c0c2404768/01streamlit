# import streamlit as st

# st.markdown("<h1 class='hero-title'>✨ 株兄さん v2.1 ✨</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; font-size:1.2rem; color:#666;'>新NISA対応！キミの未来を華麗に彩る投資診断アプリ</p>", unsafe_allow_html=True)

# st.image("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

# cols = st.columns(4)
# with cols[0]:
#     st.markdown("### 💎 銘柄拡充")
#     st.write("人気の優待株や巨大企業など、選りすぐりのラインナップだ。")
# with cols[1]:
#     st.markdown("### 🎨 華やかUI")
#     st.write("投資のワクワクを視覚で感じる、リッチな画面体験を届けるぜ。")
# with cols[2]:
#     st.markdown("### 🚀 未来予測")
#     st.write("過去のデータから、キミの資産がどう化けるかをシミュレーション！")
# with cols[3]:
#     st.markdown("### 📝 クイズ学習")
#     st.write("ゲーム感覚で新NISAの基礎を学べるクイズ部屋だぜ!")

#     #----------------------
import streamlit as st
import requests

# ----------------------------------------
# ページ設定
# ----------------------------------------
st.set_page_config(
    page_title="Investment Navigator",
    page_icon="📈",
    layout="wide"
)

# ----------------------------------------
# ネットワーク接続確認
# ----------------------------------------
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.RequestException:
        return False

if not check_internet():
    st.error("⚠ インターネットに接続できません。")
    st.warning("ネットワーク接続を確認してから再度お試しください。")
    st.stop()

# ----------------------------------------
# タイトル
# ----------------------------------------
st.title("📈 Investment Navigator")
st.caption("投資を学び、診断し、資産形成をサポートするアプリ")

st.divider()

st.markdown("""
### ようこそ！

このアプリでは、

- 📚 投資について学ぶ
- 🧠 あなたに合った投資タイプを診断する
- 👤 自分の情報や診断結果を管理する
- 📈 将来の資産をシミュレーションする

といった機能を利用できます。

※ 現在開発中のため、一部機能は未完成です。
""")

st.divider()

st.subheader("メニュー")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("## 📚 学習")
        st.write("投資の基礎知識を学びます。")
        st.info("🚧 開発中")
        if st.button("学習ページへ", use_container_width=True):
            st.switch_page("pages/1_学習.py")

with col2:
    with st.container(border=True):
        st.markdown("## 🧠 診断")
        st.write("質問に答えて投資タイプを診断します。")
        st.info("🚧 開発中")
        if st.button("診断ページへ", use_container_width=True):
            st.switch_page("pages/2_診断.py")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("## 👤 マイページ")
        st.write("診断結果や登録情報を確認できます。")
        st.info("🚧 開発中")
        if st.button("マイページへ", use_container_width=True):
            st.switch_page("pages/3_マイページ.py")

with col4:
    with st.container(border=True):
        st.markdown("## 📈 シミュレーション")
        st.write("資産運用の将来予測を行います。")
        st.info("🚧 開発中")
        if st.button("シミュレーションへ", use_container_width=True):
            st.switch_page("pages/4_シミュレーション.py")

st.divider()
st.caption("Version 0.1.0（開発中）")