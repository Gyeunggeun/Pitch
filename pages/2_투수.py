import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from streamlit_faker import get_streamlit_faker

# 데이터프레임 여기에
df = pd.read_excel('lgpitch.xlsx')
df1 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[0]]
df1 = df1.set_index('선수ID') # 강효종
df2 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[1]]
df2 = df2.set_index('선수ID') # 고우석
df3 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[3]]
df3 = df3.set_index('선수ID') # 이민호
df4 = df[['선수ID', '포지션', '출장경기수', '이닝', '투구수', '승리', '패배', '홀드', '세이브', 'ERA', '탈삼진', 'WHIP']].iloc[[4]]
df4 = df4.set_index('선수ID') # 이정용


# 부상 패턴 매트릭스
injury_recsys = pd.read_csv('injury_recsys.csv')

injury_list_gang = injury_recsys.iloc[29].sort_values(ascending =False).head(3) #'강효종 부상이력 유사 선수'
injury_list_suk = injury_recsys.iloc[5].sort_values(ascending =False).head(3)    #'이우석' 부상 패턴 top3
injury_list_ho= injury_recsys.iloc[4].sort_values(ascending =False).head(3)      #'이민호' 부상 패턴 top3
injury_list_young = injury_recsys.iloc[6].sort_values(ascending =False).head(3)  #'이정용' 부상 패턴 top3


# streamlit faker 사용 (임시)
fake = get_streamlit_faker(seed=42)

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="선수 목록",
    page_icon="🧢",
    layout="wide",
    initial_sidebar_state="expanded")

# 선수 이미지 URL
players = { 
    '강효종': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/6a00464c37f059ac3b52898fabd77bad8e7b36f3/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png',
    '고우석': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png',
    '김대현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EB%8C%80%ED%98%84.png',
    '김동규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EB%8F%99%EA%B7%9C.png',
    '김영준': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%98%81%EC%A4%80.png',
    '김유영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%9C%A0%EC%98%81.png',
    '김윤식': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%9C%A4%EC%8B%9D.png',
    '김주완': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%A3%BC%EC%99%84.png',
    '김진성': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%A7%84%EC%84%B1.png',
    '박명근': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%95%EB%AA%85%EA%B7%BC.png',
    '배재준': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%B0%EC%9E%AC%EC%A4%80.png',
    '백승현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%B1%EC%8A%B9%ED%98%84.png',
    '성동현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%84%B1%EB%8F%99%ED%98%84.png',
    '손주영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%86%90%EC%A3%BC%EC%98%81.png',
    '송은범': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%86%A1%EC%9D%80%EB%B2%94.png',
    '유영찬': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9C%A0%EC%98%81%EC%B0%AC.png',
    '윤호솔': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9C%A4%ED%98%B8%EC%86%94.png',
    '이민호': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png',
    '이상규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%83%81%EA%B7%9C.png',
    '이상영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%83%81%EC%98%81.png',
    '이우찬': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%9A%B0%EC%B0%AC.png',
    '이정용': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png',
    '이지강': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A7%80%EA%B0%95.png',
    '임정우': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9E%84%EC%A0%95%EC%9A%B0.png',
    '임찬규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9E%84%EC%B0%AC%EA%B7%9C.png',
    '정우영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A0%95%EC%9A%B0%EC%98%81.png',
    '조원태': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A1%B0%EC%9B%90%ED%83%9C.png',
    '진해수': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A7%84%ED%95%B4%EC%88%98.png',
    '채지선': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B1%84%EC%A7%80%EC%84%A0.png',
    '최동환': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B5%9C%EB%8F%99%ED%99%98.png',
    '최성훈': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B5%9C%EC%84%B1%ED%9B%88.png',
    '켈리'  : 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%BC%88%EB%A6%AC.png',
    '플럿코': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%ED%94%8C%EB%9F%BF%EC%BD%94.png',
    '함덕주': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%ED%95%A8%EB%8D%95%EC%A3%BC.png'
}

# 사이드바
pages = ['선수 목록'] + list(players.keys())
selected_page = st.sidebar.selectbox('페이지', pages)

