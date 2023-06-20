import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")

st.subheader('부상 위험 감지 투수 명단')

col201, col202, col203, col204, col205, col206 = st.columns([0.3, 0.1, 0.3, 0.1, 0.3, 0.1])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
    st.markdown("#### 강효종")
    st.markdown(
    """
    팔꿈치
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
        .markdown-text-container {margin-bottom: 0px;}
        .stImage >div {
            margin-top: -10px;
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(70)
    st.markdown(
    """
    어깨
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(30)
    st.markdown(
    """
    손목
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(20)

with col203:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
    st.markdown("#### 강효종")
    st.markdown(
    """
    팔꿈치
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
        .markdown-text-container {margin-bottom: 0px;}
        .stImage >div {
            margin-top: -10px;
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(50)
    st.markdown(
    """
    어깨
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(70)
    st.markdown(
    """
    손목
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(20)
with col205:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
    st.markdown("#### 강효종")
    st.markdown(
    """
    팔꿈치
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
        .markdown-text-container {margin-bottom: 0px;}
        .stImage >div {
            margin-top: -10px;
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(60)
    st.markdown(
    """
    어깨
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(80)
    st.markdown(
    """
    손목
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }
    </style>""",
    unsafe_allow_html=True,
    )
    progress = st.progress(45)



st.subheader('부상자 명단')

col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.markdown("#### 강효종")
    st.text("투수")
with col203:
    st.text("왼쪽 어깨")
    st.text("복귀일 D-7")

col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.markdown("#### 고우석")
    st.text("투수")
with col203:
    st.text("왼쪽 어깨")
    st.text("복귀일 D-7")

col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.markdown("#### 김윤식")
    st.text("투수")
with col203:
    st.text("오른쪽 팔꿈치")
    st.text("복귀일 D-10")


