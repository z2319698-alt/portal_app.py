import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="大豐環保管理總系統", layout="wide", initial_sidebar_state="collapsed")

# --- CSS 樣式：確保按鈕超大、圖示超大 ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .main-title {
        color: #FFFFFF; text-align: center; font-size: 64px !important;
        font-weight: 800; margin-bottom: 50px; padding-top: 40px;
    }
    /* 按鈕樣式優化 */
    .stButton > button {
        width: 100% !important; height: 350px !important;
        border-radius: 35px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20) !important;
        color: white !important; border: 2px solid #30363d !important;
        font-size: 38px !important; font-weight: bold !important;
        white-space: pre-wrap !important; line-height: 1.4 !important;
        transition: all 0.4s ease !important;
    }
    .stButton > button:hover {
        border-color: #2ECC71 !important; color: #2ECC71 !important;
        transform: scale(1.05) !important;
    }
    /* 隱藏預設元件 */
    [data-testid="stSidebar"] { display: none; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. 狀態管理：記錄目前要看哪一個系統
if 'active_system' not in st.session_state:
    st.session_state.active_system = None

st.markdown('<p class="main-title">🏢 大豐環保自動化管理平台</p>', unsafe_allow_html=True)

# --- 第一層：三大入口按鈕 ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("🌊\n自動化監測系統\n(數據監測)"):
        st.session_state.active_system = "monitor"

with col2:
    if st.button("📜\n許可證辦理系統\n(證照管理)"):
        st.session_state.active_system = "permits"

with col3:
    if st.button("📝\n危害告知表單\n(風險控管)"):
        st.session_state.active_system = "hazard"

st.markdown("---")

# --- 第二層：根據點擊內容，原地顯示內容 (不用跳分頁) ---
if st.session_state.active_system == "monitor":
    st.subheader("📊 數據監測系統載入中...")
    # 這裡使用 iframe 嵌入您原本的監測 App 網址
    st.components.v1.iframe("https://dafeng-water-monitor.streamlit.app/?embed=true", height=1200, scrolling=True)

elif st.session_state.active_system == "permits":
    st.subheader("📜 許可證辦理系統載入中...")
    st.components.v1.iframe("https://dafeng-permits.streamlit.app/?embed=true", height=1200, scrolling=True)

elif st.session_state.active_system == "hazard":
    st.subheader("📝 危害告知表單載入中...")
    st.components.v1.iframe("https://dafeng-hazard-form.streamlit.app/?embed=true", height=1200, scrolling=True)

else:
    st.info("💡 請點擊上方按鈕進入對應系統")

# 底部版權
st.markdown("<br><p style='text-align: center; color: #8b949e;'>© 2026 大豐環保數據整合中心</p>", unsafe_allow_html=True)
