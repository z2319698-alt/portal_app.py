import streamlit as st

# 1. 網頁基本設定：隱藏側邊欄，讓視覺集中在中央按鈕
st.set_page_config(page_title="全興廠管理總系統", layout="wide", initial_sidebar_state="collapsed")

# --- 高質感門戶 CSS ---
st.markdown("""
    <style>
    /* 深色背景 */
    .stApp { background-color: #0E1117; }
    
    /* 總標題文字放大 */
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-size: 56px !important;
        font-weight: 800;
        margin-bottom: 60px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* 大型卡片按鈕樣式 */
    .stButton > button {
        width: 100%;
        height: 280px !important; /* 超大按鈕 */
        border-radius: 25px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20);
        color: white !important;
        font-size: 32px !important; /* 標題文字大 */
        font-weight: bold !important;
        border: 2px solid #30363d !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* 懸停效果：亮藍色外框與浮起感 */
    .stButton > button:hover {
        border-color: #58a6ff !important;
        color: #58a6ff !important;
        transform: scale(1.05);
        box-shadow: 0px 20px 40px rgba(88, 166, 255, 0.15);
    }
    
    /* 隱藏預設元件 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🏢 全興廠自動化管理平台</p>', unsafe_allow_html=True)

# 建立三欄式大型佈局
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("🌊\n\n自動化監測系統\n(廢水 / 統計)"):
        # 跳轉至您的監測系統
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-water-monitor.streamlit.app/">', unsafe_allow_html=True)

with col2:
    if st.button("📜\n\n許可證辦理系統\n(證照管理)"):
        # 跳轉至您的許可證系統
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-permits.streamlit.app/">', unsafe_allow_html=True)

with col3:
    if st.button("📝\n\n危害告知表單\n(風險控管)"):
        # 跳轉至您的危害告知系統
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-hazard-form.streamlit.app/">', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #8b949e; font-size: 18px;'>© 2026 全興廠數據整合中心 | 系統運行正常</p>", unsafe_allow_html=True)
