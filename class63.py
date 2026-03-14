# cctv1 파일을 읽어서 
# 밤과 낮의 인구밀도가 가장 높은 세구역을 찾기

import pandas as pd
import matplotlib.pyplot as plt

cctv = pd.read_csv("./data/cctv1.csv")

# 06-12 : 6시 12시 
# 12_18 : 낮타임
# 18_24 : 밤타임

# 두 값의 평균을 새로운 컬럼으로 만들어서 비교를 해보기
# - 새컬럼  딕셔너리 처럼 df['새로운컬럼명'] = [새데이터] 
# - df 연산은 두 리스트의 합(100개) 아니고, 반복문없이 각 컬럼별 50개 연산
# cctv_n = cctv["n"]
# print(cctv['12_18'])
# print(cctv['18_24'])

print((cctv['12_18'] + cctv['18_24']) / 2)
cctv['average'] = (cctv['12_18'] + cctv['18_24']) / 2


# # 밤과 낮의 인구밀도가 가장 높은 세구역을 찾기
# 정렬하기 .sort_values(by="기준이름",asceding=True/False) 오름차순
cctv.sort_values(by="average", ascending=False)
# 상위 head(갯수) 3개 카메라 이름을
# 하위 tail(갯수)
# df-> 리스트 df.to_list()
print(cctv.head(3)["camera_name"].to_list())




# 과제) 직전 bfs/dfs를 혼자서 할수있는지
# - 미로탐색 https://www.acmicpc.net/problem/2178