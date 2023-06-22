import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#선수 기본정보 csv 파일 읽어오기
binfo = pd.read_csv('baseinfo.csv')
# 선수 이름을 설정합니다
player_name = '이민호'
# 해당 선수의 체중 정보를 가져옵니다
player_weight = binfo[binfo['이름'] == player_name]['체중'].values[0]

def elbow_max_torque():
    #공식을 위해 필요한 계산식 우선 계산
    M=player_weight+0.145
    COM= (M*0.0162)*(0.2689*0.4574) / M*0.0162

    #r의 값이 3가지라서 비슷한값을얻기위해 3가지경우 모두 고려
    r1,r2,r3=0.276,0.265,0.121

    I_forarm_3=(M*0.0162)*(0.2689*r3)**2 # 길이방향기준이라서 팔꿈치의 I= i_3로 체택

    #20회 동안의 MAX토크 데이터 저장
    no_=[str(i) for i in range(1,21)]
    tq=[]
    # 이민호 예시 = 4구 사용
    df=pd.read_csv(f'torque/elbow_torque/4_팔꿈치.csv')
    x_vel=[0]
    y_vel=[0]
    z_vel=[0]
    x_acc=[0,0]
    y_acc=[0,0]
    z_acc=[0,0]

    phi_vel=[0]
    theta_vel=[0]
    psi_vel=[0]
    phi_acc=[0,0]
    theta_acc=[0,0]
    psi_acc=[0,0]

    #토크값 계산후 넣을 리스트(절대값과 일반 둘 다)
    tq_z=[]
    tq_z_abs=[]

    # 좌표값, 각도값을 바탕으로 속도를 구하는 부분
    for i in range(1,df.shape[0]):
        x_vel.append((df['x'][i]-df['x'][i-1])/(df['time'][i]-df['time'][i-1]))
        y_vel.append((df['y'][i]-df['y'][i-1])/(df['time'][i]-df['time'][i-1]))
        z_vel.append((df['z'][i]-df['z'][i-1])/(df['time'][i]-df['time'][i-1]))
        phi_vel.append((df['phi'][i]-df['phi'][i-1])/(df['time'][i]-df['time'][i-1]))
        theta_vel.append((df['theta'][i]-df['theta'][i-1])/(df['time'][i]-df['time'][i-1]))
        psi_vel.append((df['psi'][i]-df['psi'][i-1])/(df['time'][i]-df['time'][i-1]))

    df['x_vel']=x_vel
    df['y_vel']=y_vel
    df['z_vel']=z_vel
    df['phi_vel']=phi_vel
    df['theta_vel']=theta_vel
    df['psi_vel']=psi_vel

    # 좌표값, 각도값을 바탕으로 가속도를 구하는 부분
    for i in range(2,df.shape[0]):
        x_acc.append((df['x_vel'][i]-df['x_vel'][i-1])/(df['time'][i]-df['time'][i-1]))
        y_acc.append((df['y_vel'][i]-df['y_vel'][i-1])/(df['time'][i]-df['time'][i-1]))
        z_acc.append((df['z_vel'][i]-df['z_vel'][i-1])/(df['time'][i]-df['time'][i-1]))
        phi_acc.append((df['phi_vel'][i]-df['phi_vel'][i-1])/(df['time'][i]-df['time'][i-1]))
        theta_acc.append((df['theta_vel'][i]-df['theta_vel'][i-1])/(df['time'][i]-df['time'][i-1]))
        psi_acc.append((df['psi_vel'][i]-df['psi_vel'][i-1])/(df['time'][i]-df['time'][i-1]))

    df['x_acc']=x_acc
    df['y_acc']=y_acc
    df['z_acc']=z_acc
    df['phi_acc']=phi_acc
    df['theta_acc']=theta_acc
    df['psi_acc']=psi_acc

    for i in range(df.shape[0]):
        a_elbow=y_acc[i]-psi_acc[i]*0.2689-psi_vel[i]*(psi_vel[i]*0.2689)-9.81 #팔꿈치부분에 부착했기때문에 축이 psi기준이다. 던질때 y방향으로 가장 빠르게 이동한다
        a_com=a_elbow+COM*(psi_acc[i]*0.2689)+psi_vel[i]*COM*(psi_vel[i]*0.2689)

        temp3=I_forarm_3 * psi_acc[i]+COM*(M*0.0162*a_com-M*0.0162*9.81)
        tq_z.append(-temp3*6) # 선수데이터가 아니고, 던질때 센서가 확실히 고정되있지않아서 논문의 값 40~60사이값을 얻기 위해 보정
        tq_z_abs.append(abs(temp3*6)) # 절대값을 통해 던지는 최대토크를 계산함. 보정치6

    df['tq_z']=tq_z
    df['tq_z_abs']=tq_z_abs
    tq.append(round((df['tq_z_abs'].max()),1))

    #이상치 처리 84 이하 median값으로 보정  0=안전, 1=주의 2=위험
    tq_e=pd.DataFrame(no_,columns=['회차'])
    tq_e['elbow_Torque']=tq
    tq_e.loc[tq_e['elbow_Torque']<84,['elbow_Torque']]=tq_e['elbow_Torque'].median()
    tq_e['팔꿈치_부상위험']=0
    tq_e.loc[tq_e['elbow_Torque']<105,['팔꿈치_부상위험']]=0
    tq_e.loc[(tq_e['elbow_Torque']>=105)&(tq_e['elbow_Torque']<=119),['팔꿈치_부상위험']]=1
    tq_e.loc[tq_e['elbow_Torque']>119,['팔꿈치_부상위험']]=2

