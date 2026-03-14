# 선생님 코드
# matplotlib (https://matplotlib.org/)

# # matplotlib 설치
# pip install matplotlib
# # numpy : 다차원배열(리스트) 쉽게 처리하는 모듈
# pip install numpy
# # pandas : 표(관계형 레이블) 데이터를 직관적으로 다루기 쉽게 모듈
# pip install pandas

# 3.13 버전 설치
# python3 -m pip install matplotlib
# python3 -m pip install numpy

import matplotlib.pyplot as plt
import numpy as np


'''
선그래프 plot
markter = 'o'(원), 's'(사각형), '^'(삼각형), '*'(별)
color='색상'
linestyle='-'(실선), '--'(점선), '-.'(점-실선), ':'(점선)

'''
# 

x1=[10,11,12,13,14,15]
y1=[7,1,5,3,4,3]
x2=list(range(10,21,2))
y2=list(range(0,11,2))
x3=[10,11,12,13,14,15]
y3=list(range(0,16,3))

plt.plot(x1,y1, marker="o", color="red", linestyle="-", label="x1라벨")
plt.plot(x2,y2, marker="s", color="blue", linestyle="--", label="x2라벨")
plt.plot(x3,y3, marker="^", color="green", linestyle="-.", label="x3라벨")
plt.xlabel("x축라벨", loc="right")  # left center right
plt.ylabel("y축라벨", loc="top")    # top center bottom
plt.xlim(xmin=0) 
plt.ylim([0,20])
plt.gird(True, linestyle=":", alpha=0.5)
# plt.xticks(np.arange(0,15,0.1))
# plt.yticks(np.arange(0,20,0.1))
plt.title("차트타이틀",loc="center",pad=30)
plt.legend()
plt.show()


'''
막대그래프 bar
color= "배경색상"
width=0.5
edgecolor="테두리색상"
linewidth=테두리두께

과제) 공공데이터포털(https://www.data.go.kr/)


'''
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.show()

'''
산점도 점그래프 scatter

'''
x1=[10,11,12,13,14,15]
y1=[7,1,5,3,4,3]
x2=np.arange(0,20,1)
y2=x2**2
plt.scatter(x1,y1, s=[10,20,30,40,50,60], marker="*")
plt.scatter(x2,y2, s=x2*300, c=x2*300, alpha=0.5)
plt.show()


'''
원형차트 pie
labels : 각 조각의 이름 표시
autopct: 퍼센트 표시
- "%d%%" : 정수
- "%.1f%%" : 소수점 한자리
- "%.2f%%" : 소수점 둘째자리

labeldistance : 중심라벨 거리
- 테두리 1.0

wedgeprops = {"width":0.5}
explode: [1,0,0,0] 특정조각 강조0-1


'''

x=[12,25,13,34]
labels=["A","B","C","D"]
plt.pie(x,labels=labels, 
    autopct="%.2f%%", 
    labeldistance=0.7, 
    wedgeprops = {"width":0.3},
    explode= [0.1,0,0,0],
    shadow=True
    )
plt.show()


# matplotlib (https://matplotlib.org/stable/plot_types/index.html)
# 청소년 공공데이터분석
# (https://www.data.go.kr/)


import pandas as pd
# python3 -m pip install pandas

'''
(1)파일읽기
- 상대경로 : 현재 내파일을 기준으로 찾는 경로
(jupyter폴더안에 있는 파일 ./(내위치) -> data폴더안에 있는 csv파일을 찾을거기")
내 위치 ./
상위 위치 ../
자식 /자식이름

상위폴더(부모요소,조상)
 |  -------------------------|
폴더 jupyter(부모요소)                파일3(삼촌)data   
 | -------------------------|
내파일 (자식요소, 자손) ./        파일2(형제요소)
<형제찾기>
./파일2
<삼촌찾기> 상위로 한번 가기 ../
../파일3/자식

- 절대경로 : 프로젝트 최상위폴더(루트,root /)에서부터 시작합
"/자식/자식/자식"

'''
# - 경대경로 :

# pandas(데이터베이스, 표로된 데이터)로 파일 읽기
# - 파일읽어서 pandas로 관리하겠다.
# - 데이터프레임 : pandas 객체 이름 => 표table  (비슷한것로 이차원리스트 & 딕셔너리랑 섞여있는)
df = pd.read_csv("파일의 경로")
print(df)

# 데이터프레임의 컬럼명 
print(df.columns)
# 해당 컬럼에 해당되는 데이터 모두 뽑기
print(df[['도시명','이산화황측정값(ppm)']])

# 데이터프레임 중 1개의 행을 뽑기
# loc, iloc
# df.loc[0]

# 여러행 뽑기 
# 상위 5개 / 하위 5개 tail
print(df.head())

# 여러행 줄을 뽑고싶다.
df.loc[0:7,["도시명",'이산화황측정값']]


