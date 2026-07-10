import streamlit as st


# ==================================================
# ページ設定
# ==================================================

st.set_page_config(
    page_title="株兄さん",
    page_icon="📈",
    layout="wide"
)



# ==================================================
# 共通CSS
# ==================================================

st.markdown("""

<style>


html, body, [data-testid="stAppViewContainer"]{

    font-family:
    "M PLUS Rounded 1c",
    sans-serif;

}


/* サイドバー */

section[data-testid="stSidebar"]{

    background:#fafafa;

}


.sidebar-title{

    font-size:1.5rem;
    font-weight:900;
    text-align:center;

}


.sidebar-subtitle{

    text-align:center;
    color:#777;
    font-size:0.9rem;

}



/* ボタン */

.stButton button{

    border-radius:18px;

    background:
    linear-gradient(
        45deg,
        #FF6B6B,
        #FF8E53
    );

    color:white;

    border:none;

    font-weight:700;

}


.stButton button:hover{

    transform:
    translateY(-3px);

}



/* フッター */

.footer{

    text-align:center;

    color:#888;

    font-size:0.8rem;

}


</style>


""",
unsafe_allow_html=True
)



# ==================================================
# session_state
# ==================================================

if "favorites" not in st.session_state:

    st.session_state.favorites=[]



if "quiz_answered" not in st.session_state:

    st.session_state.quiz_answered=False




# ==================================================
# 共通データ
# ==================================================

if "INVESTMENT_PROFILES" not in st.session_state:


    st.session_state.INVESTMENT_PROFILES={


        "安心コツコツ型":{

            "description":
            "世界経済へ分散投資する安定型",

            "stocks":[

                {
                    "name":"全世界株式(オルカン)",
                    "ticker":"2559.T",
                    "reason":
                    "世界中へ分散投資できる商品",
                    "stats":[5,2,4]
                }

            ]

        },


        "日本インフラ堅実型":{

            "description":
            "安定企業を中心に投資するタイプ",

            "stocks":[

                {
                    "name":"日本電信電話(NTT)",
                    "ticker":"9432.T",
                    "reason":
                    "通信インフラ企業",
                    "stats":[5,2,5]
                }

            ]

        },


        "ワクワク成長チャレンジ型":{

            "description":
            "成長企業へ投資するタイプ",

            "stocks":[

                {
                    "name":"オリエンタルランド",
                    "ticker":"4661.T",
                    "reason":
                    "ブランド力を持つ企業",
                    "stats":[3,4,2]
                }

            ]

        }

    }



# ==================================================
# ページ定義
# ==================================================

home_page = st.Page(
    "views/home.py",
    title="ホーム",
    icon="🏠"
)


quiz_page = st.Page(
    "views/quiz.py",
    title="学習",
    icon="📚"
)


diagnosis_page = st.Page(
    "views/diagnosis.py",
    title="診断",
    icon="🧠"
)


simulation_page = st.Page(
    "views/simulation.py",
    title="シミュレーション",
    icon="📊"
)


mypage_page = st.Page(
    "views/mypage.py",
    title="マイページ",
    icon="👤"
)



# ==================================================
# サイドバー
# ==================================================

with st.sidebar:


    st.markdown(
        """
        <div class="sidebar-title">
        📈 株兄さん
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="sidebar-subtitle">
        Investment Navigator
        </div>
        """,
        unsafe_allow_html=True
    )


    st.caption(
        "投資を学び、診断し、未来を考えるアプリ"
    )


    st.divider()



# ==================================================
# Navigation
# ==================================================

pg = st.navigation(

    [

        home_page,
        quiz_page,
        diagnosis_page,
        simulation_page,
        mypage_page

    ]

)



# ==================================================
# 実行
# ==================================================

pg.run()



# ==================================================
# Footer
# ==================================================

st.markdown(

"""
<div class="footer">

© 2026 株兄さん | Investment Navigator

</div>

""",

unsafe_allow_html=True

)



