import streamlit as st
import plotly.graph_objects as go
import streamlit.components.v1 as components
import time


def analyze_pitches(wst, video_mapping):
    if st.button("부하 측정"):                    
        # Streamlit 구성
        st.markdown("<h1 style='text-align: center; color: white;'>투구별 토크 측정</h1>", unsafe_allow_html=True)
        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        chart = st.empty()

        # 위험 범위 정의
        elbow_torque_danger = [105, 119]
        shoulder_torque_danger = 
        
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
                <td style='text-align: left;'>어깨 토크가 28 미만일 때</td>
            </tr>
        </table>
        <br>
        """, unsafe_allow_html=True)

        # 위험한 투구를 추적하는 리스트
        dangerous_pitches = []
        warning_pitches = 
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
            shoulder_danger = Fal
            if row['elbow_Torque'] >= elbow_torque_danger[0] and row['elbow_Torque'] <= elbow_torque_danger[1]:
                elbow_danger_x.append(row['회차'])
                elbow_danger_y.append(row['elbow_Torque'])
                elbow_danger = True
            elif row['elbow_Torque'] > elbow_torque_danger[1]:
                elbow_very_danger_x.append(row['회차'])
                elbow_very_danger_y.append(row['elbow_Torque'])
                elbow_very_danger = Tr
            if row['shoulder_Torque'] < shoulder_torque_danger:
                shoulder_danger_x.append(row['회차'])
                shoulder_danger_y.append(row['shoulder_Torque'])
                shoulder_danger = Tr
            if elbow_danger and shoulder_danger:
                warning_pitches.append(int(row['회차']
            if elbow_very_danger and shoulder_danger:
                dangerous_pitches.append(int(row['회차']
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
        if warning_pitches or dangerous_pitches:
            first_danger_pitch = min(warning_pitches + dangerous_pitches) if warning_pitches and dangerous_pitches else \
                min(warning_pitches) if warning_pitches else min(dangerous_pitches)
            st.warning(f"{first_danger_pitch}번째 투구에서 위험 요소 탐지")

            video_files = video_mapping[first_danger_pitch]  # 이 부분을 추가

            col1, col2 = st.columns(2)
            with col1:
                st.video(video_files[0]) 
            with col2: 
                st.video(video_files[1])
            # 첫 번째 위험한 투구를 바로 보여주기
            if first_danger_pitch == 1:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\woosuk_back.mp4') 
                with col402: 
                    st.video('pitch_videos\\woosuk_back_dotted.mp4')
            elif first_danger_pitch == 2:
                col403, col404 = st.columns(2)
                with col403:
                    st.image('0619/스켈레톤.png')
                with col404:
                    st.image('0619/원본.png')
            elif first_danger_pitch == 6:
                col401, col402 = st.columns(2)
                with col401:
                    st.video('pitch_videos\\woosuk_back.mp4')
                with col402: 
                    st.video('pitch_videos\\woosuk_back_dotted.mp4')
        else:
            st.info("위험 투구 미발견")
