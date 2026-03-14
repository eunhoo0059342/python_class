'''
데이터변환
int() float() str()
list()- join
dict()
tuple
set

<문자열 포맷팅>
: 문자열로 많이 읽고 쓰기 
: 문자열안에 원하는 값을 정확하게 넣고싶어요.


(1) f-string(완전 최신)
"문자열~~~ {변수} "


(2) % 포맷팅 (최초의 방식, C언어방식)
print("문자열 %기호1 %기호2" % (변수1,변수2))
- %s : 문자열
- %d : 정수
- %f : 실수
- %b : 2진수
- %x : 16진수

(3)str.format()
print(" {} {} {}".format(변수,변수2,변수3))
print(" {내부변수} {내부변수} {내부변수}".format(내부변수=변수,내부변수="값",변수3))


TIP) 자리수 맞추기(보통은 숫자)
- 자리수가 5자리
- 채울문자 0, -(띄어쓰기, 문자열할때 보통쓴다.)
%05d : 5자리수로 맞추고 비어있으면 9으로 채우기
"{:05d}".format()
f"{변수:05d}"

%05.2f : 5자리수로 맞추고 비어있으면 9으로 채우기
"{:05.2f}".format()
f"{변수:05.2f}"


'''
alpha = list('abcdefghijklmnop')

print(f"알파벳은 : { alpha }")
print("알파벳은 : ["+ ", ".join(alpha)+"]")


# 달(숫자), 날짜(숫자), 요일(문자)를 각각 변수에 담아서 문자열 포멧팅
month = 12
day = 13
date = 'SAT'
# 오늘날짜는 9월 13일 SAT 이다. 
print('오늘 날짜는 %05d월 %d일 %s이다' % (month, day, date))
print('오늘 날짜는 {:05d}월 {:-7.5d}일 {:5s}이다'.format(month,day,date))  # 순서대로 매핑
print('오늘 날짜는 {m}월 {day}일 {date}이다'.format(day=day,date="SUN",m="2")) # 변수이름으로 매핑







