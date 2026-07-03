# import streamlit as st

# st.markdown("<h1 class='hero-title'>✨ 株兄さん v2.1 ✨</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; font-size:1.2rem; color:#666;'>新NISA対応！キミの未来を華麗に彩る投資診断アプリ</p>", unsafe_allow_html=True)

# st.image("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

# cols = st.columns(4)
# with cols[0]:
#     st.markdown("### 💎 銘柄拡充")
#     st.write("人気の優待株や巨大企業など、選りすぐりのラインナップだ。")
# with cols[1]:
#     st.markdown("### 🎨 華やかUI")
#     st.write("投資のワクワクを視覚で感じる、リッチな画面体験を届けるぜ。")
# with cols[2]:
#     st.markdown("### 🚀 未来予測")
#     st.write("過去のデータから、キミの資産がどう化けるかをシミュレーション！")
# with cols[3]:
#     st.markdown("### 📝 クイズ学習")
#     st.write("ゲーム感覚で新NISAの基礎を学べるクイズ部屋だぜ!")

#     #----------------------
# import streamlit as st
# import requests

# # ----------------------------------------
# # ページ設定
# # ----------------------------------------
# st.set_page_config(
#     page_title="Investment Navigator",
#     page_icon="📈",
#     layout="wide"
# )

# # ----------------------------------------
# # ネットワーク接続確認
# # ----------------------------------------
# def check_internet():
#     try:
#         requests.get("https://www.google.com", timeout=3)
#         return True
#     except requests.RequestException:
#         return False

# if not check_internet():
#     st.error("⚠ インターネットに接続できません。")
#     st.warning("ネットワーク接続を確認してから再度お試しください。")
#     st.stop()

# # ----------------------------------------
# # タイトル
# # ----------------------------------------
# st.title("📈 Investment Navigator")
# st.caption("投資を学び、診断し、資産形成をサポートするアプリ")

# st.divider()

# st.markdown("""
# ### ようこそ！

# このアプリでは、

# - 📚 投資について学ぶ
# - 🧠 あなたに合った投資タイプを診断する
# - 👤 自分の情報や診断結果を管理する
# - 📈 将来の資産をシミュレーションする

# といった機能を利用できます。

# ※ 現在開発中のため、一部機能は未完成です。
# """)

# st.divider()

# st.subheader("メニュー")

# col1, col2 = st.columns(2)

# with col1:
#     with st.container(border=True):
#         st.markdown("## 📚 学習")
#         st.write("投資の基礎知識を学びます。")
#         st.info("🚧 開発中で")
#         if st.button("学習ページへ", use_container_width=True):
#             st.switch_page("pages/1_学習.py")

# with col2:
#     with st.container(border=True):
#         st.markdown("## 🧠 診断")
#         st.write("質問に答えて投資タイプを診断します。")
#         st.info("🚧 開発中")
#         if st.button("診断ページへ", use_container_width=True):
#             st.switch_page("pages/2_診断.py")

# col3, col4 = st.columns(2)

# with col3:
#     with st.container(border=True):
#         st.markdown("## 👤 マイページ")
#         st.write("診断結果や登録情報を確認できます。")
#         st.info("🚧 開発中")
#         if st.button("マイページへ", use_container_width=True):
#             st.switch_page("pages/3_マイページ.py")

# with col4:
#     with st.container(border=True):
#         st.markdown("## 📈 シミュレーション")
#         st.write("資産運用の将来予測を行います。")
#         st.info("🚧 開発中")
#         if st.button("シミュレーションへ", use_container_width=True):
#             st.switch_page("pages/4_シミュレーション.py")

# st.divider()
# st.caption("Version 0.1.0（開発中）")

# import streamlit as st

# # -------------------------------------------------
# # ページUI（ホーム専用・表示のみ）
# # -------------------------------------------------

# st.title("📈 株兄さん")

# st.markdown("""
# ## ようこそ

# このアプリでは以下の機能を利用できます。

# - 📚 投資の基礎を学ぶ
# - 🧠 投資タイプ診断
# - 👤 マイページで結果管理
# - 📊 シミュレーションで将来予測

# 左のメニューから機能を選択してください。
# """)

# st.divider()

# # -------------------------------------------------
# # 機能カードUI
# # -------------------------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("📚 学習")
#     st.write("投資の基礎から体系的に学習します。")

# with col2:
#     st.subheader("🧠 診断")
#     st.write("あなたの投資タイプを分析します。")

# col3, col4 = st.columns(2)

# with col3:
#     st.subheader("👤 マイページ")
#     st.write("診断結果や履歴を確認できます。")

# with col4:
#     st.subheader("📊 シミュレーション")
#     st.write("将来の資産推移を確認できます。")

# st.divider()

# st.caption("Investment Navigator | Streamlit App")

# import streamlit as st

# # ==============================
# # ページ設定
# # ==============================
# st.set_page_config(
#     page_title="株兄さん",
#     page_icon="📈",
#     layout="wide"
# )

# # ==============================
# # CSS（シンプルなUI強化のみ）
# # ==============================
# st.markdown("""
# <style>
# .title {
#     font-size: 2.8rem;
#     font-weight: 800;
#     text-align: center;
#     margin-bottom: 0.5rem;
# }

# .subtitle {
#     text-align: center;
#     color: #666;
#     margin-bottom: 2rem;
# }

# .section {
#     padding: 20px;
#     border-radius: 16px;
#     border: 1px solid #eee;
#     margin-bottom: 15px;
# }

# .section h3 {
#     margin-bottom: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ==============================
# # ヘッダー
# # ==============================
# st.markdown('<div class="title">📈 Investment Navigator</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">投資を学び、理解し、判断するためのアプリ</div>', unsafe_allow_html=True)

