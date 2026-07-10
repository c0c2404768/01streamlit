import streamlit as st


 #-----------------------------------------------------------------------------
 #1. 共通デザイン（CSS）＆ページ基本設定
 #-----------------------------------------------------------------------------
st.set_page_config(page_title="株兄さん v2.1 - 華麗なる投資診断", page_icon="✨", layout="wide")

 st.markdown("""
     <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@400;700&display=swap" rel="stylesheet">
     <style>
     html, body, [data-testid="stAppViewContainer"] {
         font-family: 'M PLUS Rounded 1c', sans-serif;
         background: linear-gradient(135deg, FFF5F5 0%, FFF9F0 100%);
     }
    
     .hero-title {
         font-size: 3.5rem;
         font-weight: 700;
         background: linear-gradient(45deg, FF6B6B, FFD700);
         -webkit-background-clip: text;
         -webkit-text-fill-color: transparent;
         text-align: center;
         margin-bottom: 0px;
     }
    
     .stButton>button {
         border-radius: 20px;
         background: linear-gradient(45deg, FF6B6B, FF8E53);
         color: white;
         border: none;
         padding: 10px 30px;
         font-weight: 700;
         box-shadow: 0 10px 20px rgba(255, 107, 107, 0.2);
         transition: all 0.3s;
     }
     .stButton>button:hover {
         transform: translateY(-3px);
         box-shadow: 0 15px 30px rgba(255, 107, 107, 0.4);
     }
    
     .result-card {
         background: white;
         padding: 30px;
         border-radius: 30px;
         border-left: 15px solid FFD700;
         box-shadow: 0 20px 40px rgba(0,0,0,0.05);
         margin-top: 20px;
     }

     .study-card {
         background: FFFFFF;
         padding: 25px;
         border-radius: 20px;
         border-top: 8px solid FF6B6B;
         box-shadow: 0 10px 25px rgba(0,0,0,0.03);
         margin-bottom: 20px;
     }
    
     .stock-badge {
         background: f0f2f6;
         padding: 5px 15px;
         border-radius: 10px;
         font-weight: 700;
         color: FF6B6B;
     }
     </style>
 """, unsafe_allow_html=True)

  
  # -----------------------------------------------------------------------------
  #2. セッション状態の初期化
  #-----------------------------------------------------------------------------
 if "favorites" not in st.session_state:
     st.session_state.favorites = []
 if "quiz_answered" not in st.session_state:
     st.session_state.quiz_answered = False

  #-----------------------------------------------------------------------------
  #3. 共通データ（各ページから st.session_state を経由して参照可能にする）
  #-----------------------------------------------------------------------------
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

  #-----------------------------------------------------------------------------
  #4. ページルーティング定義
  #-----------------------------------------------------------------------------
 home_page = st.Page("views/home.py", title="ホーム", icon="🏠")
 diagnosis_page = st.Page("views/diagnosis.py", title="投資診断", icon="🔍")
 simulation_page = st.Page("views/simulation.py", title="過去シミュレーション", icon="📊")
 quiz_page = st.Page("views/quiz.py", title="NISA学習・クイズ", icon="📝")
 mypage_page = st.Page("views/mypage.py", title="マイページ", icon="📂")

  # ナビゲーションの実行
 pg = st.navigation({
     "🤵 株兄さん メニュー": [home_page, diagnosis_page, simulation_page, quiz_page, mypage_page]
 })
 pg.run()



#  -------------------------------------------------
# ページ設定
#  -------------------------------------------------
 st.set_page_config(
     page_title="Investment Navigator",
     page_icon="📈",
     layout="wide"
 )

#  -------------------------------------------------
# ページ定義（ルーター）
#  -------------------------------------------------
 home_page = st.Page("views/home.py", title="ホーム", icon="🏠")
 quiz_page = st.Page("views/quiz.py", title="学習", icon="📚")
 diagnosis_page = st.Page("views/diagnosis.py", title="診断", icon="🧠")
 mypage_page = st.Page("views/mypage.py", title="マイページ", icon="👤")
 simulation_page = st.Page("views/simulation.py", title="シミュレーション", icon="📊")

  # -------------------------------------------------
  #ナビゲーション（統一構成）
  #-------------------------------------------------
 pg = st.navigation([
     home_page,
     quiz_page,
     diagnosis_page,
     simulation_page,
     mypage_page
 ])

 pg.run()


