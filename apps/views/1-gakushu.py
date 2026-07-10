import streamlit as st

st.markdown(
    """
    <style>
    body { overflow-x: hidden; }
    .study-title {
        color: #C2410C;
        font-weight: 800;
        margin-bottom: 0.2rem;
        text-shadow: 0 1px 1px rgba(0,0,0,0.05);
    }
    .study-hero {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFFDF2 100%);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        border: 1px solid #FED7AA;
        color: #7C2D12;
    }
    .study-card {
        background: #FFF7ED;
        border-left: 6px solid #F97316;
        padding: 18px 20px;
        border-radius: 14px;
        margin: 12px 0 18px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        color: #431407;
    }
    .study-card-blue {
        background: #F8FAFC;
        border-left: 6px solid #2563EB;
        padding: 18px 20px;
        border-radius: 14px;
        margin: 12px 0 18px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        color: #0F172A;
    }
    .study-card-green {
        background: #F0FDF4;
        border-left: 6px solid #16A34A;
        padding: 18px 20px;
        border-radius: 14px;
        margin: 12px 0 18px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        color: #052E16;
    }
    .term-badge {
        display: inline-block;
        background: #F97316;
        color: white;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-bottom: 6px;
        font-weight: 700;
    }
    .stApp, .stMarkdown, .stTextInput, .stSelectbox, .stTextArea, .stButton, .stTabs [role="tab"], .stExpander, .stMetric {
        color: #111827 !important;
    }
    .stMarkdown p, .stMarkdown li, .stMarkdown div {
        color: #111827;
        line-height: 1.7;
        font-size: 1rem;
    }
    .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #111827;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
    }
    .stMetric [data-testid="stMetricLabel"] {
        color: #374151 !important;
    }
    .stSelectbox label, .stTextInput label {
        color: #111827 !important;
        font-weight: 700 !important;
    }
    .streamlit-expanderHeader {
        color: #111827 !important;
        font-weight: 700 !important;
    }
    .stAlert > div {
        color: #111827;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h2 class='study-title' style='display:none;'>📘 株兄さんの投資学習ルーム</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="study-hero" style="display:none;">
        <p style="margin: 0; font-size: 1rem; line-height: 1.7;">
            投資初心者向けに、<strong>新NISA</strong>・<strong>投資用語</strong>・<strong>基本の考え方</strong>をわかりやすく学べるページです。
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("学ぶ内容", "3つのテーマ")
with col2:
    st.metric("特徴", "初心者向け")
with col3:
    st.metric("最後に", "クイズで確認")

st.divider()

tabs = st.tabs(["💡 新NISA入門", "📚 投資用語集", "📈 投資の基本", "⚔️ 理解度クイズ"])

with tabs[0]:
    st.subheader("💡 3分でわかる新NISA")

    st.markdown(
        """
        <div class="study-card">
            <h3>① 新NISAとは？</h3>
            <p>新NISAは、投資で得た利益にかかる税金を非課税にできる制度です。長期的に資産形成を考える人にとって、始めやすい仕組みです。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="study-card">
            <h3>② なぜ初心者に向いているのか？</h3>
            <p>少額から始めやすく、毎月コツコツ積み立てる投資と相性が良いため、投資経験が少ない人でも取り組みやすいのが特徴です。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="study-card-blue">
            <h3>③ 株兄さん直伝・始め方3ステップ</h3>
            <ol>
                <li>証券会社で口座を開設する</li>
                <li>NISA口座を申し込む</li>
                <li>少額から積立投資を始める</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,

    )
    st.warning("注意：新NISAを使っても元本保証ではありません。価格は上下するため、損失が出る可能性があります。")

with tabs[1]:
    st.subheader("📚 初心者向け 投資用語集")

    terms = [
        {
            "カテゴリ": "基本",
            "用語": "リターン",
            "説明": "投資によって得られる利益率のことです。値上がり益や配当などが含まれます。",
            "例": "100万円が110万円になった場合、リターンは10%です。",
        },
        {
            "カテゴリ": "基本",
            "用語": "リスク",
            "説明": "投資では主に価格変動の大きさを意味します。リスクが高いほど大きく増える可能性もありますが、大きく下がる可能性もあります。",
            "例": "株価が大きく上下する銘柄はリスクが高いと考えられます。",
        },
        {
            "カテゴリ": "基本",
            "用語": "分散投資",
            "説明": "複数の銘柄や地域に投資することで、特定の銘柄だけに依存するリスクを下げる方法です。",
            "例": "日本株だけでなく、米国株や全世界株式にも投資する考え方です。",
        },
        {
            "カテゴリ": "商品",
            "用語": "投資信託",
            "説明": "投資家から集めたお金を専門家がまとめて運用する金融商品です。",
            "例": "S&P500に連動する投資信託などがあります。",
        },
        {
            "カテゴリ": "商品",
            "用語": "ETF",
            "説明": "証券取引所に上場している投資信託です。株式のように売買できます。",
            "例": "VOOやQQQなどが代表的なETFです。",
        },
        {
            "カテゴリ": "分析",
            "用語": "ボラティリティ",
            "説明": "価格変動の大きさを表す指標です。値が大きいほど価格の上下が激しいことを意味します。",
            "例": "Nasdaq100は成長性が高い一方、ボラティリティも高くなりやすいです。",
        },
    ]

    categories = ["すべて"] + sorted({term["カテゴリ"] for term in terms})
    selected_category = st.selectbox("カテゴリで絞り込み", categories)

    display_terms = terms if selected_category == "すべて" else [term for term in terms if term["カテゴリ"] == selected_category]

    for term in display_terms:
        with st.expander(term["用語"]):
            st.markdown(f"<span class='term-badge'>{term['カテゴリ']}</span>", unsafe_allow_html=True)
            st.write(term["説明"])
            st.caption(f"例：{term['例']}")

