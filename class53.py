'''
python 데이터타입 객체로 인식
- 내장메서드 : 해당 객체를 다루는 메서드

class 클래스이름:
    def __init__

    def 메서드1

<파이썬이 만든 메서드/함수>
- 내장 메서드 : 문자열.메서드이름()
- 내장 함수 : 함수이름(데이터) ex) len()

1. 숫자
+,-,*,/,//,%,**
round(숫자,자리수) : 반올림(소수점 자리수까지 반올림을 해서 만들기)
abs(숫자)        : 절대값

< math모듈 > (https://docs.python.org/ko/3.13/library/math.html)
math.sqrt(숫자) : 제곱근 숫자
math.ceil(숫자) : 올림
math.floor(숫자): 숫자
math.comb(n,k) : 경우의수 - 조합
maht.perb(n,k) : 경우의수 - 순열 => 팩토리얼
'''
num = -15.371234
print(type(num))
print(round(num, 2))
print(abs(num))
# 이항연산자 숫자 + 숫자
# 삼항연산자 (다른언어 조건 ? 참일때값 : 거짓일때값)
# 참일때값 if 조건 else 거짓일때값
print(num if num > 0 else num * -1)


'''
2. 문자열
<문자열 내장함수>
.upper()/.lower(): 대소문자
.capitalize() : 맨앞글자만 대문자로 변경
.title(): 단어별로 대문자
.swapcase() : 대문자 <-> 소문자

.replace("찾는문자","바꿀문자") : 찾아서 바꾸기

.find("찾는문자")       : 찾으면 인덱스를 알려주고, 없으면 -1를 출력한다.
.index("찾는문자")      : 찾으면 인덱스를 알려주고, 없으면 error     => 보통 리스트에서 사용
.count("찾는문자")      : 찾는 문자의 갯수를 알려주기

.split("구분인자")      : 구분인자 기준으로 잘라주기
"구분인자".join(리스트)   : 리스트에 구분인자를 추가해서 문자열로 합치기

.isalpha()            : 문자열에서 알파벳만 존재하는가?
.isdigit()/.isdecimal()/.isnumberic()  : 문자열에 숫자만 존재하는가?
(소수점,음수, 지수표기)(오로지 0-9까지)(로마표기법까지 ok)

.zfill(갯수) : 자리수에 맞추서 0으로 채우기
'''
text ="i lOVe python"
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# text에서 i를 삭제하고 싶어요.
print(text.replace("i", ""))
# text에서 js 찾아보기
print(text.find("js"))
# print(text.index("js"))

print("12".zfill(5))
print(f"{12:05d}")
'''
3. bool
0 "" [] {} () None => False


4. 리스트
<리스트 내장메서드>
.append(추가할값): 맨끝에 추가
.insert(인덱스, 추가할값) : 중간에 추가하기  <= 가급적이면 사용하지 말것
.pop() : 마지막값 삭제
.pop(인덱스) : 인덱스번째 값을 삭제         <= 가급적이면 사용하지 말것
.remove(삭제할 값) : 해당 값을 삭제        <= 가급적이면 사용하지 말것
del 리스트[인덱스]  : 리스트의 해당 값이 삭제 

.index("찾는요소")      : 찾으면 인덱스를 알려주고, 없으면 error     

.count("찾는요소")      : 찾는 요소의 갯수를 알려주기

<내장함수>
sum()
max()
min()
len()


# TODO: 정렬스타트
.sort() : 정렬(오름차순 정렬)



5. 딕셔너리
6. 튜플
7. 집합

'''


num = [1,2,3,4,5,6]

del num[2]
print(num)