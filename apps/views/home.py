import streamlit as st


# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#FF6B6B,#FFD93D);
    padding:40px;
    border-radius:25px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}


.hero h1{
    font-size:3rem;
    margin-bottom:10px;
}


.hero p{
    font-size:1.2rem;
}



.page-title{
    font-size:1.2rem;
    font-weight:800;
    margin-bottom:8px;
}



.card{

    background:white;
    padding:25px;
    border-radius:20px;

    border:1px solid #eee;

    box-shadow:
    0 8px 20px rgba(0,0,0,0.08);

    margin-bottom:20px;

    transition:0.3s;

}



.card:hover{

    transform:translateY(-5px);

    box-shadow:
    0 15px 30px rgba(0,0,0,0.15);

}


.description{

    color:#666;
    min-height:50px;

}


</style>

""",unsafe_allow_html=True)



# ==================================================
# ヒーロー
# ==================================================

st.markdown(
"""
<div class="hero">

<h1>📈 株兄さん</h1>

<p>
投資を学び・診断し・未来をシミュレーションする
投資学習アプリ
</p>

</div>

""",
unsafe_allow_html=True
)



# ==================================================
# 説明
# ==================================================

st.subheader("ようこそ")


st.write(
"""
株兄さんでは、投資初心者でも段階的に学習できるよう、

- 投資知識の学習
- 投資タイプ診断
- 資産形成シミュレーション
- 結果管理

の機能を提供します。

左側のナビゲーション、または以下のカードから各機能へ移動できます。
"""
)


st.divider()



# ==================================================
# 機能カード
# ==================================================


st.markdown("## 📌 機能一覧")



# -------- 学習 --------

st.markdown(
"""
<div class="page-title">
📚 学習
</div>

<div class="card">

<div class="description">

投資の基本知識やNISAについて
クイズ形式で学習できます。

</div>

</div>

""",
unsafe_allow_html=True
)


if st.button(
    "学習ページへ移動",
    key="quiz",
    use_container_width=True
):
    st.switch_page("views/quiz.py")




# -------- 診断 --------

st.markdown(
"""
<div class="page-title">
🧠 診断
</div>


<div class="card">

<div class="description">

質問に回答することで、
自分に合った投資タイプを確認できます。

</div>


</div>

""",
unsafe_allow_html=True
)


if st.button(
    "診断ページへ移動",
    key="diagnosis",
    use_container_width=True
):
    st.switch_page("views/diagnosis.py")




# -------- シミュレーション --------

st.markdown(
"""
<div class="page-title">
📊 シミュレーション
</div>


<div class="card">

<div class="description">

投資金額や期間を設定して、
資産形成のイメージを確認できます。

</div>


</div>

""",
unsafe_allow_html=True
)



if st.button(
    "シミュレーションへ移動",
    key="simulation",
    use_container_width=True
):
    st.switch_page("views/simulation.py")




# -------- マイページ --------

st.markdown(
"""
<div class="page-title">
👤 マイページ
</div>


<div class="card">

<div class="description">

診断結果やお気に入り情報を
確認できます。

</div>


</div>

""",
unsafe_allow_html=True
)


if st.button(
    "マイページへ移動",
    key="mypage",
    use_container_width=True
):
    st.switch_page("views/mypage.py")



st.divider()


st.caption(
"株兄さん | Investment Navigator"
)