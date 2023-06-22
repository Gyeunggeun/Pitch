import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def elbow_max_torque():
    #공식을 위해 필요한 계산식 우선 계산 (M=86kg 으로 가정)
    M=86+0.145
    COM= (M*0.0162)*(0.2689*0.4574) / M*0.0162
    
    #r의 값이 3가지라서 비슷한값을얻기위해 3가지경우 모두 고려
    r1,r2,r3=0.276,0.265,0.121
    
    # I_forarm_1=(M*0.0162)*(0.2689*r1)**2 #회전 방향 기준
    # I_forarm_2=(M*0.0162)*(0.2689*r2)**2 #단면 기준
    I_forarm_3=(M*0.0162)*(0.2689*r3)**2 # 길이방향기준이라서 팔꿈치의 I= i_3로 체택
