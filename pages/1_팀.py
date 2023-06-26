import streamlit as st
import streamlit.components.v1 as components
from streamlit_card import card
import pandas as pd
import validators, base64
from pathlib import Path
import plotly.graph_objects as go
from prettytable import PrettyTable
import streamlit.components.v1 as components

def add_logo(logo_url: str, height: int = 120):
    if validators.url(logo_url) is True:
        logo = f"url({logo_url})"
    else:
        logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: {logo};
                background-repeat: no-repeat;
                padding-top: {height - 100}px;
                background-position: -100px -150px;
        </style>
        """,
        unsafe_allow_html=True,
    )

df = pd.read_csv('./players/Injured_List4.csv', encoding='UTF-8')
df = df.set_index('선수')

st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")
add_logo("https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/_%EC%86%94%EB%A3%A8%EC%85%98%EB%A1%9C%EA%B3%A0/%EB%A1%9C%EA%B3%A0%EC%B5%9C%EC%A2%85.png", height=250)

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
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%B1%EC%8A%B9%ED%98%84.png' width='200' style='display: block; margin: auto;'/>
            <h3>백승현</h3>
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
    st.markdown('##### ⚠️ 부위별 위험도')
    st.markdown("팔꿈치")
    progress = st.progress(70)
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=70,
        title={'text': "안전도"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 30], 'color': 'red'},
                {'range': [30, 70], 'color': 'orange'},
                {'range': [70, 100], 'color': 'green'}]}))
    
    st.plotly_chart(fig)
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
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%9C%A0%EC%98%81.png' width='200' style='display: block; margin: auto;'/>
            <h3>김유영</h3>
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
    st.markdown('##### ⚠️ 부위별 위험도')
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
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%BC%88%EB%A6%AC.png' width='200' style='display: block; margin: auto;'/>
            <h3>켈리</h3>
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
    st.markdown('##### ⚠️ 부위별 위험도')
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
st.write("\n")

col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>이정용</h4>
            <h6 style='color: gray; margin-top: -10px;'>YI JUNG YONG</h6>
        </div>
    """, unsafe_allow_html=True)

with col203:
    table = PrettyTable()
    table.field_names = ["이름", "이정용"]

    # 데이터프레임에서 마지막 행을 선택합니다.
    row = df.iloc[-1]

    # 테이블에 각 열 이름과 값을 추가합니다.
    for key, value in row.items():
        table.add_row([key, value])

    # HTML 테이블을 생성하고 각 셀에 고유한 클래스를 부여합니다.
    html_code = table.get_html_string(attributes={"class": "myTable"})
    html_code = html_code.replace("<th>", "<th class='header'>").replace("<td>", "<td class='cell'>")

    # 예상된 CSS 코드
    css_code = """
    <style>
        .myTable .cell:first-child {
            height: 30px;
            width: 300px;
            background-color: #ADD8E6;
        }
        .myTable .header {
            height: 30px;
            width: 300px;
            background-color: #808080; 
            color: white;
        }
    </style>
    """

    # CSS 코드를 HTML 테이블 코드 앞에 추가합니다.
    html_code = css_code + html_code
    components.html(html_code, height=200)


col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>고우석</h4>
            <h6 style='color: gray; margin-top: -10px;'>GO WOO SUK</h6>
        </div>
    """, unsafe_allow_html=True)


with col203:
    st.table(df.iloc[-5])

col201, col202, col203 = st.columns([0.25, 0.1, 0.6])
with col201:
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>이민호</h4>
            <h6 style='color: gray; margin-top: -10px;'>LEE MIN HO</h6>
        </div>
    """, unsafe_allow_html=True)

with col203:
    st.table(df.iloc[-6])