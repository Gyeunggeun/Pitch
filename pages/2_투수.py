import streamlit as st
import streamlit.components.v1 as components

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
}

# 사이드바
pages = ['선수 목록'] + list(players.keys())
selected_page = st.sidebar.selectbox('페이지', pages)

# 선수 목록 페이지 구성
if selected_page == '선수 목록':
    st.title('선수 목록')
    player_list = list(players.keys())
    for i in range(0, len(player_list), 5): # 5*7 로 총 34명의 선수 이미지 표현
        columns = st.columns(5)
        for j in range(5):
            if i + j < len(player_list):
                player = player_list[i + j]
                with columns[j]:
                    image_url = players[player]
                    components.html(f'''
                        <center>
                            <img src="{image_url}" width="100%">
                            <p style="margin-top: 0px; color: white; font-size: 20px; font-weight: bold">{player}</p>
                        </center>
                    ''', height=350)
else:
    st.title(f'선수명: {selected_page}')
    # 선수의 세부 페이지에서 보여줄 정보를 검색하거나 계산
    # player_info = get_player_info(selected_page)  # 함수를 정의하여 선수 정보를 가져옴
    # 선수 정보를 표시하는 코드...


