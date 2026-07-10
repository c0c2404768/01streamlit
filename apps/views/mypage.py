import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.parse
import calendar
import uuid
from datetime import datetime

st.markdown("<h2 style='color:#FF6B6B;'>📂 キミの専用マイページ</h2>", unsafe_allow_html=True)

if "memos" not in st.session_state:
    st.session_state.memos = []

if "calendar_year" not in st.session_state:
    st.session_state.calendar_year = datetime.now().year

if "calendar_month" not in st.session_state:
    st.session_state.calendar_month = datetime.now().month

if "selected_calendar_date" not in st.session_state:
    st.session_state.selected_calendar_date = datetime.now().date()

# -----------------------------------------------------------------------------
# 1. 🏆 診断結果の記録と共有
# -----------------------------------------------------------------------------
st.markdown("### 🏆 診断結果の記録")
diagnosis_type = st.session_state.get("diagnosis_result") or st.session_state.get("user_type")

if diagnosis_type:
    profile = st.session_state.get("INVESTMENT_PROFILES", {}).get(diagnosis_type)
    description = st.session_state.get("diagnosis_feature")
    if not description and profile:
        description = profile.get("description")
    if not description:
        description = "診断結果は保存されているぜ。もう一度診断ページで確認もできるぞ。"
    
    st.markdown(f"""
        <div class='result-card'>
            <h4 style='color:#FF6B6B;'>現在の診断タイプ：{diagnosis_type}</h4>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    share_text = f"株兄さんで診断した結果、私は「{diagnosis_type}」だったぜ！✨ #株兄さん #新NISA"
    share_url = "https://your-app-url.streamlit.app/"
    
    col_sns1, col_sns2 = st.columns(2)
    with col_sns1:
        x_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(share_text)}&url={share_url}"
        st.link_button("𝕏 (Twitter)で結果を自慢する", x_url, use_container_width=True)
    with col_sns2:
        line_url = f"https://social-plugins.line.me/lineit/share?url={urllib.parse.quote(share_url)}&text={urllib.parse.quote(share_text)}"
        st.link_button("LINEで仲間に送る", line_url, use_container_width=True)
else:
    st.info("まだ診断を受けていないようだな！「投資診断」ページへGOだぜ！🚀")
    if st.button("投資診断ページへ移動する", key="go_to_diagnosis", type="primary"):
        st.switch_page("views/diagnosis.py")


# -----------------------------------------------------------------------------
# 2. ⭐ 他のページから追加されたお気に入りの表示と管理
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### ⭐ お気に入り銘柄リスト")

# もし他ページでエラーが起きてもマイページが壊れないように安全装置を配置
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if not st.session_state.favorites:
    st.info("まだお気に入りがないぜ！診断やお宝銘柄を見つけてこいよな！")
else:
    st.write("現在のお気に入りリスト（個別削除もできるぜ）：")
    
    # リスト表示と個別削除
    for fav in st.session_state.favorites:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- <span class='stock-badge'>{fav}</span>", unsafe_allow_html=True)
        with col2:
            # 個別削除ボタン（キーが重複しないように銘柄名を仕込む）
            if st.button("削除", key=f"delete_{fav}"):
                st.session_state.favorites.remove(fav)
                st.rerun()


# -----------------------------------------------------------------------------
# 3. 📊 気なる銘柄を比較・確認
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📊 銘柄比較チャート")

if len(st.session_state.favorites) < 2:
    st.warning("比較するには、他のページで2つ以上の銘柄をお気に入りに追加してくれ！")
else:
    compare_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    if "compare_selected" not in st.session_state:
        st.session_state.compare_selected = st.session_state.favorites[:2]

    st.session_state.compare_selected = [
        name for name in st.session_state.compare_selected
        if name in st.session_state.favorites
    ]

    st.write("比較したい銘柄をボタンで選んでくれ：")
    button_columns = st.columns(min(3, len(st.session_state.favorites)))

    for index, name in enumerate(st.session_state.favorites):
        column = button_columns[index % len(button_columns)]
        is_selected = name in st.session_state.compare_selected
        with column:
            button_type = "primary" if is_selected else "secondary"
            if st.button(name, key=f"compare_{index}", use_container_width=True, type=button_type):
                if is_selected:
                    st.session_state.compare_selected.remove(name)
                else:
                    st.session_state.compare_selected.append(name)
                st.rerun()

    selected_favs = st.session_state.compare_selected
    st.caption(f"選択中: {', '.join(selected_favs) if selected_favs else 'なし'}")

    if len(selected_favs) >= 2:
        compare_data = []
        favorite_stats = st.session_state.get("favorite_stock_stats", {})
        all_stocks_data = []
        for p in st.session_state.INVESTMENT_PROFILES.values():
            all_stocks_data.extend(p["stocks"])

        for name in selected_favs:
            stock_info = next((s for s in all_stocks_data if s["name"] == name), None)
            if stock_info:
                compare_data.append({
                    "名前": name,
                    "安全": stock_info["stats"][0],
                    "成長": stock_info["stats"][1],
                    "お得": stock_info["stats"][2]
                })
                continue

            if name in favorite_stats:
                stats = favorite_stats[name]
                if len(stats) == 3:
                    compare_data.append({
                        "名前": name,
                        "安全": stats[0],
                        "成長": stats[1],
                        "お得": stats[2]
                    })

        if len(compare_data) < 2:
            st.warning("選択した銘柄の比較データが足りないぜ。別の銘柄を選んでみてくれ。")
        else:
            df_compare = pd.DataFrame(compare_data)

            fig = go.Figure()
            metrics = ["安全", "成長", "お得"]

            for index, row in df_compare.reset_index(drop=True).iterrows():
                fig.add_trace(go.Bar(
                    name=row["名前"],
                    x=metrics,
                    y=[row["安全"], row["成長"], row["お得"]],
                    marker_color=compare_palette[index % len(compare_palette)]
                ))

            fig.update_layout(
                barmode='group',
                xaxis_title="評価項目",
                yaxis_title="レベル (1-5)",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("比較するには、ボタンで2つ以上の銘柄を選んでくれ。")


# -----------------------------------------------------------------------------
# 4. 📝 メモ機能
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📝 メモ")
st.caption("気づきや次に買いたい銘柄を、ここにそのまま残せるぜ。")

calendar_col1, calendar_col2, calendar_col3 = st.columns([1, 2, 1])
with calendar_col1:
    if st.button("◀ 前月", key="calendar_prev_month", use_container_width=True):
        if st.session_state.calendar_month == 1:
            st.session_state.calendar_month = 12
            st.session_state.calendar_year -= 1
        else:
            st.session_state.calendar_month -= 1
        st.rerun()

with calendar_col2:
    st.markdown(
        f"<div style='text-align:center; font-weight:700; font-size:1.15rem;'>{st.session_state.calendar_year}年 {st.session_state.calendar_month}月</div>",
        unsafe_allow_html=True,
    )

with calendar_col3:
    if st.button("次月 ▶", key="calendar_next_month", use_container_width=True):
        if st.session_state.calendar_month == 12:
            st.session_state.calendar_month = 1
            st.session_state.calendar_year += 1
        else:
            st.session_state.calendar_month += 1
        st.rerun()

calendar_weekdays = ["日", "月", "火", "水", "木", "金", "土"]
weekday_columns = st.columns(7)
for index, weekday in enumerate(calendar_weekdays):
    weekday_columns[index].markdown(
        f"<div style='text-align:center; font-weight:700; color:#666;'>{weekday}</div>",
        unsafe_allow_html=True,
    )

month_matrix = calendar.Calendar(firstweekday=6).monthdayscalendar(
    st.session_state.calendar_year,
    st.session_state.calendar_month,
)

memo_date_counts = {}
for memo in st.session_state.memos:
    memo_date_counts[memo.get("memo_date", memo["created_at"][:10])] = memo_date_counts.get(memo.get("memo_date", memo["created_at"][:10]), 0) + 1

for week in month_matrix:
    week_columns = st.columns(7)
    for day_index, day in enumerate(week):
        with week_columns[day_index]:
            if day == 0:
                st.markdown("<div style='height:48px;'></div>", unsafe_allow_html=True)
                continue

            selected_date = datetime(
                st.session_state.calendar_year,
                st.session_state.calendar_month,
                day,
            ).date()
            is_selected = selected_date == st.session_state.selected_calendar_date
            memo_count = memo_date_counts.get(selected_date.strftime("%Y-%m-%d"), 0)
            button_label = f"{day}" if memo_count == 0 else f"{day} • {memo_count}"
            button_type = "primary" if is_selected else "secondary"

            if st.button(button_label, key=f"calendar_{selected_date.isoformat()}", use_container_width=True, type=button_type):
                st.session_state.selected_calendar_date = selected_date
                st.rerun()

st.caption(f"選択中の日付: {st.session_state.selected_calendar_date.strftime('%Y-%m-%d')}")

with st.form("memo_form", clear_on_submit=True):
    memo_title = st.text_input("メモのタイトル", placeholder="例: 今週の気づき")
    memo_body = st.text_area("メモの内容", placeholder="例: 配当利回りを先に確認する")
    submitted = st.form_submit_button("メモを保存")

    if submitted:
        if memo_title.strip() or memo_body.strip():
            st.session_state.memos.insert(
                0,
                {
                    "memo_id": uuid.uuid4().hex,
                    "title": memo_title.strip() or "タイトルなし",
                    "body": memo_body.strip(),
                    "memo_date": st.session_state.selected_calendar_date.strftime("%Y-%m-%d"),
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
            )
            st.toast("メモを保存したぜ！")
            st.rerun()
        else:
            st.warning("タイトルか内容のどちらかは入れてくれ！")

if not st.session_state.memos:
    st.info("まだメモはないぜ。診断の気づきや気になる銘柄を書いてみよう。")
else:
    filtered_memos = [
        memo for memo in st.session_state.memos
        if memo.get("memo_date", memo["created_at"][:10]) == st.session_state.selected_calendar_date.strftime("%Y-%m-%d")
    ]

    st.markdown(f"#### {st.session_state.selected_calendar_date.strftime('%Y-%m-%d')} のメモ")

    if not filtered_memos:
        st.info("この日付のメモはまだないぜ。")
    else:
        for memo in filtered_memos:
            memo_key = memo.get("memo_id", memo["created_at"])
            with st.container(border=True):
                col_left, col_right = st.columns([4, 1])
                with col_left:
                    st.markdown(f"**{memo['title']}**")
                    if memo["body"]:
                        st.write(memo["body"])
                    st.caption(f"メモ日: {memo.get('memo_date', memo['created_at'][:10])}")
                    st.caption(memo["created_at"])
                with col_right:
                    if st.button("削除", key=f"delete_memo_{memo_key}"):
                        st.session_state.memos = [item for item in st.session_state.memos if item.get("memo_id") != memo_key]
                        st.rerun()