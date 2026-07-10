import streamlit as st


# -----------------------------------------------------------------------------
# 1. 共通デザイン（CSS）＆ページ基本設定
# -----------------------------------------------------------------------------
st.set_page_config(page_title="株兄さん v2.1 - 華麗なる投資診断", page_icon="✨", layout="wide")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'M PLUS Rounded 1c', sans-serif;
        background: linear-gradient(135deg, #FFF5F5 0%, #FFF9F0 100%);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #FF6B6B, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. セッション状態の初期化
# -----------------------------------------------------------------------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

# -----------------------------------------------------------------------------
# 3. 共通データ（各ページから st.session_state を経由して参照可能にする）
# -----------------------------------------------------------------------------
if "INVESTMENT_PROFILES" not in st.session_state:
    st.session_state.INVESTMENT_PROFILES = {
        "安心コツコツ型": {
            "description": "世界経済の成長にまるごと投資！大きな失敗を避け、長い時間をかけて財産を築く王道スタイルだぜ。",
            "stocks": [
                {"name": "全世界株式(オルカン)", "ticker": "2559.T", "reason": "1つの銘柄で世界中の会社を応援できる、初心者人気No.1だ！", "stats": [5, 2, 4]},
                {"name": "米国株S&P500", "ticker": "2558.T", "reason": "アップルやグーグルなど、最強の米国企業500社に投資するぜ！", "stats": [4, 4, 3]}
            ]
        },
        "日本インフラ堅実型": {
            "description": "日本の大企業を応援して、配当金（ご褒美）をしっかり受け取るスタイル。安定感が抜群だ！",
            "stocks": [
                {"name": "日本電信電話(NTT)", "ticker": "9432.T", "reason": "通信の巨人。株価が手頃で、配当金も安定している初心者の味方だ。", "stats": [5, 2, 5]},
                {"name": "三菱UFJフィナンシャルG", "ticker": "8306.T", "reason": "日本最大の銀行。金利が上がると利益が出やすい、頼れる兄貴分だ。", "stats": [4, 3, 4]}
            ]
        },
        "ワクワク成長チャレンジ型": {
            "description": "キミの好きなブランドや、未来を創る技術に投資！株価の大幅アップや優待も狙える冒険スタイルだぜ。",
            "stocks": [
                {"name": "オリエンタルランド", "ticker": "4661.T", "reason": "ディズニー運営！圧倒的なブランド力で、応援するだけでワクワクするぜ。", "stats": [3, 4, 2]},
                {"name": "サンリオ", "ticker": "8136.T", "reason": "ハローキティなど世界的人気。新NISAで今、めちゃくちゃ注目されてるぞ！", "stats": [2, 5, 2]},
                {"name": "三菱重工業", "ticker": "7011.T", "reason": "日本の技術力の結晶。防衛や宇宙など、ロマン溢れる巨大企業だぜ！", "stats": [2, 5, 3]}
            ]
        }
    }

# -----------------------------------------------------------------------------
# 4. ページルーティング定義
# -----------------------------------------------------------------------------
home_page = st.Page("views/home.py", title="ホーム", icon="🏠")
diagnosis_page = st.Page("views/diagnosis.py", title="投資診断", icon="🔍")
gakushu_page = st.Page("views/1-gakushu.py", title="学習", icon="📚")
simulation_page = st.Page("views/simulation.py", title="過去シミュレーション", icon="📊")
quiz_page = st.Page("views/quiz.py", title="NISA学習・クイズ", icon="📝")
mypage_page = st.Page("views/mypage.py", title="マイページ", icon="📂")

# ナビゲーションの実行
pg = st.navigation({
    "🤵 株兄さん メニュー": [home_page, diagnosis_page, gakushu_page, simulation_page, quiz_page, mypage_page]
})
pg.run()