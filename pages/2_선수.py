import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objs as go
import time
from packages.logo import add_logo

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
injury_recsys = pd.read_csv('injury_recsys_kor.csv')

injury_list_gang = injury_recsys.iloc[29].sort_values(ascending =False).head(3) #'강효종 부상이력 유사 선수'
injury_list_suk = injury_recsys.iloc[5].sort_values(ascending =False).head(3)    #'이우석' 부상 패턴 top3
injury_list_ho= injury_recsys.iloc[4].sort_values(ascending =False).head(3)      #'이민호' 부상 패턴 top3
injury_list_young = injury_recsys.iloc[6].sort_values(ascending =False).head(3)  #'이정용' 부상 패턴 top3



# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="선수",
    page_icon="🧢",
    layout="wide",
    initial_sidebar_state="expanded",
    )
add_logo("_솔루션로고\\로고확장4.png", height=370)

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
pages = ['선수'] + list(players.keys())
selected_page = st.sidebar.selectbox('확인할 선수를 선택해주세요.', pages)

# 선수 목록 페이지 구성
if selected_page == '선수':
    st.title('선수')
    st.markdown("""
            <style>
                  hr {
                    height: 3px; /* 가로줄의 두께를 지정 */
                    background-color: white; /* 가로줄의 색상을 지정 */
                  }
            </style>
            <hr>

            """, unsafe_allow_html=True)
    
    st.subheader('투수 목록')
    st.write("가나다순")
    st.write("")
    
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
        tab1, tab2, tab3= st.tabs(['선수 프로필', '부하 측정','전체 투구 영상'])
        with tab1:
            st.subheader("선수 기본 프로필")
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/6a00464c37f059ac3b52898fabd77bad8e7b36f3/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png', width=300)
            with col302:
                st.text("이름: 강효종")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 2002년 10월 14일")
                st.text("신장/체중: 184cm/86kg")
            st.markdown("")
            st.write('2023시즌') # 볼드체로
            st.dataframe(df1, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            col303, col304, col305 = st.columns(3)

            with col303:
                #st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%96%B4%EA%B9%A8%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | May 1<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                             '</div>', unsafe_allow_html=True)

                
            with col304:
                #st.image('body/이두원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%9D%B4%EB%91%90%EC%9B%90.png">'
                            '<br>'
                            '<strong>Biceps</strong> | April 17<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                #st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%ED%97%88%EB%A6%AC%EC%9B%90.png">'
                            '<br>'
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
            st.markdown('')
            options = [injury_list_gang.index[0], injury_list_gang.index[1], injury_list_gang.index[2]]
            selected_option = st.selectbox("부상명을 선택하세요:", options)
            if selected_option == options[0]:  # injury_list_gang.index[0]
                video_file = open("treatment_videos\\TommyJohn.mp4", 'rb')
            elif selected_option == options[1]:  # injury_list_suk.index[1]
                video_file = open("treatment_videos\\neck.mp4", 'rb')
            elif selected_option == options[2]:  # injury_list_suk.index[2]
                video_file = open("treatment_videos\\calf.mp4", 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, format='mp4')
        with tab2:
            hjt = pd.read_csv('torque/hjtorque.csv')
            if st.button("부하 측정"):                    
                    # Streamlit 구성
                    st.markdown("<h1 style='text-align: center; color: white;'>투구별 토크 측정</h1>", unsafe_allow_html=True)
                    progress_bar = st.sidebar.progress(0)
                    status_text = st.sidebar.empty()
                    chart = st.empty()
            
                    # 위험 범위 정의
                    elbow_torque_danger = [105, 119]
                    shoulder_torque_danger = 25 # 15번째 투구가 위험

                    
                    st.markdown("""
                    <table>
                        <tr>
                            <th style='text-align: left; background-color: #606770'>위험 유형</th>
                            <th style='text-align: left; background-color: #606770'>기준</th>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 고위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 119 이상일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 105 이상 119 이하일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>어깨 토크 저위험</td>
                            <td style='text-align: left;'>어깨 토크가 25 미만일 때</td>
                        </tr>
                    </table>
                    <br>
                    """, unsafe_allow_html=True)
            
                    # 위험한 투구를 추적하는 리스트
                    dangerous_pitches = []
                    warning_pitches = []

                    # 그래프 및 데이터 초기 설정
                    fig = go.Figure()
                    elbow_x, elbow_y = [], []
                    shoulder_x, shoulder_y = [], []
                    elbow_danger_x, elbow_danger_y = [], []
                    elbow_very_danger_x, elbow_very_danger_y = [], []
                    shoulder_danger_x, shoulder_danger_y = [], []
            
                    # 처음에 선 그래프를 그립니다
                    fig.add_trace(go.Scatter(x=elbow_x, y=elbow_y, mode='lines', name='팔꿈치 토크'))
                    fig.add_trace(go.Scatter(x=shoulder_x, y=shoulder_y, mode='lines', name='어깨 토크'))
            
                    # 위험 점 추가
                    fig.add_trace(go.Scatter(x=elbow_danger_x, y=elbow_danger_y, mode='markers', marker=dict(color='yellow'), name='팔꿈치 토크 높음'))
                    fig.add_trace(go.Scatter(x=elbow_very_danger_x, y=elbow_very_danger_y, mode='markers', marker=dict(color='red'), name='팔꿈치 토크 매우 높음'))
                    fig.add_trace(go.Scatter(x=shoulder_danger_x, y=shoulder_danger_y, mode='markers', marker=dict(color='orange'), name='어깨 토크 낮음'))
            
                    for i in range(len(hjt)):
                        # 데이터프레임 행 단위 추가
                        row = hjt.iloc[i]
                    
                        # 데이터 업데이트
                        elbow_x.append(row['회차'])
                        elbow_y.append(row['elbow_Torque'])
                        shoulder_x.append(row['회차'])
                        shoulder_y.append(row['shoulder_Torque'])
            
                        # 위험 점 표시
                        elbow_danger = False
                        elbow_very_danger = False
                        shoulder_danger = False

                        if row['elbow_Torque'] >= elbow_torque_danger[0] and row['elbow_Torque'] <= elbow_torque_danger[1]:
                            elbow_danger_x.append(row['회차'])
                            elbow_danger_y.append(row['elbow_Torque'])
                            elbow_danger = True
                        elif row['elbow_Torque'] > elbow_torque_danger[1]:
                            elbow_very_danger_x.append(row['회차'])
                            elbow_very_danger_y.append(row['elbow_Torque'])
                            elbow_very_danger = True

                        if row['shoulder_Torque'] < shoulder_torque_danger:
                            shoulder_danger_x.append(row['회차'])
                            shoulder_danger_y.append(row['shoulder_Torque'])
                            shoulder_danger = True

                        if elbow_danger and shoulder_danger:
                            warning_pitches.append(int(row['회차']))

                        if elbow_very_danger and shoulder_danger:
                            dangerous_pitches.append(int(row['회차']))

                        # 그래프 업데이트
                        fig.data[0].x = elbow_x
                        fig.data[0].y = elbow_y
                        fig.data[1].x = shoulder_x
                        fig.data[1].y = shoulder_y
                        fig.data[2].x = elbow_danger_x
                        fig.data[2].y = elbow_danger_y
                        fig.data[3].x = elbow_very_danger_x
                        fig.data[3].y = elbow_very_danger_y
                        fig.data[4].x = shoulder_danger_x
                        fig.data[4].y = shoulder_danger_y
                        
                        chart.plotly_chart(fig)
                        status_text.text(f"{i+1}/{len(hjt)} rows processed.")
                        progress_bar.progress((i+1)/len(hjt))
                    
                        # 0.5초 간격 설정
                        time.sleep(0.25)
                    
                    progress_bar.empty()
                    for pitch in warning_pitches + dangerous_pitches:
                        st.warning(f"{pitch}번째 투구에서 위험 요소 탐지")
                        if pitch == 1:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\hyojong1.mp4') 
                            with col402: 
                                st.video('pitch_videos\\hyojong1_dotted.mp4')
                        elif pitch == 2:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\hyojong2.mp4')
                            with col404:
                                st.video('pitch_videos\\hyojong2_dotted.mp4')
                        elif pitch == 6:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\hyojong3.mp4')
                            with col402: 
                                st.video('pitch_videos\\hyojong3_dotted.mp4')
                        elif pitch == 7:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\hyojong4.mp4')
                            with col404:
                                st.video('pitch_videos\\hyojong4_dotted.mp4')
                        

                    
                    if not warning_pitches and not dangerous_pitches:
                        st.info("위험 투구 미발견")
        with tab3:
            st.subheader('투구 분석')

            selected_pitch = st.selectbox('투구를 선택하세요', [str(x) + '구' for x in range(1, 21)])
            selected_pitch_num = int(selected_pitch.replace('구', ''))

            if selected_pitch_num == 1:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\hyojong1.mp4') 
                with col402: 
                    st.video('pitch_videos\\hyojong1_dotted.mp4')
            elif selected_pitch_num == 2:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\hyojong2.mp4')
                with col404:
                    st.video('pitch_videos\\hyojong2_dotted.mp4')
            elif selected_pitch_num == 6:                                
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\hyojong3.mp4')
                with col402: 
                    st.video('pitch_videos\\hyojong3_dotted.mp4')
            elif selected_pitch_num == 7:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\hyojong4.mp4')
                with col404:
                    st.video('pitch_videos\\hyojong4_dotted.mp4')
    elif selected_page == '고우석':
        tab1, tab2, tab3= st.tabs(['선수 프로필', '부하 측정','전체 투구 영상'])
        with tab1:
            st.subheader("선수 기본 프로필")
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png', width=300)
            with col302:
                st.text("이름: 고우석")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 1998년 8월 6일")
                st.text("신장/체중: 177cm/90kg")
            st.markdown("")
            st.write('2023시즌')
            st.dataframe(df2, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")            
            col303, col304, col305 = st.columns(3)

            with col303:
                #st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%96%B4%EA%B9%A8%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | May 22<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

                
            with col304:
                #st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%96%B4%EA%B9%A8%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | May 12<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                #st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%96%B4%EA%B9%A8%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | May 2<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)
                st.markdown('')
            
            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format('팔꿈치 통증'), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_suk.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_suk.index[2]), unsafe_allow_html=True)
            st.markdown('')
            options = ['팔꿈치 통증', injury_list_suk.index[1], injury_list_suk.index[2]]
            selected_option = st.selectbox("부상명을 선택하세요:", options)
            if selected_option == options[0]:  # injury_list_suk.index[0]
                video_file = open("treatment_videos\\tenniselbow.mp4", 'rb')
            elif selected_option == options[1]:  # injury_list_suk.index[1]
                video_file = open("treatment_videos\\waist.mp4", 'rb')
            elif selected_option == options[2]:  # injury_list_suk.index[2]
                video_file = open("treatment_videos\\biceps.mp4", 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, format='mp4')
        with tab2:
            wst = pd.read_csv('torque/wstorque.csv')
            if st.button("부하 측정"):                    
                    # Streamlit 구성
                    st.markdown("<h1 style='text-align: center; color: white;'>투구별 토크 측정</h1>", unsafe_allow_html=True)
                    progress_bar = st.sidebar.progress(0)
                    status_text = st.sidebar.empty()
                    chart = st.empty()
            
                    # 위험 범위 정의
                    elbow_torque_danger = [105, 119]
                    shoulder_torque_danger = 25 # 6번째 투구가 위험

                    
                    st.markdown("""
                    <table>
                        <tr>
                            <th style='text-align: left; background-color: #606770'>위험 유형</th>
                            <th style='text-align: left; background-color: #606770'>기준</th>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 고위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 119 이상일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 105 이상 119 이하일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>어깨 토크 저위험</td>
                            <td style='text-align: left;'>어깨 토크가 25 미만일 때</td>
                        </tr>
                    </table>
                    <br>s
                    """, unsafe_allow_html=True)
            
                    # 위험한 투구를 추적하는 리스트
                    dangerous_pitches = []
                    warning_pitches = []

                    # 그래프 및 데이터 초기 설정
                    fig = go.Figure()
                    elbow_x, elbow_y = [], []
                    shoulder_x, shoulder_y = [], []
                    elbow_danger_x, elbow_danger_y = [], []
                    elbow_very_danger_x, elbow_very_danger_y = [], []
                    shoulder_danger_x, shoulder_danger_y = [], []
            
                    # 처음에 선 그래프를 그립니다
                    fig.add_trace(go.Scatter(x=elbow_x, y=elbow_y, mode='lines', name='팔꿈치 토크'))
                    fig.add_trace(go.Scatter(x=shoulder_x, y=shoulder_y, mode='lines', name='어깨 토크'))
            
                    # 위험 점 추가
                    fig.add_trace(go.Scatter(x=elbow_danger_x, y=elbow_danger_y, mode='markers', marker=dict(color='yellow'), name='팔꿈치 토크 높음'))
                    fig.add_trace(go.Scatter(x=elbow_very_danger_x, y=elbow_very_danger_y, mode='markers', marker=dict(color='red'), name='팔꿈치 토크 매우 높음'))
                    fig.add_trace(go.Scatter(x=shoulder_danger_x, y=shoulder_danger_y, mode='markers', marker=dict(color='orange'), name='어깨 토크 낮음'))
            
                    for i in range(len(wst)):
                        # 데이터프레임 행 단위 추가
                        row = wst.iloc[i]
                    
                        # 데이터 업데이트
                        elbow_x.append(row['회차'])
                        elbow_y.append(row['elbow_Torque'])
                        shoulder_x.append(row['회차'])
                        shoulder_y.append(row['shoulder_Torque'])
            
                        # 위험 점 표시
                        elbow_danger = False
                        elbow_very_danger = False
                        shoulder_danger = False

                        if row['elbow_Torque'] >= elbow_torque_danger[0] and row['elbow_Torque'] <= elbow_torque_danger[1]:
                            elbow_danger_x.append(row['회차'])
                            elbow_danger_y.append(row['elbow_Torque'])
                            elbow_danger = True
                        elif row['elbow_Torque'] > elbow_torque_danger[1]:
                            elbow_very_danger_x.append(row['회차'])
                            elbow_very_danger_y.append(row['elbow_Torque'])
                            elbow_very_danger = True

                        if row['shoulder_Torque'] < shoulder_torque_danger:
                            shoulder_danger_x.append(row['회차'])
                            shoulder_danger_y.append(row['shoulder_Torque'])
                            shoulder_danger = True

                        if elbow_danger and shoulder_danger:
                            warning_pitches.append(int(row['회차']))

                        if elbow_very_danger and shoulder_danger:
                            dangerous_pitches.append(int(row['회차']))

                        # 그래프 업데이트
                        fig.data[0].x = elbow_x
                        fig.data[0].y = elbow_y
                        fig.data[1].x = shoulder_x
                        fig.data[1].y = shoulder_y
                        fig.data[2].x = elbow_danger_x
                        fig.data[2].y = elbow_danger_y
                        fig.data[3].x = elbow_very_danger_x
                        fig.data[3].y = elbow_very_danger_y
                        fig.data[4].x = shoulder_danger_x
                        fig.data[4].y = shoulder_danger_y
                        
                        chart.plotly_chart(fig)
                        status_text.text(f"{i+1}/{len(wst)} rows processed.")
                        progress_bar.progress((i+1)/len(wst))
                    
                        # 0.5초 간격 설정
                        time.sleep(0.25)
                    
                    progress_bar.empty()
                    for pitch in warning_pitches + dangerous_pitches:
                        st.warning(f"{pitch}번째 투구에서 위험 요소 탐지")

                        # 첫 번째 위험한 투구를 바로 보여주기
                        if pitch == 1:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\gowoo1.mp4') 
                            with col402: 
                                st.video('pitch_videos\\gowoo1_dotted.mp4')
                        elif pitch == 2:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\gowoo2.mp4')
                            with col404:
                                st.video('pitch_videos\\gowoo2_dotted.mp4')
                        elif pitch == 3:
                            col405, col406 = st.columns(2)
                            with col405:
                                st.video('pitch_videos\\gowoo3.mp4')
                            with col406:
                                st.video('pitch_videos\\gowoo3_dotted.mp4')
                        elif pitch == 4:
                            col407, col408 = st.columns(2)
                            with col407:
                                st.video('pitch_videos\\gowoo4.mp4')
                            with col408:
                                st.video('pitch_videos\\gowoo4_dotted.mp4')
                        elif pitch == 5:
                            col409, col410 = st.columns(2)
                            with col409:
                                st.video('pitch_videos\\gowoo5.mp4')
                            with col410:
                                st.video('pitch_videos\\gowoo5_dotted.mp4')
                        elif pitch == 6:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\gowoo6.mp4')
                            with col402: 
                                st.video('pitch_videos\\gowoo6_dotted.mp4')
                        elif pitch == 7:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\gowoo7.mp4')
                            with col404:
                                st.video('pitch_videos\\gowoo7_dotted.mp4')
                        elif pitch == 8:
                            col405, col406 = st.columns(2)
                            with col405:
                                st.video('pitch_videos\\gowoo8.mp4')
                            with col406:
                                st.video('pitch_videos\\gowoo8_dotted.mp4')
                        elif pitch == 9:
                            col407, col408 = st.columns(2)
                            with col407:
                                st.video('pitch_videos\\gowoo9.mp4')
                            with col408:
                                st.video('pitch_videos\\gowoo9_dotted.mp4')
                        elif pitch == 17:
                            col409, col410 = st.columns(2)
                            with col409:
                                st.video('pitch_videos\\gowoo10.mp4')
                            with col410:
                                st.video('pitch_videos\\gowoo10_dotted.mp4')
                    if not warning_pitches and not dangerous_pitches:
                        st.info("위험 투구 미발견")
        with tab3:
            st.subheader('투구 분석')
            selected_pitch = st.selectbox('투구를 선택하세요', [str(x) + '구' for x in range(1, 21)])
            selected_pitch_num = int(selected_pitch.replace('구', ''))

            if selected_pitch_num == 1:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\gowoo1.mp4')
                with col402: 
                    st.video('pitch_videos\\gowoo1_dotted.mp4')
            elif selected_pitch_num == 2:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\gowoo2.mp4')
                with col404:
                    st.video('pitch_videos\\gowoo2_dotted.mp4')
            elif selected_pitch_num == 3:
                col405, col406 = st.columns(2)
                with col405:
                    st.video('pitch_videos\\gowoo3.mp4')
                with col406:
                    st.video('pitch_videos\\gowoo3_dotted.mp4')
            elif selected_pitch_num == 4:
                col407, col408 = st.columns(2)
                with col407:
                    st.video('pitch_videos\\gowoo4.mp4')
                with col408:
                    st.video('pitch_videos\\gowoo4_dotted.mp4')

            elif selected_pitch_num == 5:
                col409, col410 = st.columns(2)
                with col409:
                    st.video('pitch_videos\\gowoo5.mp4')
                with col410:
                    st.video('pitch_videos\\gowoo5_dotted.mp4')
            elif selected_pitch_num == 6:                                
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\gowoo6.mp4')
                with col402: 
                    st.video('pitch_videos\\gowoo6_dotted.mp4')
            elif selected_pitch_num == 7:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\gowoo7.mp4')
                with col404:
                    st.video('pitch_videos\\gowoo7_dotted.mp4')
            elif selected_pitch_num == 8:
                col405, col406 = st.columns(2)
                with col405:
                    st.video('pitch_videos\\gowoo8.mp4')
                with col406:
                    st.video('pitch_videos\\gowoo8_dotted.mp4')
            elif selected_pitch_num == 9:
                col407, col408 = st.columns(2)
                with col407:
                    st.video('pitch_videos\\gowoo9.mp4')
                with col408:
                    st.video('pitch_videos\\gowoo9_dotted.mp4')
            elif selected_pitch_num == 17:
                col409, col410 = st.columns(2)
                with col409:
                    st.video('pitch_videos\\gowoo10.mp4')
                with col410:
                    st.video('pitch_videos\\gowoo10_dotted.mp4')   
    elif selected_page == '이민호':
        tab1, tab2, tab3= st.tabs(['선수 프로필', '부하 측정','전체 투구 영상'])
        with tab1:
            st.subheader("선수 기본 프로필")
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png', width=300)
            with col302:
                st.text("이름: 이민호")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 2001년 8월 30일")
                st.text("신장/체중: 189cm/95kg")
            st.markdown('') # 이것도 볼드체로
            st.write('2023시즌')
            st.dataframe(df3, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            # st.text("5월 27일 Tommy john surgery (23일 전)") # 이부분 표로?? 아님 데이터프레임?? 
            col303, col304, col305 = st.columns(3)

            with col303:
                #st.image('body/삼두원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%82%BC%EB%91%90%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | April 10<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                            '</div>', unsafe_allow_html=True)

                
            with col304:
                #st.image('body/옆구리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%98%86%EA%B5%AC%EB%A6%AC%EC%9B%90.png">'
                            '<br>'
                            '<strong>Oblique</strong> | March 23<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                #st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%ED%97%88%EB%A6%AC%EC%9B%90.png">'
                            '<br>'
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
            options = [injury_list_ho.index[0], injury_list_ho.index[1], injury_list_ho.index[2]]
            selected_option = st.selectbox("부상명을 선택하세요:", options)
            if selected_option == options[0]:  # injury_list_ho.index[0]
                video_file = open("treatment_videos\\tenniselbow.mp4", 'rb')
            elif selected_option == options[1]:  # injury_list_ho.index[1]
                video_file = open("treatment_videos\\forearm2.mp4", 'rb')
            elif selected_option == options[2]:  # injury_list_ho.index[2]
                video_file = open("treatment_videos\\forearm2.mp4", 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, format='mp4')
            
        with tab2:
            st.subheader('투구 분석')
            mht = pd.read_csv('torque/mhtorque.csv')
            if st.button("부하 측정"):                    
                    # Streamlit 구성
                    st.markdown("<h1 style='text-align: center; color: white;'>투구별 토크 측정</h1>", unsafe_allow_html=True)
                    progress_bar = st.sidebar.progress(0)
                    status_text = st.sidebar.empty()
                    chart = st.empty()
            
                    # 위험 범위 정의
                    elbow_torque_danger = [105, 119]
                    shoulder_torque_danger = 25

                    
                    st.markdown("""
                    <table>
                        <tr>
                            <th style='text-align: left; background-color: #606770'>위험 유형</th>
                            <th style='text-align: left; background-color: #606770'>기준</th>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 고위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 119 이상일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 105 이상 119 이하일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>어깨 토크 저위험</td>
                            <td style='text-align: left;'>어깨 토크가 25 미만일 때</td>
                        </tr>
                    </table>
                    <br>
                    """, unsafe_allow_html=True)
            
                    # 위험한 투구를 추적하는 리스트
                    dangerous_pitches = []
                    warning_pitches = []

                    # 그래프 및 데이터 초기 설정
                    fig = go.Figure()
                    elbow_x, elbow_y = [], []
                    shoulder_x, shoulder_y = [], []
                    elbow_danger_x, elbow_danger_y = [], []
                    elbow_very_danger_x, elbow_very_danger_y = [], []
                    shoulder_danger_x, shoulder_danger_y = [], []
            
                    # 처음에 선 그래프를 그립니다
                    fig.add_trace(go.Scatter(x=elbow_x, y=elbow_y, mode='lines', name='팔꿈치 토크'))
                    fig.add_trace(go.Scatter(x=shoulder_x, y=shoulder_y, mode='lines', name='어깨 토크'))
            
                    # 위험 점 추가
                    fig.add_trace(go.Scatter(x=elbow_danger_x, y=elbow_danger_y, mode='markers', marker=dict(color='yellow'), name='팔꿈치 토크 높음'))
                    fig.add_trace(go.Scatter(x=elbow_very_danger_x, y=elbow_very_danger_y, mode='markers', marker=dict(color='red'), name='팔꿈치 토크 매우 높음'))
                    fig.add_trace(go.Scatter(x=shoulder_danger_x, y=shoulder_danger_y, mode='markers', marker=dict(color='orange'), name='어깨 토크 낮음'))
            
                    for i in range(len(mht)):
                        # 데이터프레임 행 단위 추가
                        row = mht.iloc[i]
                    
                        # 데이터 업데이트
                        elbow_x.append(row['회차'])
                        elbow_y.append(row['elbow_Torque'])
                        shoulder_x.append(row['회차'])
                        shoulder_y.append(row['shoulder_Torque'])
            
                        # 위험 점 표시
                        elbow_danger = False
                        elbow_very_danger = False
                        shoulder_danger = False

                        if row['elbow_Torque'] >= elbow_torque_danger[0] and row['elbow_Torque'] <= elbow_torque_danger[1]:
                            elbow_danger_x.append(row['회차'])
                            elbow_danger_y.append(row['elbow_Torque'])
                            elbow_danger = True
                        elif row['elbow_Torque'] > elbow_torque_danger[1]:
                            elbow_very_danger_x.append(row['회차'])
                            elbow_very_danger_y.append(row['elbow_Torque'])
                            elbow_very_danger = True

                        if row['shoulder_Torque'] < shoulder_torque_danger:
                            shoulder_danger_x.append(row['회차'])
                            shoulder_danger_y.append(row['shoulder_Torque'])
                            shoulder_danger = True

                        if elbow_danger and shoulder_danger:
                            warning_pitches.append(int(row['회차']))

                        if elbow_very_danger and shoulder_danger:
                            dangerous_pitches.append(int(row['회차']))

                        # 그래프 업데이트
                        fig.data[0].x = elbow_x
                        fig.data[0].y = elbow_y
                        fig.data[1].x = shoulder_x
                        fig.data[1].y = shoulder_y
                        fig.data[2].x = elbow_danger_x
                        fig.data[2].y = elbow_danger_y
                        fig.data[3].x = elbow_very_danger_x
                        fig.data[3].y = elbow_very_danger_y
                        fig.data[4].x = shoulder_danger_x
                        fig.data[4].y = shoulder_danger_y
                        
                        chart.plotly_chart(fig)
                        status_text.text(f"{i+1}/{len(mht)} rows processed.")
                        progress_bar.progress((i+1)/len(mht))
                    
                        # 0.5초 간격 설정
                        time.sleep(0.25)
                    
                    progress_bar.empty()
                    for pitch in warning_pitches + dangerous_pitches:
                        st.warning(f"{pitch}번째 투구에서 위험 요소 탐지")

                        # 첫 번째 위험한 투구를 바로 보여주기
                        if pitch == 1:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\minho1.mp4')
                            with col402: 
                                st.video('pitch_videos\\minho1_dotted.mp4')
                        elif pitch == 2:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\minho2.mp4')
                            with col404:
                                st.video('pitch_videos\\minho2_dotted.mp4')
                        elif pitch == 3:
                            col405, col406 = st.columns(2)
                            with col405:
                                st.video('pitch_videos\\minho3.mp4')
                            with col406:
                                st.video('pitch_videos\\minho3_dotted.mp4')
                        elif pitch == 4:
                            col407, col408 = st.columns(2)
                            with col407:
                                st.video('pitch_videos\\minho4.mp4')
                            with col408:
                                st.video('pitch_videos\\minho4_dotted.mp4')
                        elif pitch == 5:
                            col409, col410 = st.columns(2)
                            with col409:
                                st.video('pitch_videos\\minho5.mp4')
                            with col410:
                                st.video('pitch_videos\\minho5_dotted.mp4')
                        elif pitch == 6:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\minho6.mp4')
                            with col402: 
                                st.video('pitch_videos\\minho6_dotted.mp4')
                        elif pitch == 15:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\minho7.mp4')
                            with col404:
                                st.video('pitch_videos\\minho7_dotted.mp4')
                    if not warning_pitches and not dangerous_pitches:
                        st.info("위험 투구 미발견")
        with tab3:
            st.subheader('투구 분석')

            selected_pitch = st.selectbox('투구를 선택하세요', [str(x) + '구' for x in range(1, 21)])
            selected_pitch_num = int(selected_pitch.replace('구', ''))

            if selected_pitch_num == 1:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\minho1.mp4') 
                with col402: 
                    st.video('pitch_videos\\minho1_dotted.mp4')
            elif selected_pitch_num == 2:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\minho2.mp4')
                with col404:
                    st.video('pitch_videos\\minho2_dotted.mp4')
            elif selected_pitch_num == 3:
                col405, col406 = st.columns(2)
                with col405:
                    st.video('pitch_videos\\minho3.mp4')
                with col406:
                    st.video('pitch_videos\\minho3_dotted.mp4')
            elif selected_pitch_num == 4:  
                col407, col408 = st.columns(2)
                with col407:
                    st.video('pitch_videos\\minho4.mp4')
                with col408:
                    st.video('pitch_videos\\minho4_dotted.mp4')
            elif selected_pitch_num == 5:
                col409, col410 = st.columns(2)
                with col409:
                    st.video('pitch_videos\\minho5.mp4')
                with col410:
                    st.video('pitch_videos\\minho5_dotted.mp4')
            elif selected_pitch_num == 6:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\minho6.mp4')
                with col402: 
                    st.video('pitch_videos\\minho6_dotted.mp4')
            elif selected_pitch_num == 15:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\minho7.mp4')
                with col404:
                    st.video('pitch_videos\\minho7_dotted.mp4')              
    elif selected_page == '이정용':
        tab1, tab2, tab3= st.tabs(['선수 프로필', '부하 측정','전체 투구 영상'])
        with tab1:
            st.subheader("선수 기본 프로필")
            col301, col302 = st.columns(2)
            with col301:
                st.image('https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png', width=300)
            with col302:
                st.text("이름: 이정용")
                st.text("포지션: 투수")
                st.text("팀: LG 트윈스")
                st.text("생년월일: 1996년 3월 26일")
                st.text("신장/체중: 186cm/85kg")
            st.markdown('') # 이것도 볼드체로
            st.write('2023시즌')
            st.dataframe(df4, width=1000)
            st.markdown("   ")
            st.subheader("최근 부상 이력")
            col303, col304, col305 = st.columns(3)

            with col303:
                #st.image('body/어깨원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%96%B4%EA%B9%A8%EC%9B%90.png">'
                            '<br>'
                            '<strong>Shoulder</strong> | May 1<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">15 days</span>'
                            '</div>', unsafe_allow_html=True)

                
            with col304:
                #st.image('body/이두원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%EC%9D%B4%EB%91%90%EC%9B%90.png">'
                            '<br>'
                            '<strong>Biceps</strong> | April 17<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">10 days</span>'
                            '</div>', unsafe_allow_html=True)

            with col305:
                #st.image('body/허리원.png')
                st.markdown('<div style="text-align: center;">'
                            '<img src="https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/body/%ED%97%88%EB%A6%AC%EC%9B%90.png">'
                            '<br>'
                            '<strong>Oblique</strong> | Feb 4<br>'
                            '<span style="color: gray; display: inline-block; border-radius: 20px; background-color: lightgray; padding: 5px;">30 days</span>'
                            '</div>', unsafe_allow_html=True)
            st.markdown(' ')
            st.subheader('주의해야할 부상 Top 3')
            st.text('나와 비슷한 부상 이력을 가진 선수의 패턴이에요.')
            col306, col307, col308 = st.columns(3)
            with col306:
                st.markdown('<div style="background-color: #be0737; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format('팔꿈치 통증'), unsafe_allow_html=True)
            with col307:
                st.markdown('<div style="background-color: #d8445f; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_young.index[1]), unsafe_allow_html=True)
            with col308:
                st.markdown('<div style="background-color: #f0597a; padding: 10px; border-radius: 5px; text-align: center;">{}</div>'.format(injury_list_young.index[2]), unsafe_allow_html=True)
            st.markdown(' ')
            options = ['팔꿈치 통증', injury_list_young.index[1], injury_list_young.index[2]]
            selected_option = st.selectbox("부상명을 선택하세요:", options)
            if selected_option == options[0]:  # injury_list_young.index[0]
                video_file = open("treatment_videos\\tenniselbow2.mp4", 'rb')
            elif selected_option == options[1]:  # injury_list_young.index[1]
                video_file = open("treatment_videos\\sideflank.mp4", 'rb')
            elif selected_option == options[2]:  # injury_list_young.index[2]
                video_file = open("treatment_videos\\biceps.mp4", 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, format='mp4')

        with tab2:
            st.subheader('투구 분석')
            jwt = pd.read_csv('torque/jwtorque.csv')
            if st.button("부하 측정"):                    
                    # Streamlit 구성
                    st.markdown("<h1 style='text-align: center; color: white;'>투구별 토크 측정</h1>", unsafe_allow_html=True)
                    progress_bar = st.sidebar.progress(0)
                    status_text = st.sidebar.empty()
                    chart = st.empty()
            
                    # 위험 범위 정의
                    elbow_torque_danger = [105, 119]
                    shoulder_torque_danger = 25

                    
                    st.markdown("""
                    <table>
                        <tr>
                            <th style='text-align: left; background-color: #606770'>위험 유형</th>
                            <th style='text-align: left; background-color: #606770'>기준</th>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 고위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 119 이상일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>팔꿈치 토크 위험</td>
                            <td style='text-align: left;'>팔꿈치 토크가 105 이상 119 이하일 때</td>
                        </tr>
                        <tr>
                            <td style='text-align: left;'>어깨 토크 저위험</td>
                            <td style='text-align: left;'>어깨 토크가 25 미만일 때</td>
                        </tr>
                    </table>
                    <br>
                    """, unsafe_allow_html=True)
            
                    # 위험한 투구를 추적하는 리스트
                    dangerous_pitches = []
                    warning_pitches = []

                    # 그래프 및 데이터 초기 설정
                    fig = go.Figure()
                    elbow_x, elbow_y = [], []
                    shoulder_x, shoulder_y = [], []
                    elbow_danger_x, elbow_danger_y = [], []
                    elbow_very_danger_x, elbow_very_danger_y = [], []
                    shoulder_danger_x, shoulder_danger_y = [], []
            
                    # 처음에 선 그래프를 그립니다
                    fig.add_trace(go.Scatter(x=elbow_x, y=elbow_y, mode='lines', name='팔꿈치 토크'))
                    fig.add_trace(go.Scatter(x=shoulder_x, y=shoulder_y, mode='lines', name='어깨 토크'))
            
                    # 위험 점 추가
                    fig.add_trace(go.Scatter(x=elbow_danger_x, y=elbow_danger_y, mode='markers', marker=dict(color='yellow'), name='팔꿈치 토크 높음'))
                    fig.add_trace(go.Scatter(x=elbow_very_danger_x, y=elbow_very_danger_y, mode='markers', marker=dict(color='red'), name='팔꿈치 토크 매우 높음'))
                    fig.add_trace(go.Scatter(x=shoulder_danger_x, y=shoulder_danger_y, mode='markers', marker=dict(color='orange'), name='어깨 토크 낮음'))
            
                    for i in range(len(jwt)):
                        # 데이터프레임 행 단위 추가
                        row = jwt.iloc[i]
                    
                        # 데이터 업데이트
                        elbow_x.append(row['회차'])
                        elbow_y.append(row['elbow_Torque'])
                        shoulder_x.append(row['회차'])
                        shoulder_y.append(row['shoulder_Torque'])
            
                        # 위험 점 표시
                        elbow_danger = False
                        elbow_very_danger = False
                        shoulder_danger = False

                        if row['elbow_Torque'] >= elbow_torque_danger[0] and row['elbow_Torque'] <= elbow_torque_danger[1]:
                            elbow_danger_x.append(row['회차'])
                            elbow_danger_y.append(row['elbow_Torque'])
                            elbow_danger = True
                        elif row['elbow_Torque'] > elbow_torque_danger[1]:
                            elbow_very_danger_x.append(row['회차'])
                            elbow_very_danger_y.append(row['elbow_Torque'])
                            elbow_very_danger = True

                        if row['shoulder_Torque'] < shoulder_torque_danger:
                            shoulder_danger_x.append(row['회차'])
                            shoulder_danger_y.append(row['shoulder_Torque'])
                            shoulder_danger = True

                        if elbow_danger and shoulder_danger:
                            warning_pitches.append(int(row['회차']))

                        if elbow_very_danger and shoulder_danger:
                            dangerous_pitches.append(int(row['회차']))

                        # 그래프 업데이트
                        fig.data[0].x = elbow_x
                        fig.data[0].y = elbow_y
                        fig.data[1].x = shoulder_x
                        fig.data[1].y = shoulder_y
                        fig.data[2].x = elbow_danger_x
                        fig.data[2].y = elbow_danger_y
                        fig.data[3].x = elbow_very_danger_x
                        fig.data[3].y = elbow_very_danger_y
                        fig.data[4].x = shoulder_danger_x
                        fig.data[4].y = shoulder_danger_y
                        
                        chart.plotly_chart(fig)
                        status_text.text(f"{i+1}/{len(jwt)} rows processed.")
                        progress_bar.progress((i+1)/len(jwt))
                    
                        # 0.5초 간격 설정
                        time.sleep(0.25)
                    
                    progress_bar.empty()
                    for pitch in warning_pitches + dangerous_pitches:
                        st.warning(f"{pitch}번째 투구에서 위험 요소 탐지")

                        # 첫 번째 위험한 투구를 바로 보여주기
                        if pitch == 1:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\yong1.mp4')
                            with col402: 
                                st.video('pitch_videos\\yong1_dotted.mp4')
                        elif pitch == 2:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\yong2.mp4')
                            with col404:
                                st.video('pitch_videos\\yong2_dotted.mp4')
                        elif pitch == 3:
                            col405, col406 = st.columns(2)
                            with col405:
                                st.video('pitch_videos\\yong3.mp4')
                            with col406:
                                st.video('pitch_videos\\yong3_dotted.mp4')
                        elif pitch == 4:
                            col407, col408 = st.columns(2)
                            with col407:
                                st.video('pitch_videos\\yong4.mp4')
                            with col408:
                                st.video('pitch_videos\\yong4_dotted.mp4')
                        elif pitch == 5:
                            col409, col410 = st.columns(2)
                            with col409:
                                st.video('pitch_videos\\yong5.mp4')
                            with col410:
                                st.video('pitch_videos\\yong5_dotted.mp4')
                        elif pitch == 6:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\yong6.mp4')
                            with col402: 
                                st.video('pitch_videos\\yong6_dotted.mp4')
                        elif pitch == 7:
                            col403, col404 = st.columns(2)
                            with col403:
                                st.video('pitch_videos\\yong7.mp4')
                            with col404:
                                st.video('pitch_videos\\yong7_dotted.mp4')
                        elif pitch == 8:
                            col405, col406 = st.columns(2)
                            with col405:
                                st.video('pitch_videos\\yong8.mp4')
                            with col406:
                                st.video('pitch_videos\\yong8_dotted.mp4')
                        elif pitch == 9:
                            col407, col408 = st.columns(2)
                            with col407:
                                st.video('pitch_videos\\yong9.mp4')
                            with col408:
                                st.video('pitch_videos\\yong9_dotted.mp4')
                        elif pitch == 10:
                            col409, col410 = st.columns(2)
                            with col409:
                                st.video('pitch_videos\\yong10.mp4')
                            with col410:
                                st.video('pitch_videos\\yong10_dotted.mp4')
                        elif pitch == 11:
                            col401, col402 = st.columns(2)
                            with col401:
                                st.video('pitch_videos\\yong11.mp4')
                            with col402:
                                st.video('pitch_videos\\yong11_dotted.mp4')
                    if not warning_pitches and not dangerous_pitches:
                        st.info("위험 투구 미발견")
        with tab3:
            st.subheader('투구 분석')

            selected_pitch = st.selectbox('투구를 선택하세요', [str(x) + '구' for x in range(1, 21)])
            selected_pitch_num = int(selected_pitch.replace('구', ''))

            if selected_pitch_num == 1:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\yong1.mp4')
                with col402:
                    st.video('pitch_videos\\yong1_dotted.mp4')
            elif selected_pitch_num == 2:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\yong2.mp4')
                with col404:
                    st.video('pitch_videos\\yong2_dotted.mp4')
            elif selected_pitch_num == 3:
                col405, col406 = st.columns(2)
                with col405:
                    st.video('pitch_videos\\yong3.mp4')
                with col406:
                    st.video('pitch_videos\\yong3_dotted.mp4')
            elif selected_pitch_num == 4:
                col407, col408 = st.columns(2)
                with col407:
                    st.video('pitch_videos\\yong4.mp4')
                with col408:
                    st.video('pitch_videos\\yong4_dotted.mp4')
            elif selected_pitch_num == 5:
                col409, col410 = st.columns(2)
                with col409:
                    st.video('pitch_videos\\yong5.mp4')
                with col410:
                    st.video('pitch_videos\\yong5_dotted.mp4')
            elif selected_pitch_num == 6:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\yong6.mp4')
                with col402:
                    st.video('pitch_videos\\yong6_dotted.mp4')
            elif selected_pitch_num == 7:
                col403, col404 = st.columns(2)
                with col403:
                    st.video('pitch_videos\\yong7.mp4')
                with col404:
                    st.video('pitch_videos\\yong7_dotted.mp4')
            elif selected_pitch_num == 8:
                col405, col406 = st.columns(2)
                with col405:
                    st.video('pitch_videos\\yong8.mp4')
                with col406:
                    st.video('pitch_videos\\yong8_dotted.mp4')
            elif selected_pitch_num == 9:
                col407, col408 = st.columns(2)
                with col407:
                    st.video('pitch_videos\\yong9.mp4')
                with col408:
                    st.video('pitch_videos\\yong9_dotted.mp4')
            elif selected_pitch_num == 10:
                col409, col410 = st.columns(2)
                with col409:
                    st.video('pitch_videos\\yong10.mp4')
                with col410:
                    st.video('pitch_videos\\yong10_dotted.mp4')
            elif selected_pitch_num == 11:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\yong11.mp4')
                with col402:
                    st.video('pitch_videos\\yong11_dotted.mp4')