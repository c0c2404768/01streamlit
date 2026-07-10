import streamlit as st

# ==============================
# 1. CSS
# ==============================
st.markdown(
    """
    <style>
    .title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1f6feb;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #4b5563;
        margin-bottom: 0.8rem;
    }
    .notice {
        background: #f8fbff;
        border: 1px solid #dbeafe;
        padding: 0.8rem 1rem;
        border-radius: 0.8rem;
        color: #374151;
        margin-bottom: 1rem;
    }
    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        color: #111827;
    }
    .result-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #0f766e;
        margin-bottom: 0.4rem;
    }
    .product-card {
        background: #f9fcff;
        border: 1px solid #dbeafe;
        border-radius: 0.8rem;
        padding: 0.9rem;
        margin-bottom: 0.8rem;
        color: #111827;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================
# 3. セッション状態の初期化
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
if "diagnosis_answers" not in st.session_state:
    st.session_state.diagnosis_answers = {}

# ==============================
# 4. 質問データと配点データ
# ==============================
TYPES = [
    "コツコツ積立型",
    "堅実安定型",
    "成長チャレンジ型",
    "世界分散型",
    "配当重視型",
    "インデックス型",
    "一点集中型",
    "短期チャレンジ型",
    "分析派型",
    "初心者安心型",
]

QUESTION_DATA = [
    {
        "question": "あなたが投資で一番大切にしたいことは？",
        "options": [
            "できるだけ損をしたくない",
            "少しずつでも着実に増やしたい",
            "大きく資産を増やしたい",
            "投資について学びながら始めたい",
        ],
        "scores": {
            "堅実安定型": 2,
            "初心者安心型": 1,
            "コツコツ積立型": 1,
            "成長チャレンジ型": 2,
            "一点集中型": 1,
            "分析派型": 1,
            "インデックス型": 1,
            "世界分散型": 1,
        },
    },
    {
        "question": "投資したお金が1か月で20％下がったら？",
        "options": [
            "すぐ売る",
            "様子を見る",
            "そのまま持ち続ける",
            "安くなったので追加で買う",
        ],
        "scores": {
            "堅実安定型": 1,
            "初心者安心型": 1,
            "コツコツ積立型": 1,
            "分析派型": 2,
            "世界分散型": 1,
            "成長チャレンジ型": 1,
            "短期チャレンジ型": 1,
            "インデックス型": 1,
            "一点集中型": 1,
        },
    },
    {
        "question": "投資はどれくらい続けたいですか？",
        "options": [
            "1年未満",
            "1～3年",
            "5年以上",
            "老後まで長く続けたい",
        ],
        "scores": {
            "短期チャレンジ型": 1,
            "コツコツ積立型": 2,
            "堅実安定型": 1,
            "初心者安心型": 2,
            "インデックス型": 1,
            "世界分散型": 1,
            "配当重視型": 1,
        },
    },
    {
        "question": "あなたはどんな利益がうれしいですか？",
        "options": [
            "毎年配当金がもらえる",
            "資産が少しずつ増える",
            "短期間で大きく値上がりする",
            "どれが自分に合うか知りたい",
        ],
        "scores": {
            "配当重視型": 2,
            "コツコツ積立型": 1,
            "堅実安定型": 1,
            "成長チャレンジ型": 2,
            "短期チャレンジ型": 2,
            "初心者安心型": 1,
            "分析派型": 1,
        },
    },
    {
        "question": "投資先はどのように選びたいですか？",
        "options": [
            "世界中に幅広く分散したい",
            "日本やアメリカの有名企業が安心",
            "好きな企業に集中したい",
            "おすすめされたものを選びたい",
        ],
        "scores": {
            "世界分散型": 2,
            "インデックス型": 1,
            "初心者安心型": 1,
            "一点集中型": 2,
            "分析派型": 1,
            "堅実安定型": 1,
        },
    },
    {
        "question": "株価はどれくらい確認したいですか？",
        "options": [
            "毎日確認したい",
            "週に数回",
            "月に1回くらい",
            "ほとんど見ない",
        ],
        "scores": {
            "短期チャレンジ型": 2,
            "分析派型": 1,
            "成長チャレンジ型": 1,
            "コツコツ積立型": 1,
            "初心者安心型": 1,
            "世界分散型": 1,
        },
    },
    {
        "question": "投資経験はありますか？",
        "options": [
            "全くない",
            "少しだけある",
            "NISAなどを利用している",
            "個別株も売買したことがある",
        ],
        "scores": {
            "初心者安心型": 2,
            "コツコツ積立型": 1,
            "インデックス型": 1,
            "分析派型": 1,
            "成長チャレンジ型": 1,
            "一点集中型": 1,
        },
    },
    {
        "question": "あなたは投資するとき、どのように判断しますか？",
        "options": [
            "しっかり調べて納得してから買う",
            "人気の商品を選ぶ",
            "自分の直感も大切にする",
            "診断結果やおすすめを参考にする",
        ],
        "scores": {
            "分析派型": 2,
            "初心者安心型": 2,
            "成長チャレンジ型": 1,
            "一点集中型": 1,
            "コツコツ積立型": 1,
            "インデックス型": 1,
        },
    },
    {
        "question": "次のうち、一番興味があるものは？",
        "options": [
            "高配当株",
            "S&P500などのインデックス",
            "AIや半導体などの成長企業",
            "世界中への分散投資",
        ],
        "scores": {
            "配当重視型": 2,
            "インデックス型": 2,
            "成長チャレンジ型": 2,
            "世界分散型": 2,
            "分析派型": 1,
        },
    },
    {
        "question": "将来どんな投資家になりたいですか？",
        "options": [
            "安定して資産を増やしたい",
            "コツコツ積み立てたい",
            "大きな利益を狙いたい",
            "知識を身につけて賢く運用したい",
        ],
        "scores": {
            "堅実安定型": 2,
            "コツコツ積立型": 2,
            "成長チャレンジ型": 2,
            "分析派型": 2,
            "初心者安心型": 1,
        },
    },
]

# ==============================
# 5. 診断結果データ
# ==============================
RESULT_DATA = {
    "コツコツ積立型": {
        "feature": "毎月少しずつ積み立てて、長く続けることに強いタイプです。",
        "method": "毎月の積立と長期保有を前提にした投資法が向いています。",
        "risk": "値動きに一喜一憂しすぎないことが大切です。",
        "products": [
            {
                "name": "eMAXIS Slim 米国株式（S&P500）",
                "reason": "長期で米国市場に投資しやすく、積立に向いています。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "世界の主要企業に広く分散されており、初心者にも扱いやすいです。",
            },
            {
                "name": "eMAXIS Slim 全世界株式（オール・カントリー）",
                "reason": "世界中の株式に分散しやすく、コツコツ積み立てるのに向いています。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "国や業種を広くカバーできるため、長期投資向きです。",
            },
            {
                "name": "VTI",
                "reason": "米国の大型企業に広く投資でき、長期の資産形成に向きます。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "シンプルな構成で、積立投資の選択肢として人気があります。",
            },
        ],
        "advice": "無理のない金額から始めて、毎月継続することが大切です。",
    },
    "堅実安定型": {
        "feature": "損失を抑えながら、落ち着いて資産を育てたいタイプです。",
        "method": "安定性の高い投資信託や債券型の商品を中心に考えると合います。",
        "risk": "大きな急騰は期待しにくいですが、比較的安心感があります。",
        "products": [
            {
                "name": "バランス型投資信託",
                "reason": "株と債券をバランスよく組み合わせて、安定性を重視した設計です。",
                "risk": "★★☆☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "初心者でも扱いやすいため、安定志向の方に向いています。",
            },
            {
                "name": "BND",
                "reason": "米国債券に投資でき、価格変動を抑えやすいです。",
                "risk": "★☆☆☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "安全寄りの資産配分を考えるうえで参考になります。",
            },
            {
                "name": "国内債券型投資信託",
                "reason": "安定性を重視したい方に向いています。",
                "risk": "★☆☆☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "価格変動は比較的小さめで、落ち着いて投資したい方に向きます。",
            },
        ],
        "advice": "急な値動きに一喜一憂しすぎず、長めの目線で見ましょう。",
    },
    "成長チャレンジ型": {
        "feature": "成長企業や新しいテーマに投資して、資産を大きく増やしたいタイプです。",
        "method": "成長性の高い企業やテーマ型商品を中心に考えると合います。",
        "risk": "値動きが大きく、短期で損失が出る可能性があります。",
        "products": [
            {
                "name": "NASDAQ100連動型投資信託",
                "reason": "成長企業に強い分野に投資できるため、伸びしろを狙いやすいです。",
                "risk": "★★★★☆",
                "return": "★★★★★",
                "dividend": "★☆☆☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★☆☆☆",
                "description": "利益を狙いやすい反面、値動きが大きいです。",
            },
            {
                "name": "QQQ",
                "reason": "テクノロジー企業の成長性に注目したい方に人気です。",
                "risk": "★★★★☆",
                "return": "★★★★★",
                "dividend": "★☆☆☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★☆☆☆",
                "description": "上昇余地が大きい一方で、下落時の耐性が必要です。",
            },
            {
                "name": "NVIDIA",
                "reason": "AI関連で注目度が高く、成長テーマを狙う方に向いています。",
                "risk": "★★★★★",
                "return": "★★★★★",
                "dividend": "★☆☆☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★☆☆☆☆",
                "description": "値動きが大きく、短期での損益が出やすい商品です。",
            },
        ],
        "advice": "資金の一部に絞って、長期の視点で見ましょう。",
    },
    "世界分散型": {
        "feature": "世界中の企業に分散して投資したいタイプです。",
        "method": "全世界株式やグローバル型ETFを中心に考えると合います。",
        "risk": "地政学リスクなども含めて、幅広く分散するのがポイントです。",
        "products": [
            {
                "name": "eMAXIS Slim 全世界株式（オール・カントリー）",
                "reason": "世界中の企業に広く分散できるため、安定感を求める方に向いています。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "1つの国や業種に偏りにくいです。",
            },
            {
                "name": "VT",
                "reason": "全世界株式に投資できる代表的なETFです。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★☆",
                "description": "グローバルに分散したい方にとって扱いやすいです。",
            },
            {
                "name": "ACWI",
                "reason": "世界の大型株に分散しやすく、長期投資に向いています。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★☆",
                "description": "幅広い分散を重視するなら参考になります。",
            },
        ],
        "advice": "国や業種に偏りすぎないように、分散を意識しましょう。",
    },
    "配当重視型": {
        "feature": "配当金を受け取りながら、長期的に資産を育てたいタイプです。",
        "method": "高配当株や配当重視ETFを中心に考えると合います。",
        "risk": "値上がりより配当重視のため、成長性はやや抑えめです。",
        "products": [
            {
                "name": "VYM",
                "reason": "配当利回りの高い米国株に投資できるETFです。",
                "risk": "★★★☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★★☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "配当の安定感を重視する方に向いています。",
            },
            {
                "name": "HDV",
                "reason": "高配当と安定性の両立を目指すETFです。",
                "risk": "★★★☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★★☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "配当を得ながら長期保有しやすいです。",
            },
            {
                "name": "SPYD",
                "reason": "高配当株に投資でき、配当重視の方に人気があります。",
                "risk": "★★★☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★★☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "定期的な配当を期待しやすいです。",
            },
        ],
        "advice": "配当だけに頼りすぎず、企業の成長性も確認しましょう。",
    },
    "インデックス型": {
        "feature": "市場全体に連動した投資を通じて、長期的に着実に増やしたいタイプです。",
        "method": "インデックス型ETFや投資信託を中心に考えると合います。",
        "risk": "全体の市場動向に左右されますが、比較的シンプルです。",
        "products": [
            {
                "name": "eMAXIS Slim 米国株式（S&P500）",
                "reason": "S&P500に連動し、長期投資の代表格です。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "シンプルで理解しやすく、積立にも向いています。",
            },
            {
                "name": "VOO",
                "reason": "S&P500に連動する代表的なETFです。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "米国の主要企業に広く投資できます。",
            },
            {
                "name": "TOPIX連動型投資信託",
                "reason": "日本市場全体に広く投資したい方に向いています。",
                "risk": "★★★☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★★★☆",
                "description": "日本株の動きに合わせて考えやすいです。",
            },
        ],
        "advice": "手数料や分散のしやすさを意識すると、より効率的です。",
    },
    "一点集中型": {
        "feature": "好きな企業やテーマに絞って投資したいタイプです。",
        "method": "個別株に関心がある方に向いています。",
        "risk": "1社に依存しやすく、損失の幅が大きくなりやすいです。",
        "products": [
            {
                "name": "Apple",
                "reason": "ブランド力の強い企業で、長期投資の代表例です。",
                "risk": "★★★☆☆",
                "return": "★★★★☆",
                "dividend": "★★★☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★★☆☆☆",
                "description": "人気が高く、長期的な成長を期待しやすいです。",
            },
            {
                "name": "Microsoft",
                "reason": "業績の安定感が高く、長期保有しやすい企業です。",
                "risk": "★★★☆☆",
                "return": "★★★★☆",
                "dividend": "★★★☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★★☆☆☆",
                "description": "成長と安定の両方を考えやすいです。",
            },
            {
                "name": "NVIDIA",
                "reason": "成長テーマに強い企業として注目されやすいです。",
                "risk": "★★★★★",
                "return": "★★★★★",
                "dividend": "★☆☆☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★☆☆☆☆",
                "description": "急な値上がりと下落の両方が出やすいです。",
            },
        ],
        "advice": "資金を絞って投資し、1社に寄せすぎないように注意しましょう。",
    },
    "短期チャレンジ型": {
        "feature": "短期間で値動きの大きい銘柄を追いかけ、利益を狙いたいタイプです。",
        "method": "テーマ型ETFや成長株など、短期で動きやすい商品に関心が向きます。",
        "risk": "値動きが大きく、損失も出やすいです。",
        "products": [
            {
                "name": "テーマ型ETF",
                "reason": "特定のテーマに沿って動くため、短期の流れを追いやすいです。",
                "risk": "★★★★☆",
                "return": "★★★★☆",
                "dividend": "★☆☆☆☆",
                "diversification": "★★★☆☆",
                "beginner": "★☆☆☆☆",
                "description": "テーマの変化で値動きが大きくなりやすいです。",
            },
            {
                "name": "成長株",
                "reason": "短期で上昇する可能性が高い銘柄を探しやすいです。",
                "risk": "★★★★☆",
                "return": "★★★★☆",
                "dividend": "★☆☆☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★☆☆☆☆",
                "description": "急に上がる一方で、急に下がることもあります。",
            },
            {
                "name": "値動きの大きい個別株",
                "reason": "短期の値動きを狙う方に向いています。",
                "risk": "★★★★★",
                "return": "★★★★★",
                "dividend": "★☆☆☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★☆☆☆☆",
                "description": "高いリターンが期待できる反面、リスクも非常に高いです。",
            },
        ],
        "advice": "投資金額を小さくし、損失を許容できる範囲に留めましょう。",
    },
    "分析派型": {
        "feature": "企業分析や市場の動きをしっかり見て、納得しながら投資したいタイプです。",
        "method": "財務分析や業績を重視した投資に向いています。",
        "risk": "情報収集を重ねることで、判断の精度を上げやすいです。",
        "products": [
            {
                "name": "QUAL",
                "reason": "品質重視の株式に投資できるETFです。",
                "risk": "★★★☆☆",
                "return": "★★★★☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★☆",
                "beginner": "★★★☆☆",
                "description": "企業の品質を重視して選びたい方に向いています。",
            },
            {
                "name": "財務状況が安定した個別株",
                "reason": "企業の業績や財務をじっくり確認したい方に向いています。",
                "risk": "★★★☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★☆☆☆☆",
                "beginner": "★★☆☆☆",
                "description": "分析に基づいて選ぶことで、比較的安定した判断がしやすいです。",
            },
            {
                "name": "S&P500連動型ETF",
                "reason": "市場全体の成長性と安定性を見たい方に向いています。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★☆",
                "description": "分析しやすい構成で、投資の基礎を学ぶのにも向いています。",
            },
        ],
        "advice": "情報を集めること自体は大事ですが、判断基準を一つに絞りすぎないようにしましょう。",
    },
    "初心者安心型": {
        "feature": "まずは安心して始めたい、投資の基礎を学びたいタイプです。",
        "method": "分散された投資信託やインデックスを中心に始めると合います。",
        "risk": "最初は大きな値動きに驚かないよう、シンプルな選び方が向いています。",
        "products": [
            {
                "name": "eMAXIS Slim 全世界株式（オール・カントリー）",
                "reason": "初心者でも使いやすく、世界中に分散しやすいです。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "投資の入門として非常に扱いやすいです。",
            },
            {
                "name": "eMAXIS Slim 米国株式（S&P500）",
                "reason": "米国の代表的な企業群に投資でき、理解しやすいです。",
                "risk": "★★☆☆☆",
                "return": "★★★★☆",
                "dividend": "★★☆☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "投資の基礎を学びながら始める人に向いています。",
            },
            {
                "name": "バランス型投資信託",
                "reason": "株と債券を組み合わせて、初心者でも安心して始めやすいです。",
                "risk": "★★☆☆☆",
                "return": "★★★☆☆",
                "dividend": "★★★☆☆",
                "diversification": "★★★★★",
                "beginner": "★★★★★",
                "description": "リスクとリターンのバランスを取りやすいです。",
            },
        ],
        "advice": "まずは少額から始めて、投資の仕組みを理解することが大切です。",
    },
}

# ==============================
# 6. ヘルパー関数
# ==============================
def reset_diagnosis():
    st.session_state.current_question = 1
    st.session_state.answers = {}
    st.session_state.diagnosis_result = None
    st.session_state.diagnosis_scores = {}
    st.session_state.diagnosis_answers = {}


def calculate_result(answers):
    scores = {t: 0 for t in TYPES}

    for idx, answer in enumerate(answers):
        if answer is None:
            continue
        question = QUESTION_DATA[idx]
        for t in TYPES:
            scores[t] += question["scores"].get(t, 0)

    tie_priority = [
        "初心者安心型",
        "コツコツ積立型",
        "堅実安定型",
        "インデックス型",
        "世界分散型",
        "配当重視型",
        "分析派型",
        "成長チャレンジ型",
        "一点集中型",
        "短期チャレンジ型",
    ]

    max_score = max(scores.values())
    top_types = [t for t, s in scores.items() if s == max_score]

    if len(top_types) == 1:
        return top_types[0], scores

    for t in tie_priority:
        if t in top_types:
            return t, scores

    return top_types[0], scores


def render_product_card(product):
    st.markdown(
        f"""
        <div class='product-card'>
            <div style='font-weight:700; font-size:1.05rem; color:#0f172a;'>{product['name']}</div>
            <div style='color:#4b5563; margin-top:0.3rem;'>{product['reason']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(f"特徴: {product['description']}")
    st.write(f"向いている理由: {product['reason']}")
    st.write(f"評価: リスク {product['risk']} / リターン {product['return']} / 配当 {product['dividend']}")
    st.write(f"分散性: {product['diversification']} / 初心者向け度: {product['beginner']}")

    if st.button(f"お気に入りに追加: {product['name']}", key=f"fav_{product['name']}"):
        if product['name'] not in st.session_state.favorites:
            st.session_state.favorites.append(product['name'])
            st.success("お気に入りに追加しました")
        else:
            st.info("すでにお気に入りに登録されています")


def handle_answer_change():
    current_idx = st.session_state.current_question - 1
    selection_key = f"answer_{st.session_state.current_question}"
    selected_option = st.session_state.get(selection_key)

    if selected_option is None:
        return

    st.session_state.answers[current_idx] = selected_option
    st.session_state.diagnosis_answers = dict(st.session_state.answers)

    if st.session_state.current_question < len(QUESTION_DATA):
        st.session_state.current_question += 1
    else:
        result_type, scores = calculate_result([st.session_state.answers.get(i) for i in range(len(QUESTION_DATA))])
        st.session_state.diagnosis_result = result_type
        st.session_state.diagnosis_scores = scores

# ==============================
# 7. メイン画面
# ==============================
st.markdown('<div class="title">投資タイプ診断</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">10問に答えて、あなたに合った投資タイプを見つけましょう</div>', unsafe_allow_html=True)
st.markdown('<div class="notice">本診断は投資判断の参考情報であり、投資を勧誘するものではありません</div>', unsafe_allow_html=True)

if st.session_state.diagnosis_result is None:
    current_idx = st.session_state.current_question - 1
    question = QUESTION_DATA[current_idx]

    progress_value = st.session_state.current_question / len(QUESTION_DATA)
    st.progress(progress_value)
    st.write(f"質問 {st.session_state.current_question} / {len(QUESTION_DATA)}")

    for idx in range(min(st.session_state.current_question - 1, len(QUESTION_DATA))):
        if idx in st.session_state.answers:
            st.markdown(
                f"<div class='card'><b>{idx + 1}. {QUESTION_DATA[idx]['question']}</b><br><span style='color:#2563eb;'>→ {st.session_state.answers[idx]}</span></div>",
                unsafe_allow_html=True,
            )

    st.markdown(f"<div class='card'><b>{question['question']}</b></div>", unsafe_allow_html=True)

    selection_key = f"answer_{st.session_state.current_question}"
    if selection_key not in st.session_state:
        saved_value = st.session_state.answers.get(current_idx)
        st.session_state[selection_key] = saved_value if saved_value is not None else question["options"][0]

    default_value = st.session_state[selection_key]
    if default_value not in question["options"]:
        default_value = question["options"][0]

    st.radio(
        "選択してください",
        question["options"],
        index=question["options"].index(default_value),
        key=selection_key,
        on_change=handle_answer_change,
    )

    if st.session_state.current_question > 1:
        if st.button("前の質問へ戻る", key=f"prev_btn_{st.session_state.current_question}"):
            if st.session_state.current_question > 1:
                st.session_state.current_question -= 1
                st.session_state.diagnosis_answers = dict(st.session_state.answers)

else:
    result_type = st.session_state.diagnosis_result
    result_data = RESULT_DATA[result_type]

    st.markdown(f"<div class='card'><div class='result-title'>あなたは {result_type} です！</div>", unsafe_allow_html=True)
    st.write(result_data["feature"])
    st.write(f"**向いている投資方法**：{result_data['method']}")
    st.write(f"**注意点**：{result_data['risk']}")
    st.write("**おすすめの銘柄・ETF・投資信託（参考例）**")

    for product in result_data["products"]:
        render_product_card(product)

    st.write(f"**ワンポイントアドバイス**：{result_data['advice']}")
    st.write("診断結果をもとにした参考例です")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("診断をやり直す"):
        reset_diagnosis()
