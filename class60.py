# 이동방법을 리스트로 만들어서 리스트로 계산하는 방법을 연습
# 

#data
# 3 로봇위치 : 3개
# 4 목적지 : 각 로봇별로 목적지까지 몇칸인지 계산하기 
# 누가 가장 빠르게 가는지
from collections import deque
import queue

string = [
   "0 0 1 0 0 0 0 0 0 0",
   "0 1 0 1 1 1 1 1 0 0",
   "4 1 3 0 0 0 0 1 0 0",
   "0 1 0 0 1 0 0 1 1 1",
   "0 1 1 1 1 0 0 0 0 3",
   "0 0 0 0 0 1 0 1 1 1",
   "1 1 1 1 0 0 0 0 0 0",
   "0 0 0 0 0 1 0 1 0 0",
   "1 1 0 0 1 1 1 1 0 1",
   "1 0 0 0 0 3 0 1 0 0",
]
#             B

# 1  4 10
# 1  3 6
# 1  2 3 4
# A  1 1 1
map_data=[]
robot_list=[]


# 각 로봇별로 이동 방법
# 아래(x:0 y:1)/위(x:0 y:-1)/우(x:1 y:0) /좌(x:-1 y:0)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# n, m=map(int, input().split())
for i in range(len(string)):
   map_data.append(list(map(int, string[i].split(" "))))
 
for i in map_data:
   print(i)
print()

# 2. BFS로 각 로봇별 경로 탐색을 진행하기 => 함수
# - 입력:  현재 로봇의 시작위치
# - 결과: 로봇이 목적지까지 가는데 걸리는 거리경로 이차원리스트
# ->
def loute(start):
    #(0-1) BFS Queue : 탐색예정 deque() 
    #(0-2) BFS 거리겸 방문체크리스트: 방문체크용 및 거리기록용 이차원리스트 => 거리 0으로 채워진 이차원리스트
    #(0-3) 시작노드를 queue 추가
    
    que = deque()
    lst = []    # 이차원리스트의 축약형 : visited = [[0 for j in range(len(map_data[i]))] for i in range(len(map_data))]
    for i in range(len(map_data)):
        ls = []
        for j in range(len(map_data[i])):
            ls.append(0)
        lst.append(ls)
    
    lst[start[0]][start[1]]=1
    que.append(start)
    #(1) 탐색 queue 방문예정이 더이상 없을때까지 진행
    # - (1-1) 탐색할 노드 뽑아주기
    # - (1-2) 이동할 좌표 계산 -> dx,dy 이동한 칸수리스트 사용해서 이동할 예상좌표 계산
    while len(que) != 0:
        pop_lst = que.popleft() # 좌표 노드[i,j] = [y,x]
        curr_y = pop_lst[0]
        curr_x = pop_lst[1]
        for k in range(4):
            dy_pop = curr_y + dy[k]
            dx_pop = curr_x + dx[k]
            
            # (1-3) 새로 계산된 좌표 : 행,열의 위치가 0 ~ 마지막인덱스 안에 있어야한다.
            # - 현재 노드 : 위를 볼건지  vs 새로계사한 위좌표가 가능한지
            # 0<=dy_pop<=마지막인덱스
            if dy_pop < 0 or dy_pop > len(map_data)-1:
                continue
            if dx_pop < 0 or dx_pop > len(map_data[0]) -1 :
                continue
            # (1-4) 탐색진행, map_data 1이랑 4는 지나갈수없습니다. 방문리스트 지나간 길은 탐색할수없습니다. (lst 값이 없을때 0일때만 탐색하기)
            if map_data[dy_pop][dx_pop] == 1 or lst[dy_pop][dx_pop] != 0:
                continue
            # print("다음좌표위치",dy_pop, dx_pop)
            # 다음좌표까지의 거리값 계산 = 현재까지의 거리값(lst,map_dat) +1 
            lst[dy_pop][dx_pop] = lst[curr_y][curr_x] + 1
            # 탐색예정 큐에다가 다음좌표를 추가
            que.append([dy_pop, dx_pop])

            
    for i in range(len(lst)):
        print(lst[i])
    
    # 도착위치 2행 0열의 거리값을 return 결과로 반환하기
    return lst[2][0] -1

# 1. 로봇(3)의 위치, 행,열 찾아주세요
for i in range(len(map_data)):
   for j in range(len(map_data[i])):
        if map_data[i][j] == 3:
            print("로봇위치",i,j,"----")
            print(loute([i,j]))

