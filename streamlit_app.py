import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="大豐環保管理總系統", layout="wide", initial_sidebar_state="collapsed")

# --- 高質感大豐環保門戶 CSS ---
st.markdown("""
    <style>
    /* 深色背景 */
    .stApp { background-color: #0E1117; }
    
    /* 總標題文字放大 */
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-size: 64px !important;
        font-weight: 800;
        margin-bottom: 70px;
        padding-top: 40px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
        letter-spacing: 2px;
    }

    /* 大型卡片按鈕樣式：寬度全滿、字體與按鈕同寬感 */
    .stButton > button {
        width: 100% !important;
        height: 350px !important; /* 加高按鈕讓視覺更震撼 */
        border-radius: 30px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20);
        color: white !important;
        font-size: 38px !important; /* 字體再加大 */
        font-weight: bold !important;
        border: 2px solid #30363d !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        white-space: pre-wrap; /* 允許文字換行 */
        line-height: 1.4;
    }

    /* 懸停效果：亮綠色外框 */
    .stButton > button:hover {
        border-color: #2ECC71 !important;
        color: #2ECC71 !important;
        transform: scale(1.03);
        box-shadow: 0px 15px 45px rgba(46, 204, 113, 0.2);
    }
    
    /* 隱藏側邊欄與頁尾 */
    [data-testid="stSidebar"] { display: none; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 品牌標題
st.markdown('<p class="main-title">🏢 大豐環保自動化管理平台</p>', unsafe_allow_html=True)

# 建立三欄佈局
col1, col2, col3 = st.columns(3, gap="large")

# 修正字串寫法，確保不會噴 SyntaxError
with col1:
    if st.button("🌊\n\n自動化監測系統\n(數據監測)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-water-monitor.streamlit.app/">', unsafe_allow_html=True)

with col2:
    if st.button("📜\n\n許可證辦理系統\n(證照管理)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-permits.streamlit.app/">', unsafe_allow_html=True)

with col3:
    if st.button("📝\n\n危害告知表單\n(風險控管)"):
        st.write('<meta http-equiv="refresh" content="0;url=https://dafeng-hazard-form.streamlit.app/">', unsafe_allow_html=True)

# 底部版權宣告
st.markdown("<br><br><p style='text-align: center; color: #8b949e; font-size: 20px;'>© 2026 大豐環保數據整合中心 | 系統運行正常</p>", unsafe_allow_html=True)
