# 💪 수업 준비사항 💻
# 1. 하우코딩 수업 NIS 로그인(미션풀때)
# ＊ID: agent@nis.com
# ＊PW: python
# 2.  VSCode LiveShare 링크 전달

'''
<복습>

데이터타입
1. 숫자형 Number
2. 문자열 String
- 인덱스(순서)를 가지고 있습니다. => 인덱싱, 슬라이싱
- len(데이터) : 데이터의 길이, 크기
- 문자열변수.replace("찾는문자,"바꿀문자") : 찾아서 바꾸기 => 찾아서 없애기로 응용 가능
- 문자열변수.split("구분인자") : 구분인자를 기준으로 문자열을 리스트로 변환

3. 리스트 List :여러개의 데이터를 저장하는 데이터타입
- 형태 : [요소,요소,요소,요소]
- 인덱스(순서)를 가지고 있습니다. => 인덱싱, 슬라이싱
- len(데이터) : 데이터의 길이, 크기
- 리스트는 추가, 수정, 삭제 
  - 리스트변수.append("추가데이터") 
  - 리스트변수[인덱스] = "변경할데이터" : 데이터 수정 (변수의 저장을 활용)
  - 리스트변수.pop() : 맨뒤에 데이터가 삭제

4. bool형 : True / False
=> 조건문


조건문 if~ elif~ else
if 조건 :

조건 : 만족한다(True), 불만족한다(False)
  

반복문 : 원하는 조건으로 반복
for문

for 반복변수 in 반복조건(range(숫자)): 
    반복할 코드
'''

print(bool(1+2==3))
# 10 > 20
print(bool(10 > 20))

alphabet = ['a','b','c','d','e','f','g']
# 리스트에 대해서 뭔가를 동작을할때, 통째로 하는 것보다 하나씩 꺼내서 사용한다.
alphabet[0]
alphabet[1]
alphabet[2]
alphabet[3]
# => 반복문을 통해서 모든 리스트의 요소를 뽑을수가 있습니다.
#(1) 리스트의 크기 만큼 반복을 돌려보자
# - len(데이터) : 데이터의 길이, 크기
#(2) 반복변수를 체크하자
# - 반복할때 반복변수가 어떤값이 나오는지 잘 체크할것
#(3) 리스트에서는 반복변수를 인덱스로 활용을 합니다.
# - 인덱싱이 가능합니다. => 리스트변수[인덱스(반복변수)]
for i in range(len(alphabet)):
    print(alphabet[i],f"{i}번째 값")

print("mission1 =================================")
# mission1) 기밀자료실(secret)이 있는 층을 찾아라!

# 각층에 대한 용도
purpose_list = ['general', 'office', 'office', 'general', 'office', 'general', 'office', 'office', 'office', 'secret', 'conference', 'conference', 'office', 'general', 'office', 'general', 'secret', 'office', 'general', 'secret', 'general', 'office', 'office', 'general', 'office', 'conference', 'office', 'office', 'office', 'conference', 'conference', 'conference', 'office', 'general', 'secret', 'general', 'office', 'secret', 'general', 'office']
#인덱스+1 = 층수 표현  1층        2층

#(3) 정답만 모아놓은 리스트 만들겁니다. : 정답이 여러개이기때문에
# - 빈리스트 []
answer = []

# 리스트 안에 'secret'이 있는지 체크해서 있으면, 해당 층을 출력해보기
#(1) 리스트의 모든 값을 뽑아라
for i in range(len(purpose_list)):
    # (2) 출력된 값이 'secret' 인지를 찾기 => 조건문
    # (주의) 내가 체크한값과 비교한 값이 다르지 않게 하기
    # print(purpose_list)
    if "secret" == purpose_list[i] :
        print(purpose_list[i],i + 1)
        #(4) 층수를 정답리스트에 추가하기
        # - 리스트변수.append(추가데이터)
        answer.append(i + 1)
print(answer)

print("mission2 =================================")
# 센서스 동작하지 않는다 = "error"가 있는 층을 찾는거다. 정답이 여러개면 리스트타입으로
answer2 = []
sensor_list = ['error', 'error', '054057', '054324', '054326', '054327', 'error', 'error', '054345', '054352', '054353', '054359', '054404', '054406', '054411', '054412', '054413', '054414', 'error', 'error', '054415', '054416', 'error', 'error', 'error', 'error', '054421', '054422', 'error', 'error', '054425', '054426', '054427', '054428' , '054429', '054430', '054431', '054432', '054433', '054434']
for i in range(len(sensor_list)):
    if "error" == sensor_list[i] :
        print(sensor_list[i], i + 1)
        answer2.append(i + 1)
print(answer2)

print("mission3 =================================")
# 폭발물은 기밀자료실이면서 센서가 "error"인 층이다.

# <조건문>
# 한번에 하나만 갖지는 않습니다. 한번에 여러조건을 체크해야할때, 
# <논리연산자>
# 1) A조건과 B조건을 동시에 만족하고 싶다. => A and B
# ex) 중학교 3학년이고, 파이썬을 공부하는 학생
# 2) A조건 B조건중 하나라도 만족하고 싶다. => A or B
# ex) 중학교 3학년이거나, 중학교 2학년이 학생


# 시청 데이터 => 각층별로 데이터를 말하기 때문에 서로 크기는 같습니다.
# 위치정보는 같다. = 인덱스를 같이 사용할 수 있따.
purpose_list = ['general', 'office', 'office', 'general', 'office', 'general', 'office', 'office', 'office', 'secret', 'conference', 'conference', 'office', 'general', 'office', 'general', 'secret', 'office', 'general', 'secret', 'general', 'office', 'office', 'general', 'office', 'conference', 'office', 'office', 'office', 'conference', 'conference', 'conference', 'office', 'general', 'secret', 'general', 'office', 'secret', 'general', 'office']
sensor_list = ['error', 'error', '054057', '054324', '054326', '054327', 'error', 'error', '054345', '054352', '054353', '054359', '054404', '054406', '054411', '054412', '054413', '054414', 'error', 'error', '054415', '054416', 'error', 'error', 'error', 'error', '054421', '054422', 'error', 'error', '054425', '054426', '054427', '054428' , '054429', '054430', '054431', '054432', '054433', '054434']
print(len(purpose_list))
print(len(sensor_list))

for i in range(len(purpose_list)):
    # print(purpose_list[i])
    # print(sensor_list[i])
    # purpose_list[i]가 "secret"이고 동시에 sensor_list[i]가 "error" 인 조건
    if "secret" == purpose_list[i] and "error" == sensor_list[i]:
        print(i + 1)

