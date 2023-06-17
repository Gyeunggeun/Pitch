import streamlit as st


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

def 팀():
    st.title('팀 요약')
    # 팀 페이지의 내용 추가

def 선수():
    st.title('투수 목록')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/6a00464c37f059ac3b52898fabd77bad8e7b36f3/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png'
        

def 설정():
    st.title('설정')
    # 설정 페이지의 내용 추가
     


page_names_to_funcs = {'홈': 홈페이지, '팀': 팀, '선수': 선수, '설정': 설정}

selected_page = st.sidebar.selectbox('페이지를 선택하세요',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()