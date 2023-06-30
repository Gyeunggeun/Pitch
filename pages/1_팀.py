import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prettytable import PrettyTable
import streamlit.components.v1 as components
from packages.card import custom_metric_card, style_metric_cards
from packages.logo import add_logo

df = pd.read_csv('./players/Injured_List4.csv', encoding='euc-kr')
df = df.set_index('선수')

st.set_page_config(
    page_title="팀 요약",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded")
add_logo("https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/solutionlogo/final.png", height=370)

st.title('팀')

st.markdown("""
            <style>
                  hr {
                    height: 3px; 
                    background-color: white; 
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
    custom_metric_card(label="팔꿈치", value="Low", delta="감소", label_color="#7D7D7D", text_color="#008000", delta_color="#008000")
    custom_metric_card(label="어깨", value="High", delta="증가", label_color="#7D7D7D", text_color="#D80027", delta_color="#D80027")
    custom_metric_card(label="손목", value="High", delta="변화 없음", label_color="#7D7D7D", text_color="#D80027", delta_color="#000000")

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
    custom_metric_card(label="팔꿈치", value="Low", delta="변화 없음", label_color="#7D7D7D", text_color="#008000", delta_color="#000000")
    custom_metric_card(label="어깨", value="Low", delta="감소", label_color="#7D7D7D", text_color="#D80027", delta_color="#008000")
    custom_metric_card(label="손목", value="High", delta="증가", label_color="#7D7D7D", text_color="#D80027", delta_color="#D80027")
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
    custom_metric_card(label="팔꿈치", value="Low", delta="변화 없음", label_color="#7D7D7D", text_color="#008000", delta_color="#000000")
    custom_metric_card(label="어깨", value="High", delta="증가", label_color="#7D7D7D", text_color="#D80027", delta_color="#D80027")
    custom_metric_card(label="손목", value="Low", delta="변화 없음", label_color="#7D7D7D", text_color="#008000", delta_color="#000000")




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
        .myTable .cell {
        height: 30px;
        width: 300px;
        background-color: #6A89BD;
        color: white;   
        }
        .myTable .cell:first-child {
            height: 30px;
            width: 300px;
            background-color: #3F5270;
            color: white;
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
    table = PrettyTable()
    table.field_names = ["이름", "고우석"]

    # 데이터프레임에서 마지막 행을 선택합니다.
    row = df.iloc[-5]

    # 테이블에 각 열 이름과 값을 추가합니다.
    for key, value in row.items():
        table.add_row([key, value])

    # HTML 테이블을 생성하고 각 셀에 고유한 클래스를 부여합니다.
    html_code = table.get_html_string(attributes={"class": "myTable"})
    html_code = html_code.replace("<th>", "<th class='header'>").replace("<td>", "<td class='cell'>")

    # 예상된 CSS 코드
    css_code = """
    <style>
        .myTable .cell {
        height: 30px;
        width: 300px;
        background-color: #6A89BD;
        color: white;   
        }
        .myTable .cell:first-child {
            height: 30px;
            width: 300px;
            background-color: #3F5270;
            color: white;
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
            <img src='https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png' width='200' />
            <h4 style='margin-top: -5px; margin-bottom: 0;'>이민호</h4>
            <h6 style='color: gray; margin-top: -10px;'>LEE MIN HO</h6>
        </div>
    """, unsafe_allow_html=True)

with col203:
    table = PrettyTable()
    table.field_names = ["이름", "이민호"]

    # 데이터프레임에서 마지막 행을 선택합니다.
    row = df.iloc[-6]

    # 테이블에 각 열 이름과 값을 추가합니다.
    for key, value in row.items():
        table.add_row([key, value])

    # HTML 테이블을 생성하고 각 셀에 고유한 클래스를 부여합니다.
    html_code = table.get_html_string(attributes={"class": "myTable"})
    html_code = html_code.replace("<th>", "<th class='header'>").replace("<td>", "<td class='cell'>")

    # 예상된 CSS 코드
    css_code = """
    <style>
        .myTable .cell {
        height: 30px;
        width: 300px;
        background-color: #6A89BD;
        color: white;   
        }
        .myTable .cell:first-child {
            height: 30px;
            width: 300px;
            background-color: #3F5270;
            color: white;
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