#  =========================================
#  ページ設定
#  =========================================
 st.set_page_config(
     page_title="株兄さん",
     page_icon="📈",
     layout="wide"
 )

  # =========================================
  #ヘッダー（アプリの世界観）
  #=========================================
 st.markdown("""
 <style>
 .title {
     font-size: 2.8rem;
     font-weight: 800;
     text-align: center;
     margin-top: 1rem;
 }

 .subtitle {
     text-align: center;
     color: 666;
     margin-bottom: 2rem;
 }

 .info-box {
     padding: 15px;
     border-radius: 12px;
     background: f5f7fb;
     border: 1px solid e6e6e6;
 }
 </style>
 """, unsafe_allow_html=True)

 st.markdown('<div class="title">📈 Investment Navigator</div>', unsafe_allow_html=True)
 st.markdown('<div class="subtitle">投資を学び、診断し、シミュレーションする総合アプリ</div>', unsafe_allow_html=True)

 st.divider()

 # =========================================
 # ナビゲーション（シンプルで迷わせない）
 # =========================================
 home_page = st.Page("views/home.py", title="ホーム", icon="🏠")
 quiz_page = st.Page("views/quiz.py", title="学習", icon="📚")
 diagnosis_page = st.Page("views/diagnosis.py", title="診断", icon="🧠")
 simulation_page = st.Page("views/simulation.py", title="シミュレーション", icon="📊")
 mypage_page = st.Page("views/mypage.py", title="マイページ", icon="👤")

 pg = st.navigation([
     home_page,
     quiz_page,
     diagnosis_page,
     simulation_page,
     mypage_page
 ])

  # =========================================
  #アプリ実行
  # =========================================
 pg.run()

 # =========================================
 # フッター（安心感）
 # =========================================
 st.divider()
 st.caption("© 2026 株兄さん | Learning & Simulation Platform")

 import streamlit as st

 # ==============================
 # ページ設定
 # ==============================
 st.set_page_config(
     page_title="株兄さん",
     page_icon="📈",
     layout="wide"
 )

 # ==============================
 # CSS
  #==============================
 st.markdown("""
 <style>
 .sidebar-title {
     font-size: 1.2rem;
     font-weight: 800;
     margin-bottom: 10px;
 }

 .active-page {
     background: e8f0ff;
     padding: 6px 10px;
     border-radius: 8px;
     font-weight: bold;
     color: 1f4bd8;
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
  #-----------------------------------------------------------------------------
 home_page = st.Page("views/home.py", title="ホーム", icon="🏠")
 quiz_page = st.Page("views/quiz.py", title="学習", icon="📚")
 diagnosis_page = st.Page("views/diagnosis.py", title="診断", icon="🧠")
 simulation_page = st.Page("views/simulation.py", title="シミュレーション", icon="📊")
 mypage_page = st.Page("views/mypage.py", title="マイページ", icon="👤")

 pages = {
     "ホーム": home_page,
     "学習": quiz_page,
     "診断": diagnosis_page,
     "シミュレーション": simulation_page,
     "マイページ": mypage_page
 }

 # ==============================
  #ナビゲーション
  #==============================
 pg = st.navigation(list(pages.values()))

  #==============================
  #サイドバー（アクティブ表示）
  #==============================
 with st.sidebar:
     st.markdown('<div class="sidebar-title">📈 Investment Navigator</div>', unsafe_allow_html=True)

     st.write("ナビゲーション")

     st.divider()

    #  現在ページの取得（Streamlit内部状態）
     current = st.session_state.get("current_page", None)

     # アクティブ表示（簡易ロジック）
     for name, page in pages.items():
         if current and str(current) == str(page):
             st.markdown(f"👉 <div class='active-page'>{name}</div>", unsafe_allow_html=True)
         else:
             st.write(f"{name}")

  #==============================
  # 実行
  #==============================
 pg.run()

  #==============================
  #フッター
  #==============================
 st.caption("株兄さん")



# ==========================================================
 #ページ設定
 #==========================================================
st.set_page_config(
    page_title="株兄さん",
    page_icon="📈",
    layout="wide"
)

 #==========================================================
# 共通CSS
 #==========================================================
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: fafafa;
}

.sidebar-title{
    font-size:1.5rem;
    font-weight:800;
    text-align:center;
    margin-bottom:0.2rem;
}

.sidebar-subtitle{
    text-align:center;
    color:666;
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
 #  ==========================================================
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
 #サイドバー
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
 #  ==========================================================
pg = st.navigation([
    home_page,
    quiz_page,
    diagnosis_page,
    simulation_page,
    mypage_page
])

pg.run()

#==========================================================
# フッター
 #==========================================================
st.markdown(
    '<div class="footer">Version 1.0.0</div>',
    unsafe_allow_html=True
)
