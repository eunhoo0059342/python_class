# 미로탐색 https://www.acmicpc.net/problem/2178
# - 이차원리스트에서 탐색
# - m,n : 행과 열의 크기
# - 문제 설명은 (1,1) 출발해서 (m,n)까지 도착하는 최단 거리를 구하는 문제 => 인덱스 처리할것
#
#

'''
문제)
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력)
4 6
*01111
101010
101011
11101&
'''

# 탐색의 방법 : 
# bfs(너비우선탐색 - queue), dfs(깊이우선탐색 - stack)
#  _________  B
# 1|_4|_10|_ |_ |
# 1|_3|_6|_ |_ |
# 1|_2|_3|_4|_5|
#  |_ |_ |_ |_ |
# A  1 1 1 1




from collections import deque

h , w = map(int, input().split(" "))

m_lst = []

for i in range(h):
    # map(함수이름,iterable객체(문자열,리스트,튜플,집합,딕셔너리))
    m_lst.append(list(map(int, input())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# loute함수 => (bfs탐색을 진행하는 함수)
# 입력:시작x,시작y
def loute(s_x, s_y):
    que = deque()
    lst = [] # 최소거리(방문체크)
    for i in range(h):
        ls = []
        for j in range(w):
            ls.append(0)
        lst.append(ls)
    
    lst[s_y][s_x]=1
    # 첫 queue에는 시작좌표(y(행),x(열))들어가야하는데
    que.append([s_y, s_x])
    # bfs 탐색시작
    # - 탐색예정할 좌표 계산 => 탐색예정(Queue)에 추가
    # - 방문했음을 체크 => 최소거리를 계산하면 방문했다고 체크하기
    while len(que) != 0:
        pop_lst = que.popleft()
        curr_y = pop_lst[0]
        curr_x = pop_lst[1]
        for k in range(4):
            dy_pop = curr_y + dy[k]
            dx_pop = curr_x + dx[k]
            # <탐색할수없는 범위 조건>: 
            # - 행조건,열조건이 만족하지않을때 continue(# 행/열조건 : 0보다 작거나 마지막인덱스보다 크면 패스)
            # - 맵에서길이 아니면 탐색못해!!  : 1 길 0 길아니예요
            # - 방문했으면 패스 : 최소거리체크 리스트 lst[좌표]가 0이 아니면 continue
            
            if dy_pop < 0 or dy_pop > h-1: 
                continue
            elif dx_pop < 0 or dx_pop > w-1 :  
                continue
            elif m_lst[dy_pop][dx_pop] != 1:
                continue
            elif lst[dy_pop][dx_pop] != 0:
                continue
            # 탐색예정에 추가
            que.append([dy_pop, dx_pop])
            # <방문체크: 최소거리를 계산하기>
            # - 새좌표의 거리는 : 현재좌표의 거리 +1 계산하기
            lst[dy_pop][dx_pop] = lst[curr_y][curr_x] + 1
   

            

            
    # for i in range(len(lst)):
    #     print(lst[i])
    
    return lst

# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동

print(loute(0,0)[-1][-1])



