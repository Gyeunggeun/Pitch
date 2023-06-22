import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcl
import matplotlib.patches as mpt
import seaborn as sns
import plotly.express as px
from streamlit_echarts import st_echarts
from streamlit_extras.switch_page_button import switch_page
from streamlit_faker import get_streamlit_faker

# streamlit faker
fake = get_streamlit_faker(seed=42)

# 현재부상투수현황 데이터프레임
now_injured = pd.read_csv('now_injured.csv', encoding='cp949')
# 부상x선수 중 부상 위험도 데이터프레임
high = pd.read_csv('high.csv', encoding='cp949')

# 부상자 csv 데이터프레임 !!
# injury = pd.read_csv('injury.csv')
# df1 = injury[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
# df1 = df1.set_index('선수ID')

# 경기일정 csv 데이터프레임 !!
# date

#일단 예시로 해당csv파일 활용
df = pd.read_csv('lgpitch.csv')
df1 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
df1 = df1.set_index('선수ID')

# -------------------- ▼ 필요 변수 생성 코딩 Start ▼ --------------------

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="AI 부상 방지 솔루션",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded")
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

## -------------------- ▼ 요약 START ▼ --------------------

st.title('대시보드')
st.subheader("경기일정")
st.write('2023년 06월 21일 (수)')

wch_colour_box = (142,142,141)
wch_colour_font = (0,0,0)
fontsize = 18
valign = "left"
iconname = "fas fa-asterisk"
sline = "NC"
place="away 창원"
lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
i = '06.22. (목) 18:30'

htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class=' fa-xs'></i> {i}
                        </style><BR><span style='font-size: 24px; 
                        margin-top: 0;'>{sline}</style></span>
                        </style><BR><span style='font-size: 18px; 
                        margin-top: 0;'>{place}</style></span></p>"""

wch_colour_box2 = (223,131,155)
sline2 = "롯데"
place2="home 잠실"
i2 = '06.23. (금) 18:30'
i3 = '06.24. (토) 17:00'
i4 = '06.25. (일) 17:00'

htmlstr2 = f"""<p style='background-color: rgb({wch_colour_box2[0]}, 
                                              {wch_colour_box2[1]}, 
                                              {wch_colour_box2[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class=' fa-xs'></i> {i2}
                        </style><BR><span style='font-size: 24px; 
                        margin-top: 0;'>{sline2}</style></span>
                        </style><BR><span style='font-size: 18px; 
                        margin-top: 0;'>{place2}</style></span></p>"""

htmlstr3 = f"""<p style='background-color: rgb({wch_colour_box2[0]}, 
                                              {wch_colour_box2[1]}, 
                                              {wch_colour_box2[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class=' fa-xs'></i> {i3}
                        </style><BR><span style='font-size: 24px; 
                        margin-top: 0;'>{sline2}</style></span>
                        </style><BR><span style='font-size: 18px; 
                        margin-top: 0;'>{place2}</style></span></p>"""

htmlstr4 = f"""<p style='background-color: rgb({wch_colour_box2[0]}, 
                                              {wch_colour_box2[1]}, 
                                              {wch_colour_box2[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class=' fa-xs'></i> {i4}
                        </style><BR><span style='font-size: 24px; 
                        margin-top: 0;'>{sline2}</style></span>
                        </style><BR><span style='font-size: 18px; 
                        margin-top: 0;'>{place2}</style></span></p>"""

col301, col302, col303, col304 = st.columns(4)
with col301:
    st.markdown(lnk + htmlstr, unsafe_allow_html=True)
with col302:
    st.markdown(lnk + htmlstr2, unsafe_allow_html=True)
with col303:
    st.markdown(lnk + htmlstr3, unsafe_allow_html=True)
with col304:
    st.markdown(lnk + htmlstr4, unsafe_allow_html=True)

