import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="大豐環保管理總系統", layout="wide", initial_sidebar_state="collapsed")

# --- 高質感大豐環保門戶 CSS ---
st.markdown("""
    <style>
    /* 深色背景 */
    .stApp { background-color: #0E1117; }
    
    /* 總標題文字放大與變更名稱 */
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-size: 64px !important; /* 加大標題 */
        font-weight: 800;
        margin-bottom: 70px;
        padding-top: 40px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
        letter-spacing: 2px;
    }

    /* 大型卡片按鈕樣式：寬度全滿、字體與按鈕同寬感 */
    .stButton > button {
        width: 100% !important;
        height: 320px !important; /* 再次加高按鈕 */
        border-radius: 30px !important;
        background: linear-gradient(145deg, #23272c, #1a1c20);
        color: white !important;
        font-size: 36px !important; /* 字體放大 */
        font-weight: bold !important;
        border: 2px solid #30363d !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        line-height: 1.5;
    }

    /* 懸停效果：亮綠色外框 (環保色系) */
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

# 品牌標題更新
st.markdown('<p class="main-title">🏢 大豐環保自動化管理平台</p>', unsafe_allow_html=True)

# 建立三欄式佈局，並增加間距
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    # 第一個按鈕名稱修正：(數據監測)
    if st.button("🌊\n\n
