# 전체적인 파이썬 내장 함수 점검
# - 프로그래밍 언어의 문법이랑 기타 내장함수 활용
# - 알고리즘

'''


(1) range(n) : 0~(n-1)까지 n개의 연속된 정수
- 타입: range
- 활용 : 반복문, 연속된 숫자 리스트 만들고싶을때
- 확장 : range(시작,끝) : 시작~ 끝-1 연속된 정수
        range(시작,끝,간격) : 시작~ 끝-1에서 간격만큼 연속된 정수


(2) 슬라이싱 [:끝]
           [시작:]
           [시작:끝]
           [시작:끝:간격] 

'''
print(range(10),type(range(10)))  # range(0,10)
print(list(range(10)))

print(list(range(1, 30, 3)))
# 결과 1 4 7 10 ... 

print("\nQ1. 결과로 출력된 값은?---------")
a = 0
for i in range(1, 30, 2):  # range(1,30,2):  1 3 5 7 9 11 13 ... 29 (15)
    for j in range(2, 20, 3): #  range(2, 20, 3) 2 5 8 11 14 17 (6개)
        a += 1
print(a)
print("------------------------------")

'''
(3) 반복문
- for   : 횟수반복
- while : 조건반복 

for 반복변수 in 반복조건(반복가능한 객체, iterable : str, list, tuple, range, set, dict )
    반복변수 = 반복객체의 요소값이 하나씩 들어가면서 반복

(3-1) 기본
    for i in range(횟수):
        # i = 0~(횟수-1) => 횟수만큼

(3-2) 리스트
- 인덱스,순서가 필요할때
    for i in range(len(리스트)):
        리스트[i]
- 값만 필요할때(인덱스 없이)
    for a in 리스트:
        a=리스트

(3-2) 딕셔너리
    for k, v in 딕셔너리.items():
        k, v

    for a in 딕셔너리
    TODO 딕셔너리에서 번호를 사용하는 방법 

'''

lst = ["a",100,'b','c','d']
for a in lst:
    print(a)
    # 리스트.index("찾는요소") : 리스트에서 인덱스 번호를 찾아는 함수
    print(lst.index(a))
for i in range(len(a)):
    print(lst[i])
    print(i)

text = "hello"
for a in text:
    print(a)


print("\n 2. 다음 프로그램의 실행 결과는 무엇인가?---------")
b = 0
for i in [1, 2, 3, 4, 5, 6, 7]: 
    if i % 2 == 1: # 2로 나눴을때 나머지가 1인수 (= 홀수)  
        b += i     # 홀수 4개 1+3+5+7 = 16
    if i % 3 == 1: # 3으로 나눴을때 나머지가 1인수 (=3의 배수+1)
        b -= i     # -(1+4+7) = -12
print(b)


d = {"apple":"사과", "banana":"바나나", "mango":"망고"}
# key만뽑기 - 리스트랑 유사 dict_keys(['apple', 'banana', 'mango'])
# value만뽑기 - 리스트 유사
# key,value둘다 뽑기 - (key,value) 리스트

print(d.items(),type(d.items()))
for data in [('apple', '사과'), ('banana', '바나나'), ('mango', '망고')]:
    print(data)
    k,v = data
    print(k,v)




# 과제 -> 아래코드의 결과값을 고민해보기 (실행 금지)
# a = 1
# i = 1
# while True:
#     if i > 10: 
#         break
#     i += 2
#     a *= 3 
# print(a)

# iterable : str, list, tuple, range, set, dict 

'''


<데이터타입>
---단일 데이터-----
1. 숫자
2. 문자열
3. bool타입
---다중 데이터(collection)----
4. 리스트
5. 딕셔너리
6. 튜플
7. 집합
    

iterable 객체
: 여러개가 존재하고, 하나씩 뽑을 수 있어야한다. => 순서를 가질 수 있어야한다.

- 여러개 존재가능한 데이터(collection data): list dict tuple set range
- 순서존재하는 데이터 : string list tuple range

<반복문>
for 반복변수 in 반복조건(반복가능한 객체 iterable 객체):
    # 반복할 내용

'''

# 딕셔너리.items() : 딕셔너리 -> 리스트화
# [('apple', '사과'), ('banana', '바나나'), ('mango', '망고')]

d =  {"apple":"사과", "banana":"바나나", "mango":"망고"}
print(d.items())
for k, v in d.items():
    print(k,v)


# 일반적으로 딕셔너리를 반복돌리면 key만 나오게됩니다. 
for a in d:
    print(a, d[a])


# enum : 열거형데이터
# enumerate(iterable, start=0)

alpha = list('abcdefghijklmnop')

for i,v in enumerate(alpha,start=100):
    print(i,v)




