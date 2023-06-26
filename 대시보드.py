import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcl
import matplotlib.patches as mpt
import hydralit_components as hc
import seaborn as sns
import plotly.express as px
from streamlit_echarts import st_echarts
from streamlit_extras.switch_page_button import switch_page
from streamlit_faker import get_streamlit_faker
from streamlit_card import card
import validators, base64
from pathlib import Path
from pandas.io.formats.style import Styler
import plotly.graph_objects as go


# 로고 코드
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


# streamlit faker
fake = get_streamlit_faker(seed=42)

# 현재부상투수현황 데이터프레임
# 재활, 부상, 가능 나열하기 위한 리스트
injury = ['가능','재활','부상']
now_injured = pd.read_csv('now_injured.csv', encoding='euc-kr')

# 부상 선수 중 부상 위험도 데이터프레임
high = pd.read_csv('high.csv', encoding='euc-kr')


# injured_list.csv 파일
Injured_List = pd.read_csv('Injured_List.csv')

# injured_list3.csv 파일
Injured_List3 = pd.read_csv('players/Injured_List3.csv')
Injured_List3 = Injured_List3.groupby(['부상명'])['선수'].count().rename('빈도')
Injured_List3 = Injured_List3.sort_values(ascending=False)


# -------------------- ▼ 필요 변수 생성 코딩 Start ▼ --------------------

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="AI 부상 방지 솔루션",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded")

# add_logo("https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/_%EC%86%94%EB%A3%A8%EC%85%98%EB%A1%9C%EA%B3%A0/%EA%B8%B0%EB%B3%B8_%ED%9A%8C%EC%83%89%EC%A1%B01.png", height=250)
add_logo("https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/_%EC%86%94%EB%A3%A8%EC%85%98%EB%A1%9C%EA%B3%A0/%EB%A1%9C%EA%B3%A0%EC%B5%9C%EC%A2%85.png", height=250)

# -------------------- ▲ 필요 변수 생성 코딩 End ▲ --------------------

# -------------------- ▼ Streamlit 웹 화면 구성 START ▼ --------------------

# st.title('대시보드')
# # 대시보드 페이지의 내용 추가
# want_to_contribute = st.button("팀 화면으로 이동")
# if want_to_contribute:
#     switch_page("팀")

# want_to_contribute1 = st.button("투수 화면으로 이동")
# if want_to_contribute1:
#     switch_page("투수")



## -------------------- ▼ 경기일정 START ▼ --------------------

st.title('대시보드')

st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)


st.subheader("경기 일정 📅")
st.write('기준: 2023년 06월 21일 (수)')

#can apply customisation to almost all the properties of the card, including the progress bar
                              

theme_away = {'bgcolor': '#f6f6f6','title_color': '#8e8e8d','content_color': '#8e8e8d','icon_color': 'red', 'icon': 'fas fa-sign-in'}
theme_home = {'bgcolor': '#ededed','title_color': '#be0737','content_color': '#be0737','icon_color': 'orange', 'icon': 'fa fa-sign-out'}

cc = st.columns(4)

with cc[0]:
    # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
    hc.info_card(title='NC', content='06.22. (목) 18:30 away 창원', theme_override=theme_away)


with cc[1]:
    hc.info_card(title='롯데', content='06.23. (금) 18:30 home 잠실',theme_override=theme_home)

with cc[2]:
    hc.info_card(title='롯데', content='06.24. (토) 17:00 home 잠실',theme_override=theme_home)

with cc[3]:
 #customise the the theming for a neutral content
    hc.info_card(title='롯데',content='06.25. (일) 17:00 home 잠실',key='sec',theme_override=theme_home)
    
st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)


    
# -------------------- ▲ 경기일정 End ▲ --------------------

## -------------------- ▼ 요약 START ▼ --------------------


st.subheader("부상 통계 📊")
col201, col202, col203, col204 = st.columns(4)
with col201:
    st.write(" ")
    st.write(" ")
    st.markdown("<h3 style='font-size: 1rem;'>1. 시즌 부상횟수</h3>", unsafe_allow_html=True)
    col201.metric("", "7 회", "2 회")


with col202:
    st.write(" ")
    st.write(" ")
    st.markdown("<h3 style='font-size: 1rem;'>2. 시즌 누적부상일수</h3>", unsafe_allow_html=True)
    col202.metric('',"115 일", "20일")
    #col202.metric('2. 시즌 누적부상일수', "115 일", ' 20일')

with col203:
    custom_order = ['부상', '재활', '가능']

    fig = px.pie(now_injured, values="값", names="출전여부", title="3. 투수 부상 현황", hole=.7, color = '출전여부', color_discrete_map={'부상':'#df839b', '재활':'#8e8e8d', '가능':'#f6f6f6'}, category_orders={"출전여부": custom_order})

    #fig.update_traces(now_injured.sort_values(by="출전여부", key=leg)
    fig.update_traces(textposition='outside', textinfo='label+value',
                          textfont_size=10) # textfont_color="blact"
    fig.update_layout(font=dict(size=16))
    fig.update_layout(width=250,height=300)
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig)

