# 공공데이터 .csv를 가져와서 그래프를 그렸다.

# 보통 데이터관리는 엑셀 => 표 형태
# 엑셀 간략버전으로 칸구분 -> ,구분으로 바꿔서 저장한 타입 csv파일

# (1) Pandas 모듈삽입 import pandas as pd
import pandas as pd

# (2) test2.csv 파일읽기
# 변수 = pd.read_csv("파일경로")
# - 절대경로 : 절대 위치 /를 기준으로 
# - 상대경로 : 현재파일을 기준으로 ./

# (3) Pandas의 데이터구조 = DataFrame(약어 df) (표, table)
# 헤더 : 컬럼명
# 행 : 각각의 데이터
test_file = pd.read_csv("./data/test2.csv")

print(type(test_file)) # <class 'pandas.core.frame.DataFrame'>
print(test_file)
print()
# (4) 구역 컬럼값을 모두 뽑아보기
# df['컬럼명']
print(test_file['구역'])
print()
# (5) 범죄율 계산을 위해서 '인구','범죄' 여러개의 컬럼을 동시에 뽑아보기
# df[[컬럼명리스트]]
print(test_file[['인구', '범죄', '구역']])
print()
# (6) 범죄율 = 범죄/인구 계산해보기 
# df[새로운컬럼명]=새로운 df
# df끼리는 +,-,*,/ 사칙연산이 가능하다.
test_file['범죄율'] = test_file['범죄'] / test_file['인구']
print(test_file)
print()
# (7) 범죄율이 제일 높은순으로 df를 내림차순 정렬하기
# 변수 = df.sort_values("컬럼명",asceding=True/False)  #asceding오름차순 설정
sorted_t_file = test_file.sort_values('범죄율', ascending=False)
print(sorted_t_file)
print()

# (8) head 상위 1개만 뽑겠다.
# df.head(갯수) # 안쓰면 기본 5개
# df.tail(갯수) # 안쓰면 기본 5개
print(sorted_t_file.head(1))
print(sorted_t_file.tail(2))

# (9) 상위1번째의 구역이름
print(sorted_t_file.head(1)['구역'])