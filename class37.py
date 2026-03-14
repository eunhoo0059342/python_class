# 해시(HASH)
# 규칙을 가지고 변환
# 매핑결과 => hashtable

# 차량        주차위치
# (key)     (value)
# a ------> A
# b ------> B

# 값=>  ---해쉬함수--- => 해쉬값(처리된 결과)

#          일정패턴으로
#          변환
#       ------------

# 차량번호 -> 차고번호/비밀번호
# 6657  -> 157/4418
# 4762  -> 262/3757
# - 차량번호에서 500을 나눈 나머지가 = 주차위치


# 주차공간 500개
tablesize = 500 
pw = []
import random
random.seed(29)
for i in range(tablesize):
    # 비밀번호가 들어가있다.
    pw.append(random.randint(1111,9999))

# 0으로 채워진 500길이 자리 리스트
# [0]*갯수 : 반복해서 리스트가 채워진다.
hashtable = [0]*500
print(hashtable)



# 해쉬함수 : 차량번호(key)가 들어오면 주차위치(value)를 나온다..
def hash(key):
    # 주차위치(value)는 차량번호에서 500을 나눈 나머지다.
    value = key % 500
    if hashtable[value] == 1:
        value = collision(value)
        # return '충돌'

    # value(주차위치)가 나오면 => 매핑을 해야한다.
    # hashtable 매핑이되면 1 안되면 0으로 표시
    # => 몇번째를 1로 바꿔줘야할까?
    # => hashtable(주차 현황 리스트)에서 주차위치(index)이다.
    hashtable[value] = 1
    
    print(value)
    return value


# 충돌이 되면 다음번호에다가 매핑시도
# 더이상 충돌이 없을때까지... 
# 매핑이 되는 값을 내보내주기
def collision(value):
    while hashtable[value] != 0:
        value = value + 1
        print(value)
    return value


car1 = 6657
car2 = 4762
mycar = 1809
hash_mycar = hash(mycar)
print('car1 >>',hash(car1))
print('7657 >>',hash(7657))
print('8657 >>',hash(8657))
print('car2 >>',hash(car2))
print('mycar >>',hash_mycar)
# 비밀번호 pw는 주차장 크기만큼의길이로 비밀번호를 갖고 있다.
print(hash_mycar, pw[hash_mycar])



# 자료구조 & 알고리즘 : 프로그래밍할때 필수적입니다.
# 자료구조란 : 데이터의 구조를 배우는 내용
# 알고리즘 : 문제(백준X, )를 어떻게 해결하면 될까?

# 웹사이트 로딩시간 3초가 -> 1초
