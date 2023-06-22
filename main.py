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

# 재활, 부상, 가능 나열하기 위한 리스트
injury = ['가능','재활','부상']



#일단 예시로 해당csv파일 활용
df = pd.read_csv('lgpitch.csv')
df1 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
df1 = df1.set_index('선수ID')

# injured_list.csv 파일
Injured_List = pd.read_csv('Injured_List.csv', encoding='cp949')

# injured_list3.csv 파일
Injured_List3 = pd.read_csv('./players/Injured_List3.csv', encoding='cp949')
Injured_List3 = Injured_List3.groupby(['부상명'])['선수'].count()
Injured_List3 = Injured_List3.sort_values(ascending=False)

# -------------------- ▼ 필요 변수 생성 코딩 Start ▼ --------------------

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="AI 부상 방지 솔루션",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded")
# -------------------- ▲ 필요 변수 생성 코딩 End ▲ --------------------

# -------------------- ▼ Streamlit 웹 화면 구성 START ▼ --------------------

st.title('대시보드')
# 대시보드 페이지의 내용 추가
want_to_contribute = st.button("팀 화면으로 이동")
if want_to_contribute:
    switch_page("팀")

want_to_contribute1 = st.button("투수 화면으로 이동")
if want_to_contribute1:
    switch_page("투수")

## -------------------- ▼ 요약 START ▼ --------------------

col11, col12 = st.columns(2)
with col11:
    st.subheader("요약")
    #fake.dataframe()
    
    col111, col112 = st.columns(2)
    with col111:
        col111.metric('시즌 총 부상빈도', '7 회', '작년 대비 2 회')
        # 현재 투수 부상 현황
        fig = px.pie(now_injured.sort_values(by = '출전여부', key=lambda s: s.map({k: i for i, k in enumerate(injury)})), values="값", names = "출전여부", title="현재 투수 부상 현황", hole=.7, 
                     color = '출전여부', color_discrete_map={'부상':'#df839b', '재활':'#8e8e8d', '가능':'#f6f6f6'})
        fig.update_traces(textposition='outside', textinfo='percent+label+value', textfont_size=10)
        fig.update_layout(font=dict(size=16))
        fig.update_layout(width=250,height=300)
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
        

    #부상고위험투수통계 도넛차트
    
    with col112:
        col112.metric('시즌 총 누적부상일수', '125 일', ' 작년대비 20일')
        
        # 현재 팀 투수 부상 누적일수
        fig2 = px.pie(high, values="값", names = "부상위험", title="현재 부상 고위험 투수 통계", hole=.7
                      , color = '부상위험', color_discrete_map={'고위험':'#BE0737', '보통':'#ededed'})
        fig2.update_traces(textposition='outside', textinfo='percent+label+value', textfont_size=10)
        fig2.update_layout(font=dict(size=16))
        fig2.update_layout(width=250,height=300)
        fig2.update(layout_showlegend=False)
        st.plotly_chart(fig2)
        

# -------------------- ▲ 요약 End ▲ --------------------

## -------------------- ▼ 경기일정 START ▼ --------------------

with col12:
    st.subheader("경기일정")
    st.dataframe(df)  # 경기일정 data프레임이 들어가야함

# --------------------- ▲ 경기일정 End ▲ --------------------


## -------------------- ▼ 부상통계 START ▼ --------------------

st.subheader("부상통계")
st.write("\n")  # additional space
col21, col22, col23 = st.columns([0.8, 0.1, 1.0]) # st.columns([0.1, 0.3, 0.1, 0.3])

# 팀부상종류 통계
with col21:
    st.text('2023시즌 팀 부상 종류')
    st.dataframe(Injured_List3)
    
# 팀부상선수 한명씩 나열    
# 선수 1
with col23:
    st.text('최근 부상자')
    col231, col232, col233, col234, col235= st.columns([0.4, 0.05, 0.4, 0.05, 0.4])
    with col231:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png', width=200)
        st.markdown("""<br>
         <div style="text-align: center;">
             <h3 style="margin-top: 15px;">이정용</h3>
         </div>
         """, unsafe_allow_html=True)
        
        st.text('부상부위: tommy john surgury') # 1. 파일에 부상정보가 없음(가라데이터 필요) 2. 지금은 선수 부상부위가 중복으로 들어간게 있음      
        st.text(f"부상발생일: {Injured_List['날짜'][0]}") # 해당 선수의 부상일자로 변경해야함
        st.text("예상 복귀일: D-7")
        
# 선수 2    
    with col233:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png', width=200)
        st.markdown("""<br>
         <div style="text-align: center;">
             <h3 style="margin-top: 15px;">고우석</h3>
         </div>
         """, unsafe_allow_html=True)
        
        st.text('부상부위: tommy john surgury')           
        st.text(f"부상 발생일: {Injured_List['날짜'][1]}") 
        st.text("예상 복귀일: D-7")
 
# 선수 3        
    with col235:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png', width=200)
        st.markdown("""<br>
         <div style="text-align: center;">
             <h3 style="margin-top: 15px;">이민호</h3>
         </div>
         """, unsafe_allow_html=True)
        
        st.text('부상부위: tommy john surgury')           
        st.text(f"부상발생일: {Injured_List['날짜'][0]}") 
        st.text("예상 복귀일: D-3")
    
    
    
    
    
    # <혹시 몰라, 안버린 코드>
    # 1.  반원 차트
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