with col204:
    # 현재 팀 투수 부상 누적일수
    custom_order1 = ['고위험', '보통']
    
    fig2 = px.pie(high, values="값", names = "부상위험", title="4. 부상 고위험 투수 현황", hole=.7, color = '부상위험', color_discrete_map={'고위험':'#BE0737', '보통':'#ededed'},category_orders={"부상위험": custom_order1})

    fig2.update_traces(textposition='outside', textinfo='label+value', textfont_size=10)
    fig2.update_layout(font=dict(size=16))
    fig2.update_layout(width=250,height=300)
    fig2.update(layout_showlegend=False)
    st.plotly_chart(fig2)
    
st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)

# --------------------- ▲ 요약 End ▲ --------------------

## -------------------- ▼ 부상통계 START ▼ --------------------


st.subheader("부상 종류 👨‍⚕️")
col21, col22, col23 = st.columns([0.9, 0.1, 1.0]) # st.columns([0.1, 0.3, 0.1, 0.3])

# 팀부상종류 통계
with col21:
    st.markdown('<h2 style="font-size: 1.25rem;"> 1. 2023 시즌 부상 종류</h2>', unsafe_allow_html=True)
    col211,col212, col213 = st.columns([0.05, 1, 0.3])
    with col212:
        # 데이터 읽기
        in3 = pd.read_csv('Injured_List3.csv', encoding='euc-kr')

        # 부상명에 대한 빈도를 계산하고 내림차순으로 정렬
        counts = in3['부상명'].value_counts(sort=True, ascending=False)

        fig = go.Figure()

        # 바 차트 생성
        fig.add_trace(go.Bar(x=counts.values, y=counts.index, orientation='h',
                             marker=dict(color='rgba(0, 200, 0, 0.95)', line=dict(color='rgba(0, 200, 0, 0.95)', width=1)),  # 색상 변경
                             hoverinfo='y',
                             opacity=0.6,
                             showlegend=False
                            )
                      )

        # 롤리팝 차트에 원형 마커 추가
        fig.add_trace(go.Scatter(mode='markers', 
                                 y=counts.index, x=counts.values, 
                                 marker=dict(color='rgba(0, 200, 0, 0.95)', size=15),  # 색상 변경
                                 hoverinfo='skip',
                                 showlegend=False
                                )
                     )

        fig.update_layout(title_text='부상 종류별 부상 횟수',
                          xaxis=dict(showgrid=False, showline=False, showticklabels=True),
                          yaxis=dict(zeroline=False, gridcolor='white',
                                     showgrid=False,
                                     tickmode='array', 
                                     tickvals=in3['부상명'], 
                                     ticktext=in3['부상명'],
                                     tickfont=dict(size=17) 
                                     ),
                          bargap=1
                         )


        # 차트 크기 조정 및 출력
        st.plotly_chart(fig, use_container_width=True)

    
# 팀부상선수 한명씩 나열    
with col23:
    st.markdown('<h2 style="font-size: 1.25rem;"> 2. 최근 부상자</h2>', unsafe_allow_html=True)
    col231, col232, col233, col234, col235= st.columns([0.4, 0.05, 0.4, 0.05, 0.4])
    
    # 선수 1
    with col231:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png'
        image_width = 200
        injured_date = Injured_List['날짜'][66]
        text = '''
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="{image_url}" width="{image_width}">
        <h3 style="margin-top: 15px; font-size: 1rem;">이정용</h3>
        <p style="margin-top: 15px; font-size: 0.9rem; text-align: left;">
        부상 부위: Shoulder<br>
        부상 발생일: {injured_date}<br>
        예상 복귀일: D-10
        </p>
        </div>
        '''
        st.markdown(text.format(image_url=image_url, image_width=image_width, injured_date=injured_date), unsafe_allow_html=True)
       
        
        
# 선수 2   
    with col233:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png'
        image_width = 200
        injured_date = Injured_List['날짜'][64]
        text = '''
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="{image_url}" width="{image_width}">
        <h3 style="margin-top: 15px; font-size: 1rem;">고우석</h3>
        <p style="margin-top: 15px; font-size: 0.9rem; text-align: left;">
        부상 부위: Shoulder<br>
        부상 발생일: {injured_date}<br>
        예상 복귀일: D-7
        </p>
        </div>
        '''
        st.markdown(text.format(image_url=image_url, image_width=image_width, injured_date=injured_date), unsafe_allow_html=True)
    

# 선수 3 
    with col235:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png'
        image_width = 200
        injured_date = Injured_List['날짜'][59]
        text = '''
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="{image_url}" width="{image_width}">
        <h3 style="margin-top: 15px; font-size: 1rem;">이민호</h3>
        <p style="margin-top: 15px; font-size: 0.9rem; text-align: left;">
        부상 부위: Oblique<br>
        부상 발생일: {injured_date}<br>
        예상 복귀일: D-3
        </p>
        </div>
        '''
        st.markdown(text.format(image_url=image_url, image_width=image_width, injured_date=injured_date), unsafe_allow_html=True)
           
    
   
