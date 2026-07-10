import streamlit as st
from streamlit.components.v1 import html as st_html

# ==============================
# 1. CSS（1画面に収めるための軽量化とブレ防止）
# ==============================
st.markdown(
    """
    <style>
    /* 全体の余白を徹底的に削除 */
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.2rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
    }
    /* ヘッダーやフッターの余分なスペースを削除 */
    header, footer {
        display: none !important;
    }
    /* ===== 再描画時のチラつき（がくがく）防止 ===== */
    /* 再実行中に古い要素が半透明になるフェードを無効化 */
    div[data-stale="true"] {
        opacity: 1 !important;
        transition: none !important;
    }
    /* 右上の "Running..." ステータス表示を非表示にして視覚ノイズを削減 */
    [data-testid="stStatusWidget"] {
        visibility: hidden !important;
    }
    /* 要素の出現アニメーションを無効化してレイアウトの揺れを抑える */
    .element-container, .stMarkdown, .stButton {
        animation: none !important;
    }
    .title {
        font-size: 1.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #2563eb, #0f766e);
        -webkit-background-clip: text;
        color: transparent;
        margin-bottom: 0.05rem;
        margin-top: 0.1rem;
    }
    .subtitle {
        font-size: 0.8rem;
        color: #475569;
        margin-bottom: 0.3rem;
    }
    .notice {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        padding: 0.3rem 0.6rem;
        border-radius: 0.5rem;
        color: #1e3a8a;
        margin-bottom: 0.4rem;
        font-weight: 500;
        font-size: 0.7rem;
    }
    .question-card {
        background: linear-gradient(180deg, #ffffff, #f8fbff);
        border: 1px solid #dbeafe;
        border-radius: 0.8rem;
        padding: 0.6rem 0.8rem;
        box-shadow: 0 4px 12px rgba(15,23,42,0.04);
        margin-bottom: 0.4rem;
    }
    .question-number {
        font-size: 0.7rem;
        font-weight: 700;
        color: #0f766e;
        margin-bottom: 0.1rem;
    }
    .question-text {
        font-size: 0.95rem;
        line-height: 1.4;
        color: #111827;
    }
    .progress-row {
        display: flex;
        align-items: center;
        gap: 0.3rem;
        margin-bottom: 0.2rem;
    }
    .progress-badge {
        background: #eff6ff;
        color: #2563eb;
        padding: 0.2rem 0.5rem;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 700;
    }
    .progress-text {
        color: #475569;
        font-size: 0.7rem;
    }
    /* 回答ボタン内の改行位置を制御:
       日本語の途中で勝手に折り返さず、ゼロ幅スペースの位置でのみ改行させる */
    .stButton > button p {
        word-break: keep-all !important;
        line-break: strict !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    .result-card {
        background: linear-gradient(180deg, #ffffff, #f5f8ff);
        border: 1px solid #c7d2fe;
        border-radius: 0.8rem;
        padding: 0.6rem 0.8rem;
        box-shadow: 0 10px 25px rgba(59,130,246,0.08);
        margin-bottom: 0.4rem;
    }
    .result-headline {
        font-size: 1.2rem;
        font-weight: 800;
        color: #1e40af;
        margin-bottom: 0.2rem;
    }
    .result-summary {
        color: #334155;
        line-height: 1.5;
        margin-bottom: 0.3rem;
        font-size: 0.85rem;
    }
    .product-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.6rem;
        padding: 0.5rem 0.6rem;
        margin-bottom: 0.3rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
    }
    .product-card h3 {
        font-size: 0.95rem !important;
        margin: 0.1rem 0 !important;
    }
    .product-card p, .product-card div {
        font-size: 0.75rem !important;
        line-height: 1.3 !important;
        margin: 0.1rem 0 !important;
    }
    .stButton > button {
        font-size: 0.75rem !important;
        padding: 0.2rem 0.5rem !important;
    }
    /* プログレスバーの高さを小さく */
    .stProgress [role="progressbar"],
    .stProgress [role="progressbar"] > div { height: 6px !important; }

    /* モバイル対応 */
    @media (max-width: 760px) {
        .title { font-size: 1.4rem !important; }
        .question-text { font-size: 0.85rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================
# 2. セッション状態の初期化
# ==============================
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 1
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "diagnosis_result" not in st.session_state:
    st.session_state.diagnosis_result = None
if "diagnosis_scores" not in st.session_state:
    st.session_state.diagnosis_scores = {}
if "scroll_to_top" not in st.session_state:
    st.session_state.scroll_to_top = True
if "fav_message" not in st.session_state:
    st.session_state.fav_message = None
if "fav_message_target" not in st.session_state:
    st.session_state.fav_message_target = None

# ==============================
# 3. 質問データと配点データ
# ==============================
TYPES = [
    "コツコツ積立型", "堅実安定型", "成長チャレンジ型", "世界分散型", "配当重視型",
    "インデックス型", "一点集中型", "短期チャレンジ型", "分析派型", "初心者安心型"
]

QUESTION_DATA = [
    {
        "text": "私は、多少の値下がりがあっても、高い利益を狙いたい。",
        "agree_scores": {"成長チャレンジ型": 1.0, "一点集中型": 0.7, "短期チャレンジ型": 0.7},
        "disagree_scores": {"堅実安定型": 1.0, "初心者安心型": 0.7, "コツコツ積立型": 0.7}
    },
    {
        "text": "私は、投資した商品を長期間持ち続けたい。",
        "agree_scores": {"コツコツ積立型": 1.0, "インデックス型": 0.7, "世界分散型": 0.7},
        "disagree_scores": {"短期チャレンジ型": 1.0, "一点集中型": 0.7}
    },
    {
        "text": "私は、投資先を一つに絞るより、複数に分散したい。",
        "agree_scores": {"世界分散型": 1.0, "インデックス型": 0.7, "堅実安定型": 0.7},
        "disagree_scores": {"一点集中型": 1.0, "成長チャレンジ型": 0.7}
    },
    {
        "text": "私は、値上がり益よりも、定期的に配当金を受け取りたい。",
        "agree_scores": {"配当重視型": 1.0, "堅実安定型": 0.7},
        "disagree_scores": {"成長チャレンジ型": 1.0, "一点集中型": 0.7}
    },
    {
        "text": "私は、株価や企業情報を自分で詳しく調べてから投資したい。",
        "agree_scores": {"分析派型": 1.0, "一点集中型": 0.7},
        "disagree_scores": {"初心者安心型": 1.0, "コツコツ積立型": 0.7}
    },
    {
        "text": "私は、株価を毎日確認したい。",
        "agree_scores": {"短期チャレンジ型": 1.0, "分析派型": 0.7, "一点集中型": 0.7},
        "disagree_scores": {"コツコツ積立型": 1.0, "世界分散型": 0.7, "インデックス型": 0.7}
    },
    {
        "text": "私は、世界中のさまざまな企業に投資したい。",
        "agree_scores": {"世界分散型": 1.0, "インデックス型": 0.7},
        "disagree_scores": {"一点集中型": 1.0}
    },
    {
        "text": "私は、難しいことはせずに、わかりやすい方法で投資したい。",
        "agree_scores": {"インデックス型": 1.0, "コツコツ積立型": 0.7, "初心者安心型": 0.7},
        "disagree_scores": {"一点集中型": 1.0, "分析派型": 0.7}
    },
    {
        "text": "私は、投資経験が少ないため、分かりやすく始めやすい方法を選びたい。",
        "agree_scores": {"初心者安心型": 1.0, "コツコツ積立型": 0.7, "堅実安定型": 0.7},
        "disagree_scores": {"分析派型": 1.0, "短期チャレンジ型": 0.7}
    },
    {
        "text": "私は、短期間で大きな利益を得ることに魅力を感じる。",
        "agree_scores": {"短期チャレンジ型": 1.0, "成長チャレンジ型": 0.7, "一点集中型": 0.7},
        "disagree_scores": {"コツコツ積立型": 1.0, "堅実安定型": 0.7, "世界分散型": 0.7}
    }
]

# ==============================
# 4. 診断結果データ
# ==============================
RESULT_DATA = {
    "コツコツ積立型": {
        "feature": "毎月少しずつ積み立てて、長く続けることに強いタイプです。",
        "method": "毎月の積立と長期保有を前提にした投資法が向いています。",
        "risk": "値動きに一喜一憂しすぎないことが大切です。",
        "products": [
            {"name": "eMAXIS Slim 米国株式（S&P500）", "reason": "長期で米国市場に投資しやすく、積立に向いています。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "世界の主要企業に広く分散されており、初心者にも扱いやすいです。"},
            {"name": "eMAXIS Slim 全世界株式（オール・カントリー）", "reason": "世界中の株式に分散しやすく、コツコツ積み立てるのに向いています。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "国や業種を広くカバーできるため、長期投資向きです。"},
            {"name": "VTI", "reason": "米国の大型企業に広く投資でき、長期の資産形成に向きます。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "シンプルな構成で、積立投資の選択肢として人気があります。"}
        ],
        "advice": "無理のない金額から始めて、毎月継続することが大切です。"
    },
    "堅実安定型": {
        "feature": "損失を抑えながら、落ち着いて資産を育てたいタイプです。",
        "method": "安定性の高い投資信託や債券型の商品を中心に考えると合います。",
        "risk": "大きな急騰は期待しにくいですが、比較的安心感があります。",
        "products": [
            {"name": "バランス型投資信託", "reason": "株と債券をバランスよく組み合わせて、安定性を重視した設計です。", "risk": "★★☆☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "初心者でも扱いやすいため、安定志向の方に向いています。"},
            {"name": "BND", "reason": "米国債券に投資でき、価格変動を抑えやすいです。", "risk": "★☆☆☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "安全寄りの資産配分を考えるうえで参考になります。"},
            {"name": "国内債券型投資信託", "reason": "安定性を重視したい方に向いています。", "risk": "★☆☆☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "価格変動は比較的小さめで、落ち着いて投資したい方に向きます。"}
        ],
        "advice": "急な値動きに一喜一憂しすぎず、長めの目線で見ましょう。"
    },
    "成長チャレンジ型": {
        "feature": "成長企業や新しいテーマに投資して、資産を大きく増やしたいタイプです。",
        "method": "成長性の高い企業やテーマ型商品を中心に考えると合います。",
        "risk": "値動きが大きく、短期で損失が出る可能性があります。",
        "products": [
            {"name": "NASDAQ100連動型投資信託", "reason": "成長企業に強い分野に投資できるため、伸びしろを狙いやすいです。", "risk": "★★★★☆", "return": "★★★★★", "dividend": "★☆☆☆☆", "diversification": "★★★★☆", "beginner": "★★☆☆☆", "description": "利益を狙いやすい反面、値動きが大きいです。"},
            {"name": "QQQ", "reason": "テクノロジー企業の成長性に注目したい方に人気です。", "risk": "★★★★☆", "return": "★★★★★", "dividend": "★☆☆☆☆", "diversification": "★★★★☆", "beginner": "★★☆☆☆", "description": "上昇余地が大きい一方で、下落時の耐性が必要です。"},
            {"name": "NVIDIA", "reason": "AI関連で注目度が高く、成長テーマを狙う方に向いています。", "risk": "★★★★★", "return": "★★★★★", "dividend": "★☆☆☆☆", "diversification": "★☆☆☆☆", "beginner": "★☆☆☆☆", "description": "値動きが大きく、短期での損益が出やすい商品です。"}
        ],
        "advice": "資金の一部に絞って、長期の視点で見ましょう。"
    },
    "世界分散型": {
        "feature": "世界中の企業に分散して投資したいタイプです。",
        "method": "全世界株式やグローバル型ETFを中心に考えると合います。",
        "risk": "地政学リスクなども含めて、幅広く分散するのがポイントです。",
        "products": [
            {"name": "eMAXIS Slim 全世界株式（オール・カントリー）", "reason": "世界中の企業に広く分散できるため、安定感を求める方に向いています。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "1つの国や業種に偏りにくいです。"},
            {"name": "VT", "reason": "全世界株式に投資できる代表的なETFです。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★☆", "description": "グローバルに分散したい方にとって扱いやすいです。"},
            {"name": "ACWI", "reason": "世界の大型株に分散しやすく、長期投資に向いています。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★☆", "description": "幅広い分散を重視するなら参考になります。"}
        ],
        "advice": "国や業種に偏りすぎないように、分散を意識しましょう。"
    },
    "配当重視型": {
        "feature": "配当金を受け取りながら、長期的に資産を育てたいタイプです。",
        "method": "高配当株や配当重視ETFを中心に考えると合います。",
        "risk": "値上がりより配当重視のため、成長性はやや抑えめです。",
        "products": [
            {"name": "VYM", "reason": "配当利回りの高い米国株に投資できるETFです。", "risk": "★★★☆☆", "return": "★★★☆☆", "dividend": "★★★★☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "配当の安定感を重視する方に向いています。"},
            {"name": "HDV", "reason": "高配当と安定性の両立を目指すETFです。", "risk": "★★★☆☆", "return": "★★★☆☆", "dividend": "★★★★☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "配当を得ながら長期保有しやすいです。"},
            {"name": "SPYD", "reason": "高配当株に投資でき、配当重視の方に人気があります。", "risk": "★★★☆☆", "return": "★★★☆☆", "dividend": "★★★★☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "定期的な配当を期待しやすいです。"}
        ],
        "advice": "配当だけに頼りすぎず、企業の成長性も確認しましょう。"
    },
    "インデックス型": {
        "feature": "市場全体に連動した投資を通じて、長期的に着実に増やしたいタイプです。",
        "method": "インデックス型ETFや投資信託を中心に考えると合います。",
        "risk": "全体の市場動向に左右されますが、比較的シンプルです。",
        "products": [
            {"name": "eMAXIS Slim 米国株式（S&P500）", "reason": "S&P500に連動し、長期投資の代表格です。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "シンプルで理解しやすく、積立にも向いています。"},
            {"name": "VOO", "reason": "S&P500に連動する代表的なETFです。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "米国の主要企業に広く投資できます。"},
            {"name": "TOPIX連動型投資信託", "reason": "日本市場全体に広く投資したい方に向いています。", "risk": "★★★☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★★★★☆", "beginner": "★★★★☆", "description": "日本株の動きに合わせて考えやすいです。"}
        ],
        "advice": "手数料や分散のしやすさを意識すると、より効率的です。"
    },
    "一点集中型": {
        "feature": "好きな企業やテーマに絞って投資したいタイプです。",
        "method": "個別株に関心がある方に向いています。",
        "risk": "1社に依存しやすく、損失の幅が大きくなりやすいです。",
        "products": [
            {"name": "Apple", "reason": "ブランド力の強い企業で、長期投資の代表例です。", "risk": "★★★☆☆", "return": "★★★★☆", "dividend": "★★★☆☆", "diversification": "★☆☆☆☆", "beginner": "★★☆☆☆", "description": "人気が高く、長期的な成長を期待しやすいです。"},
            {"name": "Microsoft", "reason": "業績の安定感が高く、長期保有しやすい企業です。", "risk": "★★★☆☆", "return": "★★★★☆", "dividend": "★★★☆☆", "diversification": "★☆☆☆☆", "beginner": "★★☆☆☆", "description": "成長と安定の両方を考えやすいです。"},
            {"name": "NVIDIA", "reason": "成長テーマに強い企業として注目されやすいです。", "risk": "★★★★★", "return": "★★★★★", "dividend": "★☆☆☆☆", "diversification": "★☆☆☆☆", "beginner": "★☆☆☆☆", "description": "急な値上がりと下落の両方が出やすいです。"}
        ],
        "advice": "資金を絞って投資し、1社に寄せすぎないように注意しましょう。"
    },
    "短期チャレンジ型": {
        "feature": "短期間で値動きの大きい銘柄を追いかけ、利益を狙いたいタイプです。",
        "method": "テーマ型ETFや成長株など、短期で動きやすい商品に関心が向きます。",
        "risk": "値動きが大きく、損失も出やすいです。",
        "products": [
            {"name": "テーマ型ETF", "reason": "特定のテーマに沿って動くため、短期の流れを追いやすいです。", "risk": "★★★★☆", "return": "★★★★☆", "dividend": "★☆☆☆☆", "diversification": "★★★☆☆", "beginner": "★☆☆☆☆", "description": "テーマの変化で値動きが大きくなりやすいです。"},
            {"name": "成長株", "reason": "短期で上昇する可能性が高い銘柄を探しやすいです。", "risk": "★★★★☆", "return": "★★★★☆", "dividend": "★☆☆☆☆", "diversification": "★☆☆☆☆", "beginner": "★☆☆☆☆", "description": "急に上がる一方で、急に下がることもあります。"},
            {"name": "値動きの大きい個別株", "reason": "短期の値動きを狙う方に向いています。", "risk": "★★★★★", "return": "★★★★★", "dividend": "★☆☆☆☆", "diversification": "★☆☆☆☆", "beginner": "★☆☆☆☆", "description": "高いリターンが期待できる反面、リスクも非常に高いです。"}
        ],
        "advice": "投資金額を小さくし、損失を許容できる範囲に留めましょう。"
    },
    "分析派型": {
        "feature": "企業分析や市場の動きをしっかり見て、納得しながら投資したいタイプです。",
        "method": "財務分析や業績を重視した投資に向いています。",
        "risk": "情報収集を重ねることで、判断の精度を上げやすいです。",
        "products": [
            {"name": "QUAL", "reason": "品質重視の株式に投資できるETFです。", "risk": "★★★☆☆", "return": "★★★★☆", "dividend": "★★★☆☆", "diversification": "★★★★☆", "beginner": "★★★☆☆", "description": "企業の品質を重視して選びたい方に向いています。"},
            {"name": "財務状況が安定した個別株", "reason": "企業の業績や財務をじっくり確認したい方に向いています。", "risk": "★★★☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★☆☆☆☆", "beginner": "★★☆☆☆", "description": "分析に基づいて選ぶことで、比較的安定した判断がしやすいです。"},
            {"name": "S&P500連動型ETF", "reason": "市場全体の成長性と安定性を見たい方に向いています。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★☆", "description": "分析しやすい構成で、投資の基礎を学ぶのにも向いています。"}
        ],
        "advice": "情報を集めること自体は大事ですが、判断基準を一つに絞りすぎないようにしましょう。"
    },
    "初心者安心型": {
        "feature": "まずは安心して始めたい、投資の基礎を学びたいタイプです。",
        "method": "分散された投資信託やインデックスを中心に始めると合います。",
        "risk": "最初は大きな値動きに驚かないよう、シンプルな選び方が向いています。",
        "products": [
            {"name": "eMAXIS Slim 全世界株式（オール・カントリー）", "reason": "初心者でも使いやすく、世界中に分散しやすいです。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "投資の入門として非常に扱いやすいです。"},
            {"name": "eMAXIS Slim 米国株式（S&P500）", "reason": "米国の代表的な企業群に投資でき、理解しやすいです。", "risk": "★★☆☆☆", "return": "★★★★☆", "dividend": "★★☆☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "投資の基礎を学びながら始める人に向いています。"},
            {"name": "バランス型投資信託", "reason": "株と債券を組み合わせて、初心者でも安心して始めやすいです。", "risk": "★★☆☆☆", "return": "★★★☆☆", "dividend": "★★★☆☆", "diversification": "★★★★★", "beginner": "★★★★★", "description": "リスクとリターンのバランスを取りやすいです。"}
        ],
        "advice": "まずは少額から始めて、投資の仕組みを理解することが大切です。"
    }
}

# ==============================
# 5. ヘルパー関数
# ==============================
def reset_diagnosis():
    st.session_state.current_question = 1
    st.session_state.answers = {}
    st.session_state.diagnosis_result = None
    st.session_state.diagnosis_scores = {}
    st.session_state.scroll_to_top = True


def calculate_result(answers):
    scores = {t: 0 for t in TYPES}
    for idx, answer in enumerate(answers):
        if answer is None:
            continue
        question = QUESTION_DATA[idx]
        if answer > 0:
            multiplier = {1: 0.25, 2: 0.5, 3: 1.0}.get(answer, 0)
            for t, value in question["agree_scores"].items():
                scores[t] += value * multiplier
        elif answer < 0:
            multiplier = {-1: 0.25, -2: 0.5, -3: 1.0}.get(answer, 0)
            for t, value in question["disagree_scores"].items():
                scores[t] += value * multiplier

    tie_priority = [
        "初心者安心型", "コツコツ積立型", "堅実安定型", "インデックス型", "世界分散型",
        "配当重視型", "分析派型", "成長チャレンジ型", "一点集中型", "短期チャレンジ型"
    ]
    max_score = max(scores.values())
    top_types = [t for t, s in scores.items() if s == max_score]
    if len(top_types) == 1:
        return top_types[0], scores
    for t in tie_priority:
        if t in top_types:
            return t, scores
    return top_types[0], scores


# ------------------------------
# コールバック関数（on_click用）
# rerunを明示的に呼ばず、ボタンクリックの1回の再実行だけで
# 状態を更新することで、画面のがくつき（二重描画）を防ぐ
# ------------------------------
def on_select_answer(current, val, total_questions):
    st.session_state.answers[current] = val
    if current < total_questions:
        st.session_state.current_question = current + 1
    else:
        # 最後の質問 → 診断結果を計算
        answers_list = [st.session_state.answers.get(i + 1) for i in range(total_questions)]
        result_type, scores = calculate_result(answers_list)
        st.session_state.diagnosis_result = result_type
        st.session_state.diagnosis_scores = scores
    st.session_state.scroll_to_top = True


def on_go_prev():
    st.session_state.current_question -= 1
    st.session_state.scroll_to_top = True


def on_add_favorite(name):
    if name not in st.session_state.favorites:
        st.session_state.favorites.append(name)
        st.session_state.fav_message = ("success", "お気に入りに追加しました")
    else:
        st.session_state.fav_message = ("info", "すでにお気に入りに登録されています")
    st.session_state.fav_message_target = name


# ------------------------------
# 五角形レーダーチャート（SVG生成・外部ライブラリ不要）
# ------------------------------
def star_to_num(star_str):
    """'★★★☆☆' → 3"""
    return star_str.count("★")


def render_radar_svg(product, size=220):
    """5段階評価を統合した五角形レーダーチャートのSVGを返す"""
    import math

    labels = ["リスク", "リターン", "配当", "分散性", "初心者向け"]
    values = [
        star_to_num(product["risk"]),
        star_to_num(product["return"]),
        star_to_num(product["dividend"]),
        star_to_num(product["diversification"]),
        star_to_num(product["beginner"]),
    ]

    cx = cy = size / 2
    radius = size / 2 - 42  # ラベル用の余白を確保
    n = 5

    def point(i, r):
        angle = -math.pi / 2 + 2 * math.pi * i / n  # 頂点を真上から時計回り
        return cx + r * math.cos(angle), cy + r * math.sin(angle)

    # 目盛りの五角形（1〜5）
    grid = ""
    for level in range(1, 6):
        r = radius * level / 5
        pts = " ".join(f"{point(i, r)[0]:.1f},{point(i, r)[1]:.1f}" for i in range(n))
        grid += f'<polygon points="{pts}" fill="none" stroke="#dbeafe" stroke-width="1"/>'

    # 中心から各頂点への軸線
    axes = ""
    for i in range(n):
        x, y = point(i, radius)
        axes += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#dbeafe" stroke-width="1"/>'

    # 評価値のポリゴン
    val_pts = " ".join(
        f"{point(i, radius * v / 5)[0]:.1f},{point(i, radius * v / 5)[1]:.1f}"
        for i, v in enumerate(values)
    )
    data_poly = (
        f'<polygon points="{val_pts}" fill="rgba(37,99,235,0.25)" '
        f'stroke="#2563eb" stroke-width="2"/>'
    )

    # 各頂点のマーカー
    dots = ""
    for i, v in enumerate(values):
        x, y = point(i, radius * v / 5)
        dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#2563eb"/>'

    # ラベル（数値付き）
    texts = ""
    for i, (label, v) in enumerate(zip(labels, values)):
        x, y = point(i, radius + 22)
        anchor = "middle"
        if x < cx - 5:
            anchor = "end"
        elif x > cx + 5:
            anchor = "start"
        dy = 4 if abs(y - cy) < radius else (12 if y > cy else 0)
        texts += (
            f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" '
            f'font-size="10" fill="#334155" font-weight="600">{label} {v}</text>'
        )

    return (
        f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" '
        f'xmlns="http://www.w3.org/2000/svg" style="display:block;margin:0 auto;">'
        f"{grid}{axes}{data_poly}{dots}{texts}</svg>"
    )


def render_product_card(product):
    """結果画面のカードレイアウト（コンパクト版）
    カード全体を1回のst.markdownで出力する（divを分割すると枠が内容を囲まない）"""
    st.markdown(
        f'<div class="product-card">'
        f'<h3>{product["name"]}</h3>'
        f'<p><strong>特徴</strong>: {product["description"]}</p>'
        f'<p><strong>向いている理由</strong>: {product["reason"]}</p>'
        f'{render_radar_svg(product)}'  # 5段階評価を統合した五角形レーダーチャート
        f'</div>',
        unsafe_allow_html=True,
    )

    st.button(
        "お気に入りに追加",
        key=f"fav_{product['name']}",
        use_container_width=True,
        on_click=on_add_favorite,
        args=(product["name"],),
    )
    # コールバックで積んだメッセージをここで表示
    if st.session_state.get("fav_message_target") == product["name"]:
        kind, msg = st.session_state.fav_message
        (st.success if kind == "success" else st.info)(msg)
        st.session_state.fav_message_target = None


# ==============================
# 6. メイン画面
# ==============================
st.markdown('<div class="title">投資タイプ診断</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">10問に答えて、あなたに合った投資タイプを見つけましょう</div>', unsafe_allow_html=True)
st.markdown('<div class="notice">本診断は投資判断性のものであり、勧誘を目的としません</div>', unsafe_allow_html=True)

if st.session_state.scroll_to_top:
    st_html("<script>window.parent.document.querySelector('.main').scrollTo({top: 0, behavior: 'instant'});</script>", height=0)
    st.session_state.scroll_to_top = False

# ------------------------------
# 診断中画面（1画面ずつ表示）
# ------------------------------
if st.session_state.diagnosis_result is None:
    total_questions = len(QUESTION_DATA)
    current = st.session_state.current_question
    
    # プログレス表示
    progress_pct = current / total_questions
    st.progress(progress_pct, text=f"質問 {current} / {total_questions}")
    
    # 質問カード
    # 注意: <div>の開始と終了を別々のst.markdownに分けると、Streamlitが
    # 未閉鎖のdivを自動で閉じてしまい「空のカード枠+外にはみ出た文字」になる。
    # 必ず1回のst.markdownで完結させること。
    q = QUESTION_DATA[current - 1]
    st.markdown(
        f'<div class="question-card">'
        #f'<div class="question-number">質問 {current}</div>'
        f'<div class="question-text">{q["text"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    
    # 回答ボタン（-3 ～ +3 の7段階）
    # ゼロ幅スペース(\u200b)を入れた位置でのみ改行される
    # （CSS側の word-break: keep-all とセットで機能する）
    ZW = "\u200b"
    labels = [
        f"全く{ZW}そう思わない",
        "そう思わない",
        f"やや{ZW}そう思わない",
        f"どちらでも{ZW}ない",
        f"やや{ZW}そう思う",
        "そう思う",
        f"強く{ZW}そう思う",
    ]
    values = [-3, -2, -1, 0, 1, 2, 3]
    
    cols = st.columns(7)
    for i, (col, label, val) in enumerate(zip(cols, labels, values)):
        with col:
            # 既に回答済みの場合の表示
            is_selected = st.session_state.answers.get(current) == val
            btn_type = "primary" if is_selected else "secondary"
            # on_click方式: クリック時の1回の再実行内で状態更新が完了するため、
            # st.rerun()による2回目の描画が発生せず、画面のがくつきがなくなる
            st.button(
                label,
                key=f"q{current}_v{val}",
                use_container_width=True,
                type=btn_type,
                on_click=on_select_answer,
                args=(current, val, total_questions),
            )
    
    # ナビゲーションボタン（選択肢を押すと自動で次に進むため「次へ」は廃止）
    nav_cols = st.columns([1, 1])
    with nav_cols[0]:
        if current > 1:
            st.button("← 前へ", use_container_width=True, on_click=on_go_prev)
    with nav_cols[1]:
        st.button("最初からやり直す", use_container_width=True, on_click=reset_diagnosis)

# ------------------------------
# 診断結果画面
# ------------------------------
else:
    result_type = st.session_state.diagnosis_result
    result = RESULT_DATA[result_type]
    
    # 注意: HTMLタグ(<div>)の内側ではmarkdown記法(**太字**)は効かないため、
    # <strong>タグを使う。divの開閉も1回のst.markdownで完結させる。
    st.markdown(
        f'<div class="result-card">'
        f'<div class="result-headline">あなたの投資タイプ: {result_type}</div>'
        f'<div class="result-summary"><strong>特徴</strong>: {result["feature"]}</div>'
        f'<div class="result-summary"><strong>投資方法</strong>: {result["method"]}</div>'
        f'<div class="result-summary"><strong>リスク</strong>: {result["risk"]}</div>'
        f'<div class="result-summary"><strong>アドバイス</strong>: {result["advice"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    
    # おすすめ商品
    st.subheader("おすすめの投資商品")
    for product in result["products"]:
        render_product_card(product)
    
    # お気に入り表示
    if st.session_state.favorites:
        st.subheader("お気に入りに追加した商品")
        for fav in st.session_state.favorites:
            st.write(f"• {fav}")
    
    # ボタン
    col1, col2 = st.columns(2)
    with col1:
        st.button("もう一度診断する", use_container_width=True, on_click=reset_diagnosis)
    with col2:
        if st.button("結果をシェア", use_container_width=True):
            st.info("シェア機能は準備中です")