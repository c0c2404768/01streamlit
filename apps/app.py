import streamlit as st

# ==========================================================
# ページ設定
# ==========================================================
st.set_page_config(
    page_title="株兄さん",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# 共通CSS
# ==========================================================
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #fafafa;
}

.sidebar-title{
    font-size:1.5rem;
    font-weight:800;
    text-align:center;
    margin-bottom:0.2rem;
}

.sidebar-subtitle{
    text-align:center;
    color:#666;
    font-size:0.9rem;
    margin-bottom:1rem;
}

.footer{
    text-align:center;
    color:gray;
    font-size:0.8rem;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# セッション状態
# ==========================================================
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

# ==========================================================
# 共通データ
# ==========================================================
if "INVESTMENT_PROFILES" not in st.session_state:

    st.session_state.INVESTMENT_PROFILES = {

        "安心コツコツ型": {

            "description":
            "世界経済の成長にまるごと投資！大きな失敗を避け、長い時間をかけて財産を築く王道スタイルだぜ。",

            "stocks":[

                {
                    "name":"全世界株式(オルカン)",
                    "ticker":"2559.T",
                    "reason":"1つの銘柄で世界中の会社を応援できる、初心者人気No.1だ！",
                    "stats":[5,2,4]
                },

                {
                    "name":"米国株S&P500",
                    "ticker":"2558.T",
                    "reason":"アップルやグーグルなど、最強の米国企業500社に投資するぜ！",
                    "stats":[4,4,3]
                }

            ]

        },

        "日本インフラ堅実型":{

            "description":
            "日本の大企業を応援して、配当金をしっかり受け取るスタイル。",

            "stocks":[

                {
                    "name":"日本電信電話(NTT)",
                    "ticker":"9432.T",
                    "reason":"安定した通信企業。",
                    "stats":[5,2,5]
                },

                {
                    "name":"三菱UFJフィナンシャルG",
                    "ticker":"8306.T",
                    "reason":"日本最大級の銀行。",
                    "stats":[4,3,4]
                }

            ]

        },

        "ワクワク成長チャレンジ型":{

            "description":
            "成長企業へ積極的に投資するタイプ。",

            "stocks":[

                {
                    "name":"オリエンタルランド",
                    "ticker":"4661.T",
                    "reason":"テーマパーク運営企業。",
                    "stats":[3,4,2]
                },

                {
                    "name":"サンリオ",
                    "ticker":"8136.T",
                    "reason":"世界的人気キャラクター企業。",
                    "stats":[2,5,2]
                },

                {
                    "name":"三菱重工業",
                    "ticker":"7011.T",
                    "reason":"日本を代表する重工メーカー。",
                    "stats":[2,5,3]
                }

            ]

        }

    }

# ==========================================================
# ページ定義
# ==========================================================
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

# ==========================================================
# サイドバー
# ==========================================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📈 株兄さん</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Investment Navigator</div>',
        unsafe_allow_html=True
    )

    st.caption("投資を学び、診断し、将来をシミュレーションできるアプリ")

    st.divider()

# ==========================================================
# ナビゲーション
# ==========================================================
pg = st.navigation([
    home_page,
    quiz_page,
    diagnosis_page,
    simulation_page,
    mypage_page
])

pg.run()

# ==========================================================
# フッター
# ==========================================================
st.markdown(
    '<div class="footer">Version 1.0.0</div>',
    unsafe_allow_html=True
)