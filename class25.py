'''
모듈 : 하나의 기능단위로 분리해놓은 조각
- 파이썬에는 하나의 파일이 모듈단위
- 파이썬에서 제공하는 모듈 사용해볼겁니다.
- 오픈소스 사용 : 누구나 사용할수 있도록 코드를 오픈

math, random 모듈

<모듈사용방법>
import 모듈이름
'''
# 1. 수학 math모듈  => https://docs.python.org/ko/3.13/library/math.html
import math
import random
# 모듈이름.함수()
# (1) 반올림 round / 올림 math.ceil(숫자) / math.floor(숫자)
# -> 소수점 계산은 컴퓨터가 정말 싫어한다. 
num = 3.14
print(math.ceil(num))
print(math.floor(num))

# (2)제곱근 math.sqrt(x) 루트x
num2=4
print(math.sqrt(num2))

# (3)각도 math.degrees(x도)
print(math.degrees(num2))

# (4) 원주율 : math.pi





# 2. 랜덤 random모듈  => https://docs.python.org/ko/3.13/library/random.html
print("랜덤 random모듈---------------")
# 주의사항) 모듈을 항상 맨 위에서 추가해줘야한다.
# (1)random.random() :  난수 생성하기, 0 이상 1 미만의 숫자의 난수를 생성한다.
print(random.random())

# 0~10사이의 랜덤한 숫자를 뽑고싶다.
print(int(random.random()*10))

# 0~100사이의 랜덤한 숫자 뽑기
print(int(random.random()*100))


# (2) randrange(시작,끝) : 시작 이상 끝 미만의 정수 난수 생성하기
# 10~15까지중에서 뽑기
print(random.randrange(10, 16))


# (3)random.choice(리스트)
# 반친구들중에서 발표자를 1명 뽑고싶다.
friend=['A',"B","C","D","E"]
print(random.choice(friend))

# (4)random.shuffle(데이터): 순서를 랜덤하게 뒤죽박죽 섞기  -> return 없습니다.
# # 반친구들중에서 발표순서를 랜덤으로 뽑고싶다.
random.shuffle(friend)
print(friend)




# (과제) 로또를 뽑는 프로그램을 만들기 => lotto.py
# 함수로 만들기
# (1) 1~45번까지의 숫자중에서 랜덤하게 6개를 뽑습니다.
# - 뽑았을때, 중복되면 안됩니다.
# - 뽑았을때, 숫자가 정렬되어있어야합니다.

# (2) 로또가 당첨번호랑 맞는지를 체크해서 결과를 출력하기
# - 3개맞으면 "4등"
# - 4개맞으면 "3등"
# - 5개맞으면 "2등"
# - 6개맞으면 "1등"
result=[2,13,15,16,33,43]

# (3) 터미널에서 키보드로 장수를 입력하면 자동으로 갯수만큼 여러장 로또뽑는기