# st.divider()

# # ==============================
# # 機能紹介（静的・事実のみ）
# # ==============================
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown('<div class="section">', unsafe_allow_html=True)
#     st.subheader("📚 学習")
#     st.write("投資の基礎知識を体系的に学習するページです。")
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('<div class="section">', unsafe_allow_html=True)
#     st.subheader("👤 マイページ")
#     st.write("登録情報や履歴を確認するページです。")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div class="section">', unsafe_allow_html=True)
#     st.subheader("🧠 診断")
#     st.write("質問に基づいて投資傾向を分析するページです。")
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('<div class="section">', unsafe_allow_html=True)
#     st.subheader("📊 シミュレーション")
#     st.write("投資の将来イメージを確認するページです。")
#     st.markdown('</div>', unsafe_allow_html=True)

# st.divider()

# # ==============================
# # アプリ説明（事実ベースのみ）
# # ==============================
# st.subheader("📌 このアプリについて")

# st.write("""
# Investment Navigator は、投資の理解を目的とした学習アプリです。

# - 学習コンテンツの閲覧
# - 投資診断機能
# - マイページ管理
# - シミュレーション機能

# これらの機能を通じて、投資の基礎理解を深めることを目的としています。
# """)

# st.divider()

# # ==============================
# # フッター
# # ==============================
# st.caption("Investment Navigator | Home")

# import streamlit as st

# # ==============================
# # ページ設定
# # ==============================
# st.set_page_config(
#     page_title="株兄さん",
#     page_icon="📈",
#     layout="wide"
# )

# # ==============================
# # CSS（視認性＋カード強化）
# # ==============================
# st.markdown("""
# <style>

# .main-title {
#     font-size: 3rem;
#     font-weight: 900;
#     text-align: center;
#     margin-bottom: 0.2rem;
# }

# .sub-title {
#     text-align: center;
#     color: #666;
#     margin-bottom: 2rem;
#     font-size: 1.1rem;
# }

# .card {
#     background: white;
#     padding: 20px;
#     border-radius: 16px;
#     border: 1px solid #eee;
#     box-shadow: 0 6px 18px rgba(0,0,0,0.05);
#     margin-bottom: 15px;
#     transition: 0.2s;
# }

# .card:hover {
#     transform: translateY(-3px);
#     box-shadow: 0 10px 25px rgba(0,0,0,0.08);
# }

# .section-title {
#     font-size: 1.2rem;
#     font-weight: 800;
#     margin-bottom: 8px;
# }

# .small-text {
#     color: #666;
#     font-size: 0.95rem;
# }

# </style>
# """, unsafe_allow_html=True)

# # ==============================
# # ヘッダー（入口感）
# # ==============================
# st.markdown('<div class="main-title">📈 Investment Navigator</div>', unsafe_allow_html=True)
# st.markdown('<div class="sub-title">投資を学び・理解し・判断するための学習アプリ</div>', unsafe_allow_html=True)

# st.divider()

# # ==============================
# # メイン機能（カードUI）
# # ==============================
# col1, col2 = st.columns(2)

# with col1:

#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="section-title">📚 学習</div>', unsafe_allow_html=True)
#     st.markdown('<div class="small-text">投資の基礎から応用まで体系的に学べます</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="section-title">👤 マイページ</div>', unsafe_allow_html=True)
#     st.markdown('<div class="small-text">学習状況や診断結果を管理できます</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# with col2:

#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="section-title">🧠 診断</div>', unsafe_allow_html=True)
#     st.markdown('<div class="small-text">質問に基づいて投資タイプを分析します</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.markdown('<div class="section-title">📊 シミュレーション</div>', unsafe_allow_html=True)
#     st.markdown('<div class="small-text">将来の資産推移を確認できます</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# st.divider()

# # ==============================
# # アプリ説明（整理）
# # ==============================
# st.subheader("📌 このアプリについて")

# st.info("""
# Investment Navigatorは、投資の基礎理解を目的とした学習アプリです。

# ・学習コンテンツ  
# ・投資診断  
# ・マイページ管理  
# ・シミュレーション  

# これらを通じて投資の理解を深めます。
# """)

# st.divider()

# # ==============================
# # フッター
# # ==============================
# st.caption("Investment Navigator | Home")

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
# ==============================
st.markdown("""
<style>

.title {
    font-size: 3rem;
    font-weight: 900;
    text-align: center;
    margin-bottom: 0.2rem;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 2rem;
}

.page-label {
    font-size: 1.2rem;
    font-weight: 800;
    margin-bottom: 6px;
    margin-top: 12px;
    color: #333;
}

.card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #eee;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 15px;
}

.card-text {
    color: #666;
    font-size: 0.95rem;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# タイトル（株兄さん）
# ==============================
st.markdown('<div class="title">📈 株兄さん</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">投資を学び・理解し・判断するためのアプリ</div>', unsafe_allow_html=True)

st.divider()

# ==============================
# カードUI（ページ名を上に表示）
# ==============================

# 学習
st.markdown('<div class="page-label">📚 学習</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
投資の基礎から応用まで体系的に学習できます。
</div>
""", unsafe_allow_html=True)

# 診断
st.markdown('<div class="page-label">🧠 診断</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
質問に基づいて投資タイプを分析します。
</div>
""", unsafe_allow_html=True)

# マイページ
st.markdown('<div class="page-label">👤 マイページ</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
学習状況や診断結果を管理できます。
</div>
""", unsafe_allow_html=True)

# シミュレーション
st.markdown('<div class="page-label">📊 シミュレーション</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
将来の資産推移を確認できます。
</div>
""", unsafe_allow_html=True)

st.divider()

# ==============================
# フッター
# ==============================
st.caption("株兄さん | Home")