with tabs[2]:
    st.subheader("📈 投資初心者が押さえるべき基本")

    st.markdown(
        """
        <div class="study-card">
            <h3>① 長期投資</h3>
            <p>短期の値動きに振り回されず、長い期間で資産形成を目指す考え方です。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="study-card">
            <h3>② 積立投資</h3>
            <p>毎月一定額を投資することで、価格の高低にかかわらずコツコツ買うことができます。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="study-card-green">
            <h3>③ 分散投資</h3>
            <p>一つの銘柄や一つの国だけに頼らず、複数に分けることでリスクを抑えやすくなります。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info("株兄さんポイント：初心者は「長期・積立・分散」を意識すると、理解しやすくなります。")

with tabs[3]:
    st.subheader("⚔️腕試し！投資クイズ")
    st.write("学んだ内容を確認するためのクイズです。すべて選択してから採点してください。")

    questions = [
        {
            "問題": "Q1. 新NISAの大きな特徴として正しいものは？",
            "選択肢": [
                "投資で得た利益が必ず増える",
                "投資で得た利益にかかる税金を非課税にできる",
                "どの銘柄を買っても損をしない",
            ],
            "答え": "投資で得た利益にかかる税金を非課税にできる",
            "解説": "新NISAは利益が必ず出る制度ではなく、利益にかかる税金を非課税にできる制度です。",
        },
        {
            "問題": "Q2. 分散投資の目的として正しいものは？",
            "選択肢": [
                "一つの銘柄に集中して大きく利益を狙うため",
                "投資先を分けてリスクを抑えるため",
                "株価の変動を完全になくすため",
            ],
            "答え": "投資先を分けてリスクを抑えるため",
            "解説": "分散投資はリスクを完全になくすものではありませんが、特定の投資先に依存するリスクを下げる効果があります。",
        },
        {
            "問題": "Q3. ボラティリティが高いとはどういう意味？",
            "選択肢": ["価格変動が大きい", "必ず利益が出る", "税金が安い"],
            "答え": "価格変動が大きい",
            "解説": "ボラティリティは価格変動の大きさを表します。高いほど値動きが大きくなります。",
        },
        {
            "問題": "Q4. シャープレシオは何を表す指標？",
            "選択肢": ["投資金額の大きさ", "リスクに対するリターンの効率性", "企業の売上高"],
            "答え": "リスクに対するリターンの効率性",
            "解説": "シャープレシオは、リスク1単位あたりにどれだけリターンを得られたかを表します。",
        },
        {
            "問題": "Q5. 初心者が意識しやすい投資の基本として適切なものは？",
            "選択肢": ["短期・集中・一括", "長期・積立・分散", "直感・流行・全額投資"],
            "答え": "長期・積立・分散",
            "解説": "初心者は長期・積立・分散を意識することで、リスクを抑えながら投資を学びやすくなります。",
        },
    ]

    user_answers = {}
    for i, q in enumerate(questions):
        user_answers[i] = st.selectbox(q["問題"], ["選択してください"] + q["選択肢"], key=f"learning_quiz_{i}")

    if st.button("採点する ✨"):
        if "選択してください" in user_answers.values():
            st.warning("すべての問題に回答してください。")
        else:
            score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["答え"])
            st.markdown(f"### 結果：{score} / {len(questions)} 点")

            if score == len(questions):
                st.success("🎉 全問正解！投資の基本はかなり理解できているぜ！")
                st.balloons()
            elif score >= 3:
                st.info("いい感じ！間違えたところを確認すればさらに理解が深まるぜ。")
            else:
                st.warning("もう一度、上の学習タブを読んで復習してみよう。")

            st.divider()
            st.subheader("解説")
            for i, q in enumerate(questions):
                if user_answers[i] == q["答え"]:
                    st.success(f"{q['問題']}：正解")
                else:
                    st.error(f"{q['問題']}：不正解")
                st.write(f"正解：{q['答え']}")
                st.caption(q["解説"])
