import streamlit as st
import streamlit.components.v1 as components
from streamlit_card import card
import pandas as pd
from streamlit_extras.app_logo import add_logo


df = pd.read_csv('./players/Injured_List4.csv', encoding='UTF-8')
df = df.set_index('선수')

st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")
add_logo("body/LGtwins.png", height=250)

st.title('팀')

st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)

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
                background-image: linear-gradient(to right, yellow, #C10505, #15FF0D);
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




st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)
st.subheader('부상자 명단')
st.write("\n")  # additional space

col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>이정용</h4>
            <h6 style='color: gray; margin-top: -10px;'>YI JUNG YONG</h6>
        </div>
    """, unsafe_allow_html=True)
# with col202:
#     st.markdown("""<br>
#         <div style="text-align: center;">
#             <h3 style="margin-top: 15px;">이정용</h3>
#             <h4 style="margin-top: -15px;">투수</h4>
#         </div>
#     """, unsafe_allow_html=True)

with col203:
    st.table(df.iloc[-1])
    # st.markdown(" ")
    # st.markdown(" ")
    # st.text("어깨")
    # st.text("2023-05-30")
    # st.text("예상 복귀일 D-7")


col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>고우석</h4>
            <h6 style='color: gray; margin-top: -10px;'>GO WOO SUK</h6>
        </div>
    """, unsafe_allow_html=True)

# with col202:
#     st.markdown("""<br>
#         <div style="text-align: center;">
#             <h3 style="margin-top: 15px;">고우석</h3>
#             <h4 style="margin-top: -15px;">투수</h4>
#         </div>
#     """, unsafe_allow_html=True)

with col203:
    st.table(df.iloc[-5])
    # st.markdown(" ")
    # st.markdown(" ")
    # st.text("어깨")
    # st.text("2023-05-02")
    # st.text("예상 복귀일 D-3")

col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>이민호</h4>
            <h6 style='color: gray; margin-top: -10px;'>LEE MIN HO</h6>
        </div>
    """, unsafe_allow_html=True)
# with col202:
#     st.markdown("""
#         <div style="text-align: center;">
#             <h3 style="margin-top: 15px;">이민호</h3>
#             <h4 style="margin-top: -15px;">투수</h4>
#         </div>
#     """, unsafe_allow_html=True)
with col203:
    st.table(df.iloc[-6])
    # st.markdown(" ")
    # st.markdown(" ")
    # st.text("팔꿈치")
    # st.text("2023-04-10")
    # st.text("예상 복귀일 D-1")