st.subheader("요약")
col11, col12 = st.columns(2)
with col11:
    
    #st.write(f"시즌 총 부상빈도 : {df1['출장경기수'][0]} (임시)") # st.write('팀부상빈도:', injury[부상].sum)
    #st.write(f"시즌 총 누적부상일수 : {df1['이닝'][0]} (임시)")
    #fake.dataframe()
    #부상투수통계 도넛차트
    temp1 = 7
    temp2 = 115
    
    col111, col112 = st.columns(2)
    with col111:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col111.metric('시즌 총 부상빈도', temp1, '2 회')
        #현재 투수 부상 현황
        leg = ['불가능', '가능']
                
        
        #title="현재투수부상현황",        
        #now_injured.sort_values(by="출전여부", key=lambda s: s.map({k: i for i, k in enumerate(leg)}))
           
        
        
        # 반원 차트1
        # option = {
        #     "tooltip": {
        #         "formatter": '{a} <br/>{b} : {c}%'
        #     },
        #     "series": [{
        #         # "name": '进度',
        #         "type": 'gauge',
        #         "startAngle": 180,
        #         "endAngle": 0,
        #         "progress": {
        #             "show": "true"
        #         },
        #         "radius":'100%', 
    
        #         "itemStyle": {
        #             "color": '#58D9F9',
        #             "shadowColor": 'rgba(0,138,255,0.45)',
        #             "shadowBlur": 10,
        #             "shadowOffsetX": 2,
        #             "shadowOffsetY": 2,
        #             "radius": '55%',
        #         },
        #         "progress": {
        #             "show": "true",
        #             "roundCap": "true",
        #             "width": 15
        #         },
        #         "pointer": {
        #             "length": '60%',
        #             "width": 8,
        #             "offsetCenter": [0, '5%']
        #         },
        #         "detail": {
        #             "valueAnimation": "true",
        #             "formatter": '{value}%',
        #             "backgroundColor": '#58D9F9',
        #             "borderColor": '#999',
        #             "borderWidth": 4,
        #             "width": '60%',
        #             "lineHeight": 20,
        #             "height": 20,
        #             "borderRadius": 188,
        #             "offsetCenter": [0, '40%'],
        #             "valueAnimation": "true",
        #         },
        #         "data": [{
        #             "value": 66.66
        #         }]
        #     }]
        # };
        # st_echarts(options=option, key="1")

    #부상고위험투수통계 도넛차트
    
    with col112:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col112.metric('시즌 총 누적부상일수', temp2, ' 20일')
        

        
        # 반원 차트1
        # option1 = {
        #     "tooltip": {
        #         "formatter": '{a} <br/>{b} : {c}%'
        #     },
        #     "series": [{
        #         "type": 'gauge',
        #         "startAngle": 180,
        #         "endAngle": 0,
        #         "progress": {
        #             "show": "true"
        #         },
        #         "radius":'100%', 

        #             "itemStyle": {
        #             "color": '#58D9F9',
        #             "shadowColor": 'rgba(0,138,255,0.45)',
        #             "shadowBlur": 10,
        #             "shadowOffsetX": 2,
        #             "shadowOffsetY": 2,
        #             "radius": '55%',
        #         },
        #         "progress": {
        #             "show": "true",
        #             "roundCap": "true",
        #             "width": 15
        #         },
        #         "pointer": {
        #             "length": '60%',
        #             "width": 8,
        #             "offsetCenter": [0, '5%']
        #         },
        #         "detail": {
        #             "valueAnimation": "true",
        #             "formatter": '{value}%',
        #             "backgroundColor": '#58D9F9',
        #             "borderColor": '#999',
        #             "borderWidth": 4,
        #             "width": '60%',
        #             "lineHeight": 20,
        #             "height": 20,
        #             "borderRadius": 188,
        #             "offsetCenter": [0, '40%'],
        #             "valueAnimation": "true",
        #         },
        #         "data": [{
        #             "value": 66.66
        #         }]
        #     }]
        # };
        # st_echarts(options=option1, key="2")

# -------------------- ▲ 요약 End ▲ --------------------

## -------------------- ▼ 경기일정 START ▼ --------------------

with col12:


    
    col201, col202 = st.columns(2)
    with col201:
        fig = px.pie(now_injured, values="값", names="출전여부", title="현재투수부상현황", hole=.7, color = '출전여부', color_discrete_map={'부상':'#df839b', '재활':'#8e8e8d', '가능':'#f6f6f6'})
        #fig.update_traces(now_injured.sort_values(by="출전여부", key=leg)
        fig.update_traces(textposition='outside', textinfo='label+value',
                          textfont_size=10) # textfont_color="blact"
        fig.update_layout(font=dict(size=16))
        fig.update_layout(width=250,height=300)
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
    with col202:
                # 현재 팀 투수 부상 누적일수
        fig2 = px.pie(high, values="값", names = "부상위험", title="현재 부상 고위험 투수 통계", hole=.7, color = '부상위험', color_discrete_map={'고위험':'#BE0737', '보통':'#ededed'})
        fig2.update_traces(textposition='outside', textinfo='label+value', textfont_size=10)
        fig2.update_layout(font=dict(size=16))
        fig2.update_layout(width=250,height=300)
        fig2.update(layout_showlegend=False)
        st.plotly_chart(fig2)
    
    #st.dataframe(df)  # 경기일정 data프레임이 들어가야함

