'''
반복문 whlie문

=> (조건이 달성할때)까지 ~~~하겠다
while 조건:
    # 조건 Tip 한국말조건을 반대로 조건표현식에 만들어보자.   
    # 조건이 만족할때 실행할 코드


'''

# while True:
#     무한반복
#     : 다른거 절대 할수없는 상화이 생긴다. 아주 심각한 문제 발생

#     무한반복시 안쪽에 반드시 탈출하는 조건을 적어줘야한다.


# 카운트를 셋을때, 10이되면 반복을 탈출해라
# break : 반복문이라면 도중에 탈출이 가능하다.
count = 0
while True:
    # 탈출 조건
    count+=1
    print(count)
    if count >=10:
        print("탈출")
        break

num = [1,2,3,4,99,100,120]

# num대한 모든 값을 출력하기 단, 출력값이 100보다 큰 경우 그만둔다.
i = 0
while True:
    print(num[i])
    i += 1
    if num[i] > 100:
        break
##### for문
for i in range(len(num)):
    if num[i] > 100:
        print("탈출")
        break
    print(num[i])

# <반복문의 흐름 제어>
# 1. break : 반복을 탈출
# 2. continue : 반복을 건너뛰기 - 조건을 활용한 코드만 잘 적어도 대체 가능

num = [1,2,3,4,99,100,120]
# num대한 모든 값을 출력하기 단 50보다 크고 100보다 작은 경우 스킵

for i in range(len(num)):
    if num[i] > 50 and num[i] < 100:
        # 다음반복으로 넘어간다. 아래코드는 스킵한다.
        continue
    print(num[i])

#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?B3152DB88B6BA5CDEA73A994E3F239A2A55E

# key: 지점
# value :  key해당되는 점과 연결되는 지점 - 얼마나 걸리는가
route = {
    'a':{'b':1772,'c':5805,'f':5546,'h':730},
    'b':{'a':1772,'d':3010,'g':2562},
    'c':{'a':5805,'d':4111,'e':1081,'f':1621},
    'd':{'b':2010,'c':4111,'e':2892,'g':2908,'h':3092,'j':517},
    'e':{'c':1081,'d':2892,'f':4082,'i':506,'j':290},
    'f':{'a':5546,'c':1621,'e':4082,'i':627},
    'g':{'b':2562,'d':2908,'h':903},
    'h':{'a':730,'d':3092,'g':903,'j':3900},
    'i':{'f':627,'e':506},
    'j':{'d':517,'h':3900,'e':290}
}
# a 출발 - e까지 가고싶습니다.
# 실선 : 갈 수 있는 도로
# 점선 : 공사중이여서 갈수 없는 도로

print("mission 1 ============")
# rounte에서 점선에 해당되는 도록 제거
# [리스트 추가,수정,삭제]
# .append
# 변수[인덱스]= 새로운데이터: 새로운데이터로 수정
# .pop() : 맨뒤의 값을 뽑아서 삭제 / .pop(인덱스) : 해당 인덱스를 뽑아서 삭제

# [딕셔너리 추가,수정,삭제]
# 추가,수정 : = 활용 
# => 변수[key]=새로운데이터
# 삭제 .pop('key')  : 해당 key를 뽑아서 삭제

# 예제) route 'k' 값으로 "안녕하세요" 추가해보자 
route["k"] = "안녕하세요"
# print(route)
# 예제) route 'k' 값으로 "hello" 수정해보자 
route["k"] = "hello"
# print(route)
# 예제) route 'k' 값을 삭제하기
del_data = route.pop("k")
# print(route)
print(del_data)
# 힌트 : 빼고싶은값이 안쪽에 있는 딕셔너리이다.

route["f"].pop("e")
route["e"].pop("f")
route["f"].pop("c")
route["c"].pop("f")
route["c"].pop("d")
route["d"].pop("c")
route["h"].pop("j")
route["j"].pop("h")
route["d"].pop("h")
route["h"].pop("d")
print(route)
# route에서 점섬의 데이터를 삭제
# f-e, f-c, c-d, h-d, h-j







