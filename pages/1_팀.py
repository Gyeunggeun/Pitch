import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")

st.subheader('부상 위험 감지 투수 명단')

col201, col202, col203 = st.columns(3)
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.text("강효종")
    st.text("투수")
with col203:
    st.text("오른쪽 어깨")
    st.text("복귀일 D-3")

col211, col212, col213 = st.columns(3)
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.text("강효종")
    st.text("투수")
with col203:
    st.text("오른쪽 어깨")
    st.text("복귀일 D-3")
        


st.subheader('부상자 명단')

col201, col202, col203 = st.columns(3)
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.text("강효종")
    st.text("투수")
with col203:
    st.text("오른쪽 어깨  D-3")

col201, col202, col203 = st.columns(3)
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.text("고우석")
    st.text("투수")
with col203:
    st.text("왼쪽 어깨")
    st.text("복귀일 D-7")

col201, col202, col203 = st.columns(3)
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=100)
with col202:
    st.text("김윤식")
    st.text("투수")
with col203:
    st.text("오른쪽 팔꿈치")
    st.text("복귀일 D-10")