# --------------------- ▲ 경기일정 End ▲ --------------------

st.subheader("부상통계")
wch_colour_box = (0,204,102)
wch_colour_font = (0,0,0)
fontsize = 18
valign = "left"
iconname = "fas fa-asterisk"
sline = "Observations"
lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
i = 123

htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

st.markdown(lnk + htmlstr, unsafe_allow_html=True)


# # 선수 이미지 URL
# players = { 
#     '강효종': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/6a00464c37f059ac3b52898fabd77bad8e7b36f3/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png',
#     '함덕주': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%ED%95%A8%EB%8D%95%EC%A3%BC.png'
# }

# # 사이드바
# pages = ['선수 목록'] + list(players.keys())
# selected_page = st.sidebar.selectbox('페이지', pages)

# # 선수 목록 페이지 구성
# if selected_page == '선수 목록':
#     st.title('선수 목록')
#     player_list = list(players.keys())
#     for i in range(0, len(player_list), 5):  # 5*7 로 총 35명의 선수 이미지 표현
#         columns = st.columns(5)
#         for j in range(5):
#             if i + j < len(player_list):
#                 player = player_list[i + j]
#                 with columns[j]:
#                     image_url = players[player]
#                     components.html(f'''
#                         <center>
#                             <img src="{image_url}" width="100%">
#                             <p style="margin-top: 0px; color: white; font-size: 20px; font-weight: bold">{player}</p>
#                         </center>
#                     ''', height=200)
# else:
#     st.title(f'{selected_page}')
#     # 선수의 세부 페이지에서 보여줄 정보
#     if selected_page == '강효종':
#         tab1, tab2, tab3 = st.tabs(['선수 프로필', '부상분석', '부상위험요인'])
#         with tab1:
#             col301, col302 = st.columns(2)
#             with col301:
#                 st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=300)
#             with col302:
#                 st.subheader("선수 기본 프로필")
#                 st.text("이름: 강효종")
#                 st.text("포지션: 투수")
#                 st.text("팀: LG 트윈스")
#                 st.text("생년월일: 2002년 10월 14일")
#                 st.text("신장/체중: 184cm/86kg")
#             st.write('2023시즌') # 볼드체로
#             st.dataframe(df1, width=1000)
#             st.markdown("   ")
#             st.subheader("최근 부상 이력")
#             st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
#             col303, col304 = st.columns(2)
#             with col303 :
#                 #st.write('2023시즌')
#                 #st.markdown("   ")
#                 #st.subheader("최근 부상 이력")
#                 #st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
#                 st.image('0619/부상이력히트맵.png', width=500)
#             with col304:
#                 #st.markdown("    ") # 줄바꿈 여러번 추가
#                 st.image('0619/예측히트맵.png', width=500)

#         with tab2:
#             st.subheader('투구 분석')
#             # st.image('투구별 어깨,팔꿈치 부상위험도 차트 이미지 삽입')
#             option = st.selectbox('투구를 선택하세요',
#                          ['1구', '2구', '3구', '4구', '5구', '6구', '7구', '8구', '9구', '10구','11구', '12구', '13구', '14구', '15구', '16구', '17구', '18구', '19구', '20구'])
#             st.write('선택 옵션:', option)
#             if option == '1구':
#                 col401, col402 = st.columns(2)
#                 with col401:
#                     st.video('https://youtu.be/f-tq3W2HvT8') # 출처 필요 -> 세부 페이지에
#                 with col402:
#                     st.video('https://youtu.be/8s-ZllEX4Zk')
#             elif option == '2구':
#                 col403, col404 = st.columns(2)
#                 with col403:
#                     st.image('0619/스켈레톤.png')
#                 with col404:
#                     st.image('0619/원본.png')
#             # 여따가 들어갈 표, 시각화툴 필요함
#             #이 선수의 팔 부상확률이 몇 프로 
#             #유사 투구를 하는 선수 링크(?)
#             st.markdown('') # 예시, 대체가능
#         with tab3:
#             st.subheader('부상위험요인')
#             col501, col502, col503 = st.columns(3)
#             with col501:
#                 st.write('부상위험요인1')
#     elif selected_page == '고우석':
#         st.write('고우석 상세정보')
#         # 고우석 상세정보 코드 여기에
#     # 기타 선수들에 대한 코드는 elif를 이용하여 추가


