'''
데이터타입
-------- 단일 데이터타입 ---------------
1. 숫자 타입 Number 123
2. 문자열 타입 String "",''
- .split() : 문자열=> 리스트 

3. 불린타입 boolean bool => True False
- 조건문
 
--------- 여러개를 처리하는 데이터타입  -----
4. 리스트 List [요소, 요소, 요소]
: 여러개의 데이터를 저장하는 데이터타입
- 추가(.append), 수정('='), 삭제(pop)
- "".join(리스트) : 리스트 => 문자열
- 내부리스트가 있는 이차원리스트 [[],[],[],[]]
- 인덱스 번호: 어떤 요소를 가져오고싶을때, 번호를 사용해서 불렀다.

오늘은 새로운 데이터타입
5. 딕셔너리(dictionary, 사전) {"key"(숫자,문자) : value(데이터타입), key:value, key:value }
- 찾을때, "문자"로 찾는 데이터타입을 딕셔너리라고한다.
- key-value 형태
- 순서가 없다. (=인덱스가 없다.)
- 딕셔너리타입은 파이썬에만 존재하는 특별한 데이터타입(=json)

'''
# (key): (value)
# ＊ID: agent@nis.com
# ＊PW: python
# phone: 010-1234-5678
answer = {"ID": "agent@nis.com", "PW": "python", "phone": "010-1234-5678"}
# (1) 딕셔너리 요소에 접근
# - 인덱스 대신에 key로 요소를 부를것이다.
# (리스트에서)   리스트변수[인덱스]
# (딕셔너리에서) 딕셔너리변수[key] => 해당 key대한 value가 나온다. 
print(answer["ID"])
# answer.get("ID")

# (2) 딕셔너리에 값을 추가하기 
# - 리스트변수.함수() : 메서드  해당 데이터타입에서만 사용이 가능하다
# .append로는 추가가 불가능하다(리스트에서만 가능하다)
# 딕셔너리변수["정하는 Key"]="value"

# 예제) answer에다가 birth: "01-25" 데이터를 추가해주세요.
answer["birth"]="01-25"
print(answer)

print("mission 1 ============")
# 로그데이터의 "종류"(type)가 "거래"인것을 찾아봐라

# log = 리스트타입 - 리스트안에 딕셔너리가 있는 데이터타입
log = [
    {'time':'1014','ip':'89.149.233.0','type':'trade','item':'wiz asset','price':40000,'id':'502yo4'},
{'time':'1016','ip':'89.149.233.1','type':'download','item':'None','price':0,'id':'rtw1517'},
{'time':'1305','ip':'89.149.233.3','type':'trade','item':'star asset','price':10000,'id':'eop00'},
{'time':'1315','ip':'89.149.233.6','type':'trade','item':'q energy','price':10000,'id':'versit808'},
{'time':'1253','ip':'89.149.233.9','type':'trade','item':'ms ent','price':2700,'id':'vsf7'},
{'time':'1400','ip':'89.149.233.12','type':'trade','item':'wiz asset','price':10000,'id':'ge3298'},
{'time':'1253','ip':'89.149.233.10','type':'trade','item':'ms ent','price':2700,'id':'hdus8'},
{'time':'1253','ip':'89.149.233.17','type':'trade','item':'ms ent','price':2700,'id':'tau200'},
{'time':'1508','ip':'89.149.233.20','type':'trade','item':'wiz asset','price':45000,'id':'haha160'},
{'time':'1510','ip':'89.149.233.26','type':'download','item':'None','price':0,'id':'bus328'},
{'time':'1500','ip':'89.149.233.30','type':'trade','item':'wiz asset','price':5000,'id':'son1257'},
{'time':'1144','ip':'89.149.233.20','type':'trade','item':'q energy','price':10000,'id':'fury01'},
{'time':'1400','ip':'89.149.233.32','type':'download','item':'ms ent','price':9000,'id':'bew02'},
{'time':'1400','ip':'89.149.233.39','type':'trade','item':'wiz asset','price':10000,'id':'fightclub'},
{'time':'1122','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'young0'},
{'time':'1300','ip':'89.149.233.43','type':'trade','item':'q energy','price':10000,'id':'kywu1'},
{'time':'1020','ip':'89.149.233.45','type':'trade','item':'ms ent','price':2700,'id':'wyue1'},
{'time':'1400','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'terra133'},
{'time':'1300','ip':'89.149.233.55','type':'download','item':'None','price':0,'id':'sdyt2387'},
{'time':'1046','ip':'89.149.233.48','type':'trade','item':'star asset','price':1800,'id':'sdk547'},
{'time':'1000','ip':'89.149.233.52','type':'trade','item':'q energy','price':10000,'id':'jjkw4'},
{'time':'1048','ip':'89.149.233.3','type':'trade','item':'wiz asset','price':5000,'id':'wyre97'},
{'time':'1210','ip':'89.149.233.54','type':'trade','item':'star asset','price':40000,'id':'jaeh3'},
{'time':'1055','ip':'89.149.233.13','type':'trade','item':'ms ent','price':2700,'id':'tool2345'},
{'time':'1353','ip':'89.149.233.48','type':'trade','item':'wiz asset','price':5000,'id':'lala20'},
{'time':'1400','ip':'89.149.233.2','type':'download','item':'None','price':0,'id':'vnv379'}]




# (1)로그 리스트를 반복문 통해서 요소를 하나씩 뽑아서 출력해주세요.
answer = []
for i in range(len(log)):
    # log[i] = 딕셔너리 타입 : 헷갈리지 않게 변수로 저장해주세요.
    # print(log[i])
    d = log[i]
    # (2) d 딕셔너리에서 key가 type인것을 뽑아 출력해보세요.
    #print(d["type"])
    # (3) key가 type인 value(2번에서 뽑은 value)가 trade인 딕셔너리를 뽑아주세요.
    if d["type"] == "trade":
        print(d)
        answer.append(d)
print(answer)

print("mission 2 ============")
# 종목(item)이 wiz asset 인 데이터를 찾아라. 
answer2 = []
for i in range(len(answer)):
    # print(answer[i])
    d = answer[i]
    # d["item"]
    if d["item"] == "wiz asset":
        print(d)
        answer2.append(d)
print(answer2)

print("mission 3 ============")
# 가격이 10000유로가 아닌 데이터르 앚아라
answer3 = []
for i in range(len(answer2)):
    # print(answer2[i])
    d = answer2[i]
    if d["price"] != 10000:
        print(d)
        answer3.append(d)
print(answer3)




# 과제 1) https://www.acmicpc.net/problem/2446
# 과제 2) https://www.acmicpc.net/problem/2588
# - input()은 1줄에 한개씩! => 2줄이니깐 2개