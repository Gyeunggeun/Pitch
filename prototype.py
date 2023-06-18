import streamlit as st
import streamlit.components.v1 as components

# -------------------- ▼ 필요 변수 생성 코딩 Start ▼ --------------------

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="AI 부상 방지 솔루션",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded")
# -------------------- ▲ 필요 변수 생성 코딩 End ▲ --------------------
# -------------------- ▼ Streamlit 웹 화면 구성 START ▼ --------------------


def 홈페이지():
    st.title('대시보드')
    # 대시보드 페이지의 내용 추가
