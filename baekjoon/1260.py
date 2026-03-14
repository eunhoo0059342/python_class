# DFS와 BFS https://www.acmicpc.net/problem/1260

'''
문제)
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력)
첫째 줄에 정점(node)의 개수 N(1 ≤ N ≤ 1,000), 간선(edge)의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''

from collections import deque

# a,b,c = [4,5,1] => list(map(함수이름,리스트))
# 변수의 다중할당
input_data = list(map(int, input().split(" ")))
n, m, v = input_data
input_num_lst = []
# 인접리스트(노드가 숫자), 인접행렬(노드가 문자-딕셔너리)
# n*n을 0으로 채워

# (1)반복문으로 이차원리스트만들기
# graph = []
# for i in range(n):
#     row=[]
#     for j in range(n):
#         row.append(0)
#     graph.append(row)
# (2) 축약형으로 이차원리스트만들기
graph = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(m):
    # 엣지에 연결할 노드1,노드2을 받는 중 => 그래프에 edge추가
    input_num = list(map(int, input().split(" ")))
    input_num_lst.append(input_num)
    nod1, nod2 = input_num
    
    graph[nod1][nod2] = 1
    graph[nod2][nod1] = 1



# <bfs 함수를 만들기> - Queue
# 필요데이터는 : 그래프, 시작노드
# 1. queue:앞으로 탐색예정인 노드 
#    visited: 방문완료된 노드리스트(뽑힌 노드)
# 2. 시작노드를 queue 넣어서 초기 세팅
# 3. ⭐ queue가 다 빌때가지 탐색
#  - 방문할 노드 뽑기
#  - visited에 방문한 노드를 추가
#   -> (조건)이때, 찾는 노드가 방문하지 않은 노드들만 추가해야한다.
#  - ⭐ 뽑은 노드랑 연결된 노드을 탐색예정queue 추가
# [
#     [0, 0, 0, 0, 0], # 0행 - 버리는것 
#     #  1열 2열 3열 4열
#     [0, 0, 1, 1, 1], # 1행 -1번노트 : 각 노드별로 연결상태
#     [0, 1, 0, 0, 1], # 2행 -2번노드 : 1,4번노드
#     [0, 1, 0, 0, 1], 
#     [0, 1, 1, 1, 0]
# ]


def bfs(graph, start_nod):
    # (1)
    q = deque()
    visited_nod = []
    # (2)
    q.append(start_nod)
    # (3)
    while len(q) > 0:  # while q:
        pop_q = q.popleft()
        if pop_q not in visited_nod:
            visited_nod.append(pop_q)
        # TODO: 그래프 뽑은 노드랑 연결된 엣지를 찾아라!
        # graph에서 pop_q번째노드랑 연결된 노드(1)를 찾아주세요.
        # print(pop_q)
        # print(graph[pop_q])
        for i in range(len(graph[pop_q])):
            if graph[pop_q][i] == 1:
                # print(i)
                if i not in visited_nod:
                    q.append(i)
        # print(q)
    # 방문한 노드를 문자열로 표현 map(문자열,함수)
    return " ".join(map(str, visited_nod))
       


'''
<dfs 함수를 만들기> - stack
필요 데이터 : 그래프, 시작노드

1. stack: 앞으로 탐색한 노드(LIFO)
   visited : 방문이 완료된 노드리스트
2. 시작노드를 stack 넣어서 초기화
3. stack 다 빌때까지 탐색
    - 방문할 노드 뽑기
    - visited에 방문한 노드를 추가
        -> (조건)이때, 찾는 노드가 방문하지 않은 노드들만 추가해야한다.
    - 뽑은 노드랑 연결된 노드을 탐색예정 stack 추가

'''
def dfs(graph, start_nod):
    s = []
    visited_nod = []

    s.append(start_nod)

    while len(s) > 0:
        pop_s = s.pop()
        if pop_s not in visited_nod:
            visited_nod.append(pop_s)
        # stack 넣어주면 오른쪽 탐색 - dfs 기본적으로 왼쪽부터 탐색
        # [2,3,4]
        for i in range(len(graph[pop_s])):
            ii= len(graph[pop_s])-1-i
            if graph[pop_s][ii] == 1:
                if ii not in visited_nod:
                    s.append(ii)

    return " ".join(map(str, visited_nod))


print(dfs(graph, v))
print(bfs(graph, v))

    


# 과제) 
# 소인수분해 https://www.acmicpc.net/problem/11653
# 2007년 https://www.acmicpc.net/problem/1924
