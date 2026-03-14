# datetime모듈 시간이랑 날짜를 모듈
# pytz 모듈 # pip install pytz
import datetime
from pytz import timezone
# 현재 로컬 컴퓨터에서 설정된 날짜와 시간을 가져올수가 있다.
# (1) datetime.datetime.now()
# YYYY-mm-dd HH:MM:S
time = datetime.datetime.now()
print(time)

# (2)날짜와 시간 포맷을 변경하기
# 포맷코드 %코드명
# 년도 Y 달 m 일 d 시간 H 분 M 초 S AM/PM %p 요일 %a
# 시간.strftime("%Y-%m-%d %H:%M:%S")
# ~년 ~월 ~일 ~시 ~분 ~초
print(time.strftime("%Y년%m월%d일(%a)  %H시%M분%S초 %p"))


# (3)날짜 지정하기
# 모듈이름.클래스명
# datetime.datetime(년도,월,일,시,분,초)
time2 = datetime.datetime(2025, 6, 14, 10, 17, 10)

# (4)요일을 찾는 메서드 weekday() -> 0:월~5:토요일 6:일
# 요일을 한국어로 표현해주기
date_lst =['월요일', '화요일', '수요일','목요일', '금요일', '토요일', '일요일']
print(date_lst[time2.weekday()])


# 인스턴스.tzinfo
# None : 로컬
# - 인스턴스.astimezone(timezone("America/New_York"))
# Aisa/Seoul
# print(time.tzinfo)
# print(time.astimezone(timezone("America/New_York")))
# print(time)


# (5)날짜간의 계산 
# 시험 기간 날짜인스턴스를 생성 
today = datetime.datetime(2025,6,14)
exam_date = datetime.datetime(2025, 6, 30)
# 시험기간 - 오늘날짜 
print((exam_date - today).days)



# (6) 100일 후의 날짜를 계산하기
# datime.timedelta : 시간혹은 날짜의 차이계산
# 오늘 기준에서 + datime.timedelta(날짜)
print(time + datetime.timedelta(100))

# https://meet.google.com/wqu-ofee-sva
