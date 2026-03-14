
# <데이터타입>
# 1. 숫자 Number
# - 정수 int() / 실수 float()
# 2. 문자열 String ""
# - 중요한 특징 : 인덱스(0번부터 시작하는 ~ 숫자)
# - 인덱싱 : 문자열변수[인덱스] => 인덱스 번호로 특정 문자 뽑기
# - 슬라이싱 : 문자열변수[시작 : 끝] => 인덱스 번호로 시작번호부터 끝-1 까지의 문자 자르기
# - 문자열 주요 메서드
#   - .upper()
#   - .lower()
#   - .strip()
#   - .replace("찾는문자","바꿀문자")
# - len() 함수 : 문자열의 크기, 길이
# - 뒤집기 reverse
# - 정렬 sort => 엄청 중요한 개념 => 자료구조랑 알고리즘
# - .split("구분") : 문자열 => 리스트 변화

# 3. 리스트(혹은 다른 프로그래밍언어에서 배열 array, list)
# : 여러가지 데이터(요소)를 저장하는 데이터타입
# [요소, 요소, 요소]
# - 인덱스(순서)가 있다. => 인덱싱(하나씩 뽑기), 슬라이싱(시작~끝까지 자르기)



class8 = ["A", "B", "C", "D"]
# 예제) class8의 2번째 학생을 뽑아주세요. => 인덱싱
print(class8[1])
# 추가) 리스트 맨뒤에 추가하기 : 리스트.append("추가할 데이터")
# 예제) class8의 "E"를 추가하기
class8.append("E")
print(class8)

# 예제) class8의 1번째 "B"친구를 "F"바꿀수가 있어요.
# '=' 변수에서 저장하기(없으면 새로 만들고, 있으면 덮어쓰기,수정하기)
a = 10
print(a)
a = 9
print(a)
class8[1] = "F"
print(class8)

# 예제) 삭제 리스트.pop(인덱스)
class8.pop()
print(class8)



# ===================

class8 = ["A", "B", "C", "D"]
# 리스트의 모든 값을 뽑아보기

print(class8[0])
print(class8[1])
print(class8[2])
print(class8[3])



# 반복문 
# for문 : 횟수만큼 반복 시키겠다라

# for 반복변수 in 반복조건(횟수, 리스트, 튜플, 딕셔너리, 기타 등등) :
#     반복할 코드

# (1) 기본적으로 횟수로 반복하기
# range(n) : 0부터 n-1까지의 연속된 정수를 갖고 있는 데이터
# range(시작값, 끝값, 간격)
print(range(10)) # range(0, 10)



# for i in range(횟수):  # 0부터 9까지를 나오면서 반복하기
#     print(i)

# 연습) "해피 뉴이어"를 2025번? 출력해주세요~!
for i in range(2):
    # print("",,)
    print("해피 뉴이어",i)

# 연습) 11~30까지의 숫자를 출력해주세요.
# 반복문 만들때 체크해야하는것
# 1) 몇번 반복할건지
# 2) 반복변수에 어떤값이 들어가는지
for i in range(20):
    print(i+11)


class8 = ["A", "B", "C", "D","E","F","G","H"]
# print(class8[0])
# print(class8[1])
# print(class8[2])
# print(class8[3])

# 모조리 뽑을려면 출력 8번하기
# => 8번 반복해서 출력하면
for i in range(len(class8)):
    print(i)
    print(class8[i])



p = ['theater', 'police station', 'stock market', 'city hall', 'shopping mall', 'nuclear plant', 'university']
for i in range(len(p)):
    print(p[i])


# 조건문 : 
# 만약에 ~ 
# if 조건문 :
    # 조건이 만족할때 실행할 코드(만족안하면 실행 안함)
# elif 두번째 조건 :
    # 첫번째조건이 틀리면서 두번째조건이 맞을때 실행한다.
# elif 세번째 조건 :
# else: 
    # 모든 조건이 만족하지 않을때 실행

age = 13
# 만약에 17이상이라면 고등학생이다.
# 만약에 17미만 14이상이라면 중학생이다.
# 아니면 초등학생이다. 

if 17 <= age :
    print("고등학생이다")
elif age >= 14 :   # 17> age >= 14 
    print("중학생이다")
else:
    print("초등학생이다")
print("끝")



# 예제) 0~19까지의 숫자중에서 10보다 큰 수만 출력해라.
# (1) 0~19까지의 숫자 출력하기 => 반복문
for i in range(20):
    # (2) 그중에서 i가 10보다 큰 숫자 찾기 => 조건문
    if 10 < i:
        print(i)


# 조심해야할것) 반복변수(i)를 함부로 변경하지 않습니다.

# 과제1) 1~100까지 의 숫자를 출력해보기
for i in range(100):
    a = i + 1
    print(i)

# 과제2) 1~100까지의 숫자를 중에서 짝수만 출력해보기
for i in range(100):
    a = i + 1
    if i % 2 == 0 :    
        print(i)


