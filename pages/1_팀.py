import streamlit as st
import streamlit.components.v1 as components
from streamlit_card import card

st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")

st.subheader('부상 위험 감지 투수 명단')

col201, col202, col203, col204, col205, col206 = st.columns([0.3, 0.1, 0.3, 0.1, 0.3, 0.1])
with col201:
    st.markdown(
        """
        <div style="text-align: center">
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png' width='200' style='display: block; margin: auto;'/>
            <h3>강효종</h3>
        </div>
        <style>
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
            }
            .stMarkdown h4 {
                text-align: center;
                margin-bottom: 20px;
                margin-top: 10px;
            }
            .stMarkdown p {
                margin-bottom: 0px; 
            }
            .stImage > div {
                margin-top: -50px;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("팔꿈치")
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
    st.markdown(
        """
        <div style="text-align: center">
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png' width='200' style='display: block; margin: auto;'/>
            <h3>강효종</h3>
        </div>
        <style>
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
            }
            .stMarkdown h4 {
                text-align: center;
                margin-bottom: 20px;
                margin-top: 10px;
            }
            .stMarkdown p {
                margin-bottom: 0px; 
            }
            .stImage > div {
                margin-top: -50px;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("팔꿈치")
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
    st.markdown(
        """
        <div style="text-align: center">
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png' width='200' style='display: block; margin: auto;'/>
            <h3>강효종</h3>
        </div>
        <style>
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
            }
            .stMarkdown h4 {
                text-align: center;
                margin-bottom: 20px;
                margin-top: 10px;
            }
            .stMarkdown p {
                margin-bottom: 0px; 
            }
            .stImage > div {
                margin-top: -50px;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("팔꿈치")
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





st.subheader('부상자 명단')
st.write("\n")  # additional space

col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=200)
with col202:
    st.markdown("""
        <div style="text-align: center;">
            <h3 style="margin-top: 15px;">강효종</h3>
            <h4 style="margin-top: 5px;">투수</h4>
        </div>
    """, unsafe_allow_html=True)

with col203:
    st.markdown("""
        <style>
            p {
                font-size: 18px;
                margin-top: 10px;
            }
        </style>
        <div style="display: flex; justify-content: space-between;">
            <p>왼쪽 어꺠</p>
            <p>오른쪽 팔꿈치</p>
            <p>왼쪽 발목</p>
        </div>
        <div style="display: flex; justify-content: space-between;">
            <p>복귀일 D-7</p>
            <p>복귀일 D-10</p>
            <p>복귀일 D-14</p>
        </div>
    """, unsafe_allow_html=True)


col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=200)
with col202:
    st.markdown("""
        <div style="text-align: center;">
            <h3>고우석</h3>
            <h4 style="margin-top: 0px;">투수</h4>
        </div>
    """, unsafe_allow_html=True)
with col203:
    st.text("왼쪽 어깨")
    st.text("복귀일 D-7")

col201, col202, col203 = st.columns([0.1, 0.2, 0.7])
with col201:
    st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=200)
with col202:
    st.markdown("""
        <div style="text-align: center;">
            <h3>김윤식</h3>
            <h4 style="margin-top: 0px;">투수</h4>
        </div>
    """, unsafe_allow_html=True)
with col203:
    st.text("오른쪽 팔꿈치")
    st.text("복귀일 D-10")


