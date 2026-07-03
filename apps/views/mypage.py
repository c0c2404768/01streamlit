import streamlit as st

st.markdown("<h2 style='color:#FF6B6B;'>📂 キミのコレクション</h2>", unsafe_allow_html=True)

if not st.session_state.favorites:
    st.info("まだお気に入りがないぜ！診断でお宝銘柄を見つけてこいよな！")
else:
    st.write("現在のお気に入りリスト：")
    for f in st.session_state.favorites:
        st.markdown(f"- <span class='stock-badge'>{f}</span>", unsafe_allow_html=True)
    
    if st.button("リストをクリアする"):
        st.session_state.favorites = []
        st.rerun()