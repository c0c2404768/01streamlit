import streamlit as st
import pandas as pd

st.markdown("<h2 style='color:#FF6B6B;'>🔍 華麗なる投資スタイル診断</h2>", unsafe_allow_html=True)

# 💡 ページを切り替えても「診断中かどうか」を記憶するフラグを初期化
if "has_diagnosed" not in st.session_state:
    st.session_state.has_diagnosed = False

# 質問コーナー
with st.container():
    q1 = st.selectbox("Q1. 投資に何を一番求めている？", ["とにかく安心・安全", "安定した配当(お小遣い)", "ドカンと大きな成長", "好きなブランドを応援"])
    q2 = st.radio("Q2. キミの性格はどっち？", ["石橋を叩いて渡る慎重派", "新しいことに挑戦したい冒険派"])
    
if st.button("運命の結果を見る ✨"):
    st.balloons()
    
    # 回答からタイプを判定
    if q1 == "とにかく安心・安全": user_type = "安心コツコツ型"
    elif q1 == "安定した配当(お小遣い)": user_type = "日本インフラ堅実型"
    else: user_type = "ワクワク成長チャレンジ型"
    
    # 💡 診断が完了したことを記憶させる！
    st.session_state.user_type = user_type
    st.session_state.has_diagnosed = True

# --- 💡 ここから下が最重要対策！ ---
# 診断ボタンが押された直後、または「お気に入り」を押してページが再実行された後でも、
# 過去に診断したデータが残っていれば結果を表示し続けるようにします。
if st.session_state.has_diagnosed:
    current_type = st.session_state.user_type
    profile = st.session_state.INVESTMENT_PROFILES[current_type]
    
    st.markdown(f"""
        <div class='result-card'>
            <h3 style='color:#FF6B6B;'>キミは… 【{current_type}】だ！</h3>
            <p style='font-size:1.1rem;'>{profile['description']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### 💡 株兄さん直伝！おすすめの銘柄たち")
    
    # おすすめ銘柄のループ表示
    for stock in profile["stocks"]:
        with st.expander(f"⭐ {stock['name']}"):
            cols = st.columns([2, 1])
            
            with cols[0]:
                st.write(f"**【兄さんの推しポイント】**\n{stock['reason']}")
                
                # 🛠️ お気に入り追加ボタン（これで消えずにしっかり動く！）
                if st.button(f"お気に入りに追加 ({stock['name']})", key=f"add_fav_{stock['name']}"):
                    if "favorites" not in st.session_state:
                        st.session_state.favorites = []
                        
                    if stock['name'] not in st.session_state.favorites:
                        st.session_state.favorites.append(stock['name'])
                        st.toast(f"「{stock['name']}」を登録したぜ！✨")
                    else:
                        st.warning("すでに登録されているぜ！")
                
            with cols[1]:
                st.write("ステータス")
                s_df = pd.DataFrame({"項目": ["安全", "成長", "お得"], "Lv": stock['stats']})
                st.bar_chart(s_df.set_index("項目"), height=150)