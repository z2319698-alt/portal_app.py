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

    /* 針對 st.link_button 的樣式強化 */
    div.stLinkButton > a {
        width: 100% !important;
        height: 420px !important; 
        border-radius: 35px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20) !important;
        color: white !important;
        border: 2px solid #30363d !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.4) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-decoration: none !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* 懸停效果：亮綠色外框 */
    div.stLinkButton > a:hover {
        border-color: #2ECC71 !important;
        color: #2ECC71 !important;
        transform: scale(1.05) !important;
        box-shadow: 0px 20px 50px rgba(46, 204, 113, 0.25) !important;
    }

    /* 讓內容換行並放大 */
    div.stLinkButton p {
        font-size: 38px !important;
        font-weight: bold !important;
        text-align: center !important;
        line-height: 1.5 !important;
        white-space: pre-wrap !important;
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
    # 使用 link_button 確保 100% 成功跳轉
    st.link_button("🌊\n自動化監測系統\n(數據監測)", 
                   "https://dafeng-water-monitor.streamlit.app/")

with col2:
    st.link_button("📜\n許可證辦理系統\n(證照管理)", 
                   "https://dafeng-permits.streamlit.app/")

with col3:
    st.link_button("📝\n危害告知表單\n(風險控管)", 
                   "https://dafeng-hazard-form.streamlit.app/")

# 底部版權
st.markdown("<br><br><p style='text-align: center; color: #8b949e; font-size: 20px;'>© 2026 大豐環保數據整合中心 | 系統運行正常</p>", unsafe_allow_html=True)
