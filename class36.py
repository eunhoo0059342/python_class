# 해시(hash)
# : 데이터를 일정 규칙에 따라서 변환해서 사용한다.
# 사물함 번호 2자리수 09 -> 비밀번호 4자리수 0009
# => 암호화


# 값=>  ---해쉬함수--- => 해쉬값(처리된 결과)

#         일정패턴으로
#         변환
#      ------------


'''
차량번호 -> 차고번호/비밀번호
6657  -> 157/4418
4762  -> 262/3757

- 차량번호에서 500을 나눈 나머지가 = 차고번호

0000-9999(만개) => 차고갯수(500개)가 부족하니깐 

(충돌: 변환할때, 규칙에 의해서 충돌이 발생할수 있습니다.)
(충돌체크를 해서, 충돌이 발생하면, 그 다음번호로 이동하기)
(충돌체크를 위해서, 값에따른 해쉬값이 어떻게 나왔는지 저장하는 해쉬테이블이 있습니다.)
(해쉬테이블 : 해쉬값이 어떻게 매칭되었는지 저장하는 테이블)
6657 -> 157
7657 -> 157
'''



tablesize = 500 
pw = []
import random
random.seed(29)
for i in range(tablesize):
    # 비밀번호가 들어가있다.
    pw.append(random.randint(1111,9999))
hashtable = [0]*tablesize

print(hashtable)
print(pw,len(pw))


# 1809번의 주차 비밀번호를 알아내라
# - 1. 차고번호 구하기
# =>

# 값(차량번호)=>  ---해쉬함수--- => 해쉬값(차고번호)
# (key)                        (value)
        #         차량번호를
        #         500으로
        #        나눈 나머지
        #       (충돌이 안나면(차량이 없다.),
        #        hashtable에 차량들어갔다고 표시)
        #      ------------



def hash(key):
    value = key % 500
    # (1)해쉬테이블에서 해당 차고에 챠량이 있는지 없는지 체크해보기있으면 충돌 없으면 충돌없음 출력해봊기
    print("차량번호",key)
    #print("차고 :에 차량이 들어가있는가(없으면0, 있으면 1)",hashtable)
    if hashtable[value] == 1:
        collision(value)
        return '충돌'

    else:
        # value번째 차고에 1로 표시해주기
        hashtable[value] = 1
        return'충돌 없음'


# 충돌안할때까지 찾는 함수 collision
# - 시작value번호를 전달 해서
# - 더이상 충돌안하는 차고번호(value)를 찾기
def collision(value):
    while hashtable[value] != 0:
        value = value + 1
        print(value)
        hashtable[value] == 1
    # TODO : 충돌안하는 차고 번호를 찾음. => 비밀번호 찾기 이어서하기
    
car1 = 6657
car2 = 4762
mycar = 1809
print(hash(car1))
print(hash(7657))
print(hash(car2))