# 선수 목록 페이지 구성
if selected_page == '선수 목록':
    st.title('선수 목록')
    player_list = list(players.keys())
    for i in range(0, len(player_list), 5):  # 5*7 로 총 35명의 선수 이미지 표현
        columns = st.columns(5)
        for j in range(5):
            if i + j < len(player_list):
                player = player_list[i + j]
                with columns[j]:
                    image_url = players[player]
                    st.markdown(f'''
                        <div style="text-align: center;">
                            <img src="{image_url}" width="100%">
                            <p style="margin-top: 0px; color: white; font-size: 20px; font-weight: bold">{player}</p>
                        </div>
                    ''', unsafe_allow_html=True)
else:
    st.title(f'{selected_page}')
    # 선수의 세부 페이지에서 보여줄 정보
    if selected_page == '강효종':
        tab1, tab2= st.tabs(['선수 프로필', '투구영상'])
        with tab1:
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=300)
            with col302:
                st.subheader("선수 기본 프로필")
                st.text("이름: 강효종")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 2002년 10월 14일")
                st.text("신장/체중: 184cm/86kg")
            st.text('팔꿈치 부상 위험 존재') # 이것도 볼드체로
            st.write('2023시즌') # 볼드체로
            st.dataframe(df1, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            # st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
            col303, col304, col305 = st.columns(3)

            with col303:
                st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                '<strong>Shoulder</strong> | May 1<br>'
                '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                '</div>', unsafe_allow_html=True)

                
            with col304:
                st.image('body/이두원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Biceps</strong> | April 17<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Oblique</strong> | Feb 4<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">30 days</span>'
                            '</div>', unsafe_allow_html=True)

            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_gang.index[0]), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_gang.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_gang.index[2]), unsafe_allow_html=True)
            #fake.bar_chart()
            

        with tab2:
            st.subheader('투구 분석')
            fake.line_chart()
            # st.image('투구별 어깨,팔꿈치 부상위험도 차트 이미지 삽입')
            option = st.selectbox('투구를 선택하세요',
                         ['1구', '2구', '3구', '4구', '5구', '6구', '7구', '8구', '9구', '10구','11구', '12구', '13구', '14구', '15구', '16구', '17구', '18구', '19구', '20구'])
            st.write('선택 옵션:', option)
            if option == '1구':
                col401, col402 = st.columns(2)
                with col401:
                    st.video('https://youtu.be/f-tq3W2HvT8') # 출처 필요 -> 세부 페이지에
                with col402: 
                    st.video('https://youtu.be/8s-ZllEX4Zk')
            elif option == '2구':
                col403, col404 = st.columns(2)
                with col403:
                    st.image('0619/스켈레톤.png')
                with col404:
                    st.image('body/어깨 후면.png')
    elif selected_page == '고우석':
        tab1, tab2= st.tabs(['선수 프로필', '투구영상'])
        with tab1:
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png', width=300)
            with col302:
                st.subheader("선수 기본 프로필")
                st.text("이름: 고우석")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 1998년 8월 6일")
                st.text("신장/체중: 177cm/90kg")
            st.markdown('_팔꿈치 부상 위험 존재_') # 이것도 볼드체로
            st.write('2023시즌')
            st.dataframe(df2, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            # st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
            col303, col304, col305 = st.columns(3)

            with col303:
                st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                '<strong>Shoulder</strong> | May 22<br>'
                '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                '</div>', unsafe_allow_html=True)

                
            with col304:
                st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Shoulder</strong> | May 12<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Shoulder</strong> | May 2<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)
                st.markdown('')
            
            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_suk.index[0]), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_suk.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_suk.index[2]), unsafe_allow_html=True)
            #fake.bar_chart()
        
        with tab2:
            st.subheader('투구 분석')
            fake.line_chart()
            # st.image('투구별 어깨,팔꿈치 부상위험도 차트 이미지 삽입')
            option = st.selectbox('투구를 선택하세요',
                         ['1구', '2구', '3구', '4구', '5구', '6구', '7구', '8구', '9구', '10구','11구', '12구', '13구', '14구', '15구', '16구', '17구', '18구', '19구', '20구'])
            st.write('선택 옵션:', option)
            if option == '1구':
                col401, col402 = st.columns(2)
                with col401:
                    st.video('https://youtu.be/KzDgIkzRfw8') # 출처 필요 -> 세부 페이지에
                with col402: 
                    st.video('https://youtu.be/HTNdAHUKhjg')
            elif option == '2구':
                col403, col404 = st.columns(2)
                with col403:
                    st.image('0619/스켈레톤.png')
                with col404:
                    st.image('0619/원본.png')
    elif selected_page == '이민호':
        tab1, tab2= st.tabs(['선수 프로필', '투구영상'])
        with tab1:
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png', width=300)
            with col302:
                st.subheader("선수 기본 프로필")
                st.text("이름: 이민호")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 2001년 8월 30일")
                st.text("신장/체중: 189cm/95kg")
            st.markdown('_팔꿈치 부상 위험 존재_') # 이것도 볼드체로
            st.write('2023시즌')
            st.dataframe(df3, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            # st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
            col303, col304, col305 = st.columns(3)

            with col303:
                st.image('body/삼두원.png')
                st.markdown('<div style="text-align: center;">'
                '<strong>Shoulder</strong> | April 10<br>'
                '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                '</div>', unsafe_allow_html=True)

                
            with col304:
                st.image('body/옆구리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Oblique</strong> | March 23<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Oblique</strong> | Feb 4<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">30 days</span>'
                            '</div>', unsafe_allow_html=True)

            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_ho.index[0]), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_ho.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_ho.index[2]), unsafe_allow_html=True)
            #fake.bar_chart() 
            
        with tab2:
            st.subheader('투구 분석')
            fake.line_chart()
            # st.image('투구별 어깨,팔꿈치 부상위험도 차트 이미지 삽입')
            option = st.selectbox('투구를 선택하세요',
                         ['1구', '2구', '3구', '4구', '5구', '6구', '7구', '8구', '9구', '10구','11구', '12구', '13구', '14구', '15구', '16구', '17구', '18구', '19구', '20구'])
            st.write('선택 옵션:', option)
            if option == '1구':
                col401, col402 = st.columns(2)
                with col401:
                    st.video('https://youtu.be/vmfSRPTCd08') # 출처 필요 -> 세부 페이지에
                with col402: 
                    st.video('https://youtu.be/n-5u2sF28VI')
            elif option == '2구':
                col403, col404 = st.columns(2)
                with col403:
                    st.image('0619/스켈레톤.png')
                with col404:
                    st.image('0619/원본.png')           
    elif selected_page == '이정용':
        tab1, tab2= st.tabs(['선수 프로필', '투구영상'])
        with tab1:
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png', width=300)
            with col302:
                st.subheader("선수 기본 프로필")
                st.text("이름: 이정용")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 1996년 3월 26일")
                st.text("신장/체중: 186cm/85kg")
            st.markdown('_팔꿈치 부상 위험 존재_') # 이것도 볼드체로
            st.write('2023시즌')
            st.dataframe(df4, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            # st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
            col303, col304, col305 = st.columns(3)

            with col303:
                st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                '<strong>Shoulder</strong> | May 1<br>'
                '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                '</div>', unsafe_allow_html=True)

                
            with col304:
                st.image('body/이두원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Biceps</strong> | April 17<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<strong>Oblique</strong> | Feb 4<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">30 days</span>'
                            '</div>', unsafe_allow_html=True)
            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_young.index[0]), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_young.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_young.index[2]), unsafe_allow_html=True)
            #fake.bar_chart()
            
        with tab2:
            st.subheader('투구 분석')
            fake.line_chart()
            # st.image('투구별 어깨,팔꿈치 부상위험도 차트 이미지 삽입')
            option = st.selectbox('투구를 선택하세요',
                         ['1구', '2구', '3구', '4구', '5구', '6구', '7구', '8구', '9구', '10구','11구', '12구', '13구', '14구', '15구', '16구', '17구', '18구', '19구', '20구'])
            st.write('선택 옵션:', option)
            if option == '1구':
                col401, col402 = st.columns(2)
                with col401:
                    st.video('https://youtu.be/9hXEKLezRmA') # 출처 필요 -> 세부 페이지에
                with col402: 
                    st.video('https://youtu.be/06f3maD7DzA')
            elif option == '2구':
                col403, col404 = st.columns(2)
                with col403:
                    st.image('0619/스켈레톤.png')
                with col404:
                    st.image('0619/원본.png')
        # 고우석 상세정보 코드 여기에
    # 기타 선수들에 대한 코드는 elif를 이용하여 추가
