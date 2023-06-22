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

## -------------------- ▼ 경기일정 START ▼ --------------------

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

col101, col102, col103, col104 = st.columns(4)
with col101:
    st.markdown(lnk + htmlstr, unsafe_allow_html=True)
with col102:
    st.markdown(lnk + htmlstr2, unsafe_allow_html=True)
with col103:
    st.markdown(lnk + htmlstr3, unsafe_allow_html=True)
with col104:
    st.markdown(lnk + htmlstr4, unsafe_allow_html=True)
    
# -------------------- ▲ 경기일정 End ▲ --------------------

## -------------------- ▼ 요약 START ▼ --------------------

st.subheader("요약")
col201, col202, col203, col204 = st.columns(4)
with col201:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col201.metric('시즌 총 부상빈도', "7", '2 회')

with col202:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col202.metric('시즌 총 누적부상일수', "115", ' 20일')

with col203:
    fig = px.pie(now_injured, values="값", names="출전여부", title="현재투수부상현황", hole=.7, color = '출전여부', color_discrete_map={'부상':'#df839b', '재활':'#8e8e8d', '가능':'#f6f6f6'})
    #fig.update_traces(now_injured.sort_values(by="출전여부", key=leg)
    fig.update_traces(textposition='outside', textinfo='label+value',
                          textfont_size=10) # textfont_color="blact"
    fig.update_layout(font=dict(size=16))
    fig.update_layout(width=250,height=300)
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig)
with col204:
    # 현재 팀 투수 부상 누적일수
    fig2 = px.pie(high, values="값", names = "부상위험", title="현재 부상 고위험 투수 통계", hole=.7, color = '부상위험', color_discrete_map={'고위험':'#BE0737', '보통':'#ededed'})
    fig2.update_traces(textposition='outside', textinfo='label+value', textfont_size=10)
    fig2.update_layout(font=dict(size=16))
    fig2.update_layout(width=250,height=300)
    fig2.update(layout_showlegend=False)
    st.plotly_chart(fig2)
    
    #st.dataframe(df)  # 경기일정 data프레임이 들어가야함

# --------------------- ▲ 요약 End ▲ --------------------

## -------------------- ▼ 부상통계 START (규한파일합치기) ▼ --------------------

st.subheader("부상통계")