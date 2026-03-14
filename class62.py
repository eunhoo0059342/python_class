# crime.csv 파일을 읽어서 최근 가장 많이 증가한 범죄유형을 찾아보기
# - pd.read_csv("파일경로")

# 그래프로 확인해보면 좋지 않을까?
# 선그래프 그리기
# 가로 연도수
# 세로 발생수
# 5종류의 선을 그려보기
# import matplotblib.pyplot as plt


from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

crime = pd.read_csv("./data/crime.csv")
print(crime)
# 판다스의 dataframe에서 연도 컬럼만 뽑기 
# - df['컬럼명'] : 딕셔너리 비슷하게 컬럼명으로 뽑기
# - df.loc[행기준,'컬럼명'] :특정 행과 열에 대해서 접근할수가 있습니다.
x = crime["연도"]
print(x)
y1 = crime["강도"]
y2 = crime["절도"]
y3 = crime["사기"]
y4 = crime["테러"]
y5 = crime["폭행"]

# 선그래프
# plt.plot(x,y,label="") 
# plt.show()
plt.plot(x, y1, label='robber')
plt.plot(x, y2, label='theft')
plt.plot(x, y3, label="fraud")
plt.plot(x, y4, label="terror")
plt.plot(x, y5, label="assault")

# 범례 plt.legend()
plt.legend()

plt.show()