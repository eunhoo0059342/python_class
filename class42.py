print("==============")
import random
random.seed(20201216)
import datetime
# 50230번 박스
# 컨베이어벨트(큐)에 물건을 보내고, 트럭으로 운반


# 출발시간
departure_time=datetime.datetime(2050, 2, 27, 10, 00)

# 화물 객체(Cargo)
# - number : 화물번호
# - truck_number : 화물이 타야하는 트럭번호
# - departure_time : 출발시간 <- 계산을 해야한다. 초기화 된 시간 맨처음

class Cargo:
    def __init__(self):
        self.number=random.randint(10000, 99999)
        self.truck_number=random.randint(0, 9)
        self.departure_time=datetime.datetime(2050,2,27,10,00)

'''
cargo_list : Cargo객체가 저장된 화물리스트
- 컨베이어밸트에 실려서 화물이 빠진다. => 큐(먼저들어간게 먼저, 나오는 구조) 

truck_lst : 10개의 트럭 - 화물을 싣기리스트 최대3개까지
- round_num_list : 각 트럭별로 운반횟수
- time_per_round_list : 각 트럭별로 1회 운반할때 걸리는 시간

'''
cargo_list=[]
while len(cargo_list)!=100:
    cargo=Cargo()
    if cargo not in cargo_list:
        cargo_list.append(cargo)

# 각 트럭별로 운반한 횟수 리스트: 
round_num_list=[0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0]
# 각 트럭별로 운반할때 걸리는 시간(분):
time_per_round_list=[40, 50, 60, 30, 20, 25, 10, 5, 55, 25]

# 이차원리스트
truck_lst = [[], [], [], [], [], [], [], [], [], []]
            #0트럭#1트럭 #트럭


# 시물레이션: 50230번 박스 언제 출발하는가?
# (1) cargo_list에서 하나씩 뽑아주기
# (2) 뽑은 애를 트럭에 싣기(순차적으로, 각 화물별 트럭번호에다가 싣기)
#      - 리스트에 화물객체를 추가 해주기
# (3) 트럭은 최대 3개가되면 꽉차서 출발합니다. 
#     => 출발시간을 계산하기, 한바퀴 돌때마가 걸리는 시간 주어집니다.
#     => 트럭 운반횟수 1씩 증가
#     => 출발시간 계산하기(최초시작시간 + 한바퀴걸린시간*운반횟수)

for i in range(len(cargo_list)):
    cari = cargo_list[i]

    # cari : 화물 인스턴스(cargo Object)
    #print(cari.truck_number)
    # print(cari.truck_number)
    truck_lst[cari.truck_number].append(cari)

    # (3)해당 트럭이 최대 3개의 화물이되면 출발 -> 다 비워야해
    # A -> 3
    # B -> 3
    # C -> 2 
    # [[],[],[C],[A,B]]

    

    # 50230번 화물의 출발시간을 찾아주세요!
    if len(truck_lst[cari.truck_number]) == 3:
        # print("트럭안 화물", truck_lst[cari.truck_number])
        # -- 출발할때 : 해당트럭이 현재까지 걸린시간 계산하기
        # start_time : 출발전까지 트럭이 운전한시간
        start_time = time_per_round_list[cari.truck_number] * round_num_list[cari.truck_number]
        # 출발시간 게산 : 기준되는 출발시간에 지금까지 트럭이 걸린시간 더해준다.
        # => datetime 디데이 계산 datetiem.timedelta(minutes=추가할시간)
        calcul_start_time = departure_time + datetime.timedelta(minutes=start_time)

        # 물건 내릴때 - 각 화물의 번호가 체크가 가능하다.
        while len(truck_lst[cari.truck_number]) != 0:
            pop_truck = truck_lst[cari.truck_number].pop()
            # print(pop_truck.number)
            if pop_truck.number == 50230:
                print(calcul_start_time)

        # --- 화물을 다 내린상태
        # 해당 트럭 운반횟수 1씩 증가 => round_num_list
        round_num_list[cari.truck_number] += 1


        