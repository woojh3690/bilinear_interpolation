#다음 사이트를 참고하여 구현함
#https://darkpgmr.tistory.com/117

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
#%matplotlib inline 주피터 노트북에서만 쓰는 라인 (그래프를 창 안에서 바로 보여주는 기능)
from numpy.random import randn

#이미지 출력 함수 input 값은 dataFrame
def draw(data):
    plt.rc('figure', figsize=(12, 12)) #이미지 출력 크기 조절
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data['xi'], data['yi'], data['zi'], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

split = 3 #가로 세로 몇개로 나눌 것인지 설정

# 직사각형 점 4개의 3차원 좌표 설정
columns = ['xi', 'yi', 'zi']
index = ['A', 'B', 'C', 'D']
data = [[0, 0, 4], #A
        [0, 3, 5], #B
        [3, 3, 8], #C
        [3, 0, 1]] #D

# pandas dataFrame 객체로 데이터 변환
i = pd.DataFrame(data, columns=columns, index=index)


draw(i)

#선형보간 알고리즘
def bilinear_interpolation(z, alpha, beta, p, q):
    M = beta * z[0] + alpha * z[1]
    N = beta * z[3] + alpha * z[2]
    return q * M + p * N

a = np.zeros((split + 1, split + 1)) # 결과를 저장하는 2차원 배열을 4 * 4로 초기화 (z값만 격자로 확인하는 용도)
result_df = pd.DataFrame(columns=columns)

for x in range(split + 1):
    for y in range(split + 1):
        alpha = y / split
        beta = 1 - alpha
        p = x / split
        q = 1 - p

        result_z = bilinear_interpolation(i['zi'], alpha, beta, p, q)
        a[x, y] = result_z
        result_df.loc[len(result_df)] = [x, y, result_z]
print(a) #선형보간된 z값만 2차원 배열로 출력
print(result_df) #선형보간된 결과값 텍스트로 출력
draw(result_df) #선형보간된 결과값 그리기