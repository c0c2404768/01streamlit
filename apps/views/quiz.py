import streamlit as st

st.markdown("<h2 style='color:#FF6B6B;'>📝 兄さんの新NISA白熱教室</h2>", unsafe_allow_html=True)

tabs = st.tabs(["💡 3分でわかる新NISA", "⚔️ 腕試し！投資クイズ"])

with tabs[0]:
    st.markdown("""
        <div class='study-card'>
            <h3 style='color:#FF6B6B;'>① NISAってなんのためにあるの？</h3>
            <p>普通は投資で儲かると、そのお宝（利益）から<b>約20%の税金</b>が国に引かれちまうんだ。<br>
            でもな、<b>「新NISA」という国公認の魔法の箱</b>の中で株を買えば、儲かったお金が<b>100%キミのもの</b>になるんだぜ！</p>
        </div>
        
        <div class='study-card'>
            <h3 style='color:#FF8E53;'>② どのくらいおトクなの？</h3>
            <p>例えば、投資で頑張って <b>10万円</b> 儲けたとするだろ？<br>
            ・普通の口座：約2万円が引かれて、手元には <b>8万円</b> 😢<br>
            ・新NISA口座：税金ゼロだから、まるまる <b>10万円</b> ゲット！ 😎この差はデカいぜ！</p>
        </div>
        
        <div class='study-card'>
            <h3 style='color:#FFD700; background-color:#333; padding:10px; border-radius:10px;'>🚀 兄さん直伝・始め方3ステップ</h3>
            <p style='color:white; margin-top:10px;'>
            1. ネット証券で口座を開く（スマホで5分だ！）<br>
            2. 「NISA口座も一緒に作る」にチェックを入れる<br>
            3. 月々1,000円からでもいいから、コツコツ積立を始める
            </p>
        </div>
    """, unsafe_allow_html=True)
    
with tabs[1]:
    st.subheader("🔥 兄さんからの挑戦状だ！")
    st.write("学んだ知識を活かして、クイズに答えてみな！")
    
    quiz_choice = st.radio(
        "【問題】新NISAを使って投資をしたとき、最大のメリットは何だ？",
        ["A. 絶対に株価が下がらない（元本保証）", 
         "B. 投資で得た利益に税金がかからず、丸ごと貰える", 
         "C. 銀行の利息が10倍になる"]
    )
    
    if st.button("これで勝負だ！"):
        if "利益に税金がかからず" in quiz_choice:
            st.success("🎉 大・正・解 ！！！ キミは投資の才能があるぜ！")
            st.balloons()
        else:
            st.error("あちゃー！ハズレだぜ！上の「3分でわかる新NISA」タブをもう一回読んで復習だ!")