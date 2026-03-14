# 스택, 큐
# 스택은 LIFO(Last In First Out)
# 큐은 FIFO(First In First Out)


# 16번 컨테이너가 몇번 소형활물선에 들어가 있는가
#cargoship
import random
class Stack:
    def __init__(self, input_num):
        self.lst = input_num
    
    # 스택에 데이터 넣기
    def push(self, push_data):
        self.lst.append(push_data)
    
    # 스택에 데이터 뽑기
    def pop(self):
        if self.isempty() == True:
            return None
        else:
            return self.lst.pop()
    # 스택이 비어있는지
    def isempty(self):
        if self.size() == 0:
           return True
        else:
           return False
    # 스택의 사이즈
    def size(self):
        return len(self.lst)
        
random.seed(66)

# 컨테이터 번호 리스트 cargolist
cargolist = [10, 35, 1, 2, 31, 5, 18, 19, 20, 21, 22, 4, 23, 15, 16, 17, 34, 7, 8, 30, 3, 24, 9, 36, 37, 38, 39, 14, 27, 28, 29, 25, 26, 6, 11, 12, 13, 33, 32]
random.shuffle(cargolist)

# 스택 객체에 cargolist(리스트) 데이터가 들어간다.
# 대형화물선 cargo
cargo = Stack(cargolist)
# 소형화물선 : 최대 5개까지 들어갈수 있습니다. LIFO => 스택
# - 소형화물선 번호
# - 소형화물선에 들어갈 공간 stack
cargo_ship = Stack([])
cargo_num = 1

# print(cargo.lst)
# [7, 23, 3, 6, 29, 19, 22, 2, 21, 28, 33, 24, 25, 35, 20, 10, 37, 38, 15, 11, 4, 1, 9, 32, 26, 16, 5, 12, 39, 13, 36, 18, 34, 8, 27, 17, 14, 30, 31]

target = 16

# 시뮬레이션
# (1) 반복적으로 cargo(스택) 컨테이너 하나씩 뽑아주기
# (2) 뽑은 컨테이너를 cargo_ship(스택)최대5개 넣어주기
# (3) 다섯개가 되면 다음 소형화물선을 가져오기 (번호 바뀌고, cargo_ship도 다 빼기)
# (4) 하나씩 뽑아주면서 타겟 컨테이너(target)가 어느 소형화물선 번호(cargo_num)에 들어갔느지 체크하기

while cargo.isempty() == False:
    pop_cargo = cargo.pop()
    cargo_ship.push(pop_cargo)
    if cargo_ship.size() == 5:
        # 객체에서는 속성을 바로 직접 접근 좋지않다.
        # in : 파이썬에만 있습니다. 다른 언어 프로그래밍이 어려워요.
        # => 반복문 돌리고 안에 if
        if target in cargo_ship.lst:
            print(cargo_num)
        
        # print(cargo_ship.lst)
        while cargo_ship.isempty() == False:
            container_num = cargo_ship.pop()
            if container_num == target:
                print(cargo_num)
        cargo_num += 1
        # print(cargo_ship.lst)
    