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
import elbowtorque as tq


# streamlit faker
fake = get_streamlit_faker(seed=42)

# 현재부상투수현황 데이터프레임
# 재활, 부상, 가능 나열하기 위한 리스트
injury = ['가능','재활','부상']
now_injured = pd.read_csv('now_injured.csv', encoding='euc-kr')

# 부상x선수 중 부상 위험도 데이터프레임
high = pd.read_csv('high.csv', encoding='euc-kr')

# 부상자 csv 데이터프레임 !!
# injury = pd.read_csv('injury.csv')
# df1 = injury[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
# df1 = df1.set_index('선수ID')

#일단 예시로 해당csv파일 활용
df = pd.read_csv('lgpitch.csv')
df1 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
df1 = df1.set_index('선수ID')

# injured_list.csv 파일
Injured_List = pd.read_csv('Injured_List.csv')

# injured_list3.csv 파일
Injured_List3 = pd.read_csv('Injured_List3.csv',encoding='cp949' )
Injured_List3 = Injured_List3.groupby(['부상명'])['선수'].count()
Injured_List3 = Injured_List3.sort_values(ascending=False)

# injured_list.csv 파일
Injured_List = pd.read_csv('Injured_List.csv')

# injured_list3.csv 파일
Injured_List3 = pd.read_csv('players/Injured_List3.csv')
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

# st.title('대시보드')
# # 대시보드 페이지의 내용 추가
# want_to_contribute = st.button("팀 화면으로 이동")
# if want_to_contribute:
#     switch_page("팀")

# want_to_contribute1 = st.button("투수 화면으로 이동")
# if want_to_contribute1:
#     switch_page("투수")

st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)

## -------------------- ▼ 경기일정 START ▼ --------------------

st.title('대시보드')
st.subheader("경기일정")
st.write('2023년 06월 21일 (수)')





#can apply customisation to almost all the properties of the card, including the progress bar
                              

theme_away = {'bgcolor': '#f6f6f6','title_color': '#8e8e8d','content_color': '#8e8e8d','icon_color': 'red', 'icon': 'fas fa-sign-in'}
theme_home = {'bgcolor': '#ededed','title_color': '#be0737','content_color': '#be0737','icon_color': 'orange', 'icon': 'fa fa-sign-out'}

cc = st.columns(4)

with cc[0]:
    # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
    hc.info_card(title='NC', content='06.22. (목) 18:30\naway 창원', theme_override=theme_away)

with cc[1]:
    hc.info_card(title='롯데', content='06.23. (금) 18:30 home 잠실',theme_override=theme_home)

with cc[2]:
    hc.info_card(title='롯데', content='06.24. (토) 17:00 home 잠실',theme_override=theme_home)

with cc[3]:
 #customise the the theming for a neutral content
    hc.info_card(title='롯데',content='06.25. (일) 17:00 home 잠실',key='sec',theme_override=theme_home)

    
# -------------------- ▲ 경기일정 End ▲ --------------------

## -------------------- ▼ 요약 START ▼ --------------------

st.subheader("요약")
col201, col202, col203, col204 = st.columns(4)
with col201:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col201.metric('시즌 총 부상빈도', "7 회", '2 회')

with col202:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    col202.metric('시즌 총 누적부상일수', "115 일", ' 20일')

with col203:
    custom_order = ['부상', '재활', '가능']

    fig = px.pie(now_injured, values="값", names="출전여부", title="현재투수부상현황", hole=.7, color = '출전여부', color_discrete_map={'부상':'#df839b', '재활':'#8e8e8d', '가능':'#f6f6f6'}, category_orders={"출전여부": custom_order})

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
    
    fig2 = px.pie(high, values="값", names = "부상위험", title="현재 부상 고위험 투수 통계", hole=.7, color = '부상위험', color_discrete_map={'고위험':'#BE0737', '보통':'#ededed'},category_orders={"부상위험": custom_order1})

    fig2.update_traces(textposition='outside', textinfo='label+value', textfont_size=10)
    fig2.update_layout(font=dict(size=16))
    fig2.update_layout(width=250,height=300)
    fig2.update(layout_showlegend=False)
    st.plotly_chart(fig2)
    
    #st.dataframe(df)  # 경기일정 data프레임이 들어가야함

# --------------------- ▲ 요약 End ▲ --------------------

## -------------------- ▼ 부상통계 START (규한파일합치기) ▼ --------------------


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

        st.markdown("부상부위: tommy john surgury\n"
            "\n부상발생일: {}\n"
            "\n예상 복귀일: D-10".format(Injured_List['날짜'][0]))
        
# 선수 2    
    with col233:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png', width=200)
        st.markdown("""<br>
         <div style="text-align: center;">
             <h3 style="margin-top: 15px;">고우석</h3>
         </div>
         """, unsafe_allow_html=True)
       
        st.markdown("부상부위: tommy john surgury\n"
            "\n부상발생일: {}\n"
            "\n예상 복귀일: D-7".format(Injured_List['날짜'][1]))

# 선수 3        
    with col235:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png', width=200)
        st.markdown("""<br>
         <div style="text-align: center;">
             <h3 style="margin-top: 15px;">이민호</h3>
         </div>
         """, unsafe_allow_html=True)
   
        st.markdown("부상부위: tommy john surgury\n"
            "\n부상발생일: {}\n"
            "\n예상 복귀일: D-3".format(Injured_List['날짜'][2]))
    
   
