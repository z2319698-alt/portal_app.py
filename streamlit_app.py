import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="大豐環保管理總系統", layout="wide", initial_sidebar_state="collapsed")

# --- 大豐環保門戶視覺強化 CSS ---
st.markdown("""
    <style>
    /* 深色背景 */
    .stApp { background-color: #0E1117; }
    
    /* 總標題 */
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-size: 64px !important;
        font-weight: 800;
        margin-bottom: 70px;
        padding-top: 40px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
    }

    /* 強化版卡片按鈕：圖示與文字同寬感 */
    .stButton > button {
        width: 100% !important;
        height: 420px !important; /* 加高按鈕空間 */
        border-radius: 35px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20);
        color: white !important;
        border: 2px solid #30363d !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        
        /* 核心關鍵：放大內容佈局 */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        white-space: pre-wrap;
        line-height: 1.2;
    }

    /* 針對按鈕內文字與圖示的精細調整 */
    .stButton > button p {
        font-size: 38px !important; /* 下方文字大小 */
        font-weight: bold !important;
    }

    /* 讓圖示 (Emoji) 變得超級大，跟文字同寬 */
    .stButton > button::first-line {
        font-size: 100px !important; /* 調整圖示大小至 100px */
        line-height: 1.8;
    }

    /* 懸停效果：大豐綠 */
    .stButton > button:hover {
        border-color: #2ECC71 !important;
        color: #2ECC71 !important;
        transform: scale(1.05);
        box-shadow: 0px 20px 50px rgba(46, 204, 113, 0.25);
    }
    
    /* 隱藏側邊欄 */
    [data-testid="stSidebar"] { display: none; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 品牌標題
st.markdown('<p class="main-title">🏢 大豐環保自動化管理平台</p>', unsafe_allow_html=True)

# 建立三欄式大型佈局
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    # 這裡的 Emoji 會被 CSS 抓取並放大
    if st.button("🌊\n自動化監測系統\n(數據監測)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-water-monitor.streamlit.app/">', unsafe_allow_html=True)

with col2:
    if st.button("📜\n許可證辦理系統\n(證照管理)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-permits.streamlit.app/">', unsafe_allow_html=True)

with col3:
    if st.button("📝\n危害告知表單\n(風險控管)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-hazard-form.streamlit.app/">', unsafe_allow_html=True)

# 底部版權
st.markdown("<br><br><p style='text-align: center; color: #8b949e; font-size: 20px;'>© 2026 大豐環保數據整合中心 | 系統運行正常</p>", unsafe_allow_html=True)
