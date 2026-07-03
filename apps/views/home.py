import streamlit as st

st.markdown("<h1 class='hero-title'>✨ 株兄さん v2.1 ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:#666;'>新NISA対応！キミの未来を華麗に彩る投資診断アプリ</p>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

cols = st.columns(4)
with cols[0]:
    st.markdown("### 💎 銘柄拡充")
    st.write("人気の優待株や巨大企業など、選りすぐりのラインナップだ。")
with cols[1]:
    st.markdown("### 🎨 華やかUI")
    st.write("投資のワクワクを視覚で感じる、リッチな画面体験を届けるぜ。")
with cols[2]:
    st.markdown("### 🚀 未来予測")
    st.write("過去のデータから、キミの資産がどう化けるかをシミュレーション！")
with cols[3]:
    st.markdown("### 📝 クイズ学習")
    st.write("ゲーム感覚で新NISAの基礎を学べるクイズ部屋だぜ!")