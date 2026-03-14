'''
# N번째 큰수 https://www.acmicpc.net/problem/2075
'''


import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []


# (1) 입력받기 : 전체 수에 n번째로 큰 수를 궁금한거다.
#  - 이차원리스트 => 행,열 구분이 필요한부분
# 리스트의 삽입 - .append("하나씩")
#            - .extend([리스트]) : 리스트의 요소을 하나씩 리스트에 넣어주기

for i in range(n):
    input_data = list(map(int, input().split(" ")))
         # n*n 반복해서 입력받기
    for j in range(len(input_data)):
        # heapq.heappush(리스트, 추가할데이터)
        # heapq.heappop(리스트)
        # 
        # 제한된 메모리에서 모든수 1500^2을 넣기에는 굉장히 부담스럽다.
        # - 다 넣을 필요는 없고,
        # - graph n개만 넣기 :
        # (1) graph길이기 n가 작으면, 일단 넣어
        # (2)graph길이기 n개 -> graph에서 가장 작은애보다 넣을 데이터가 크면 하나를 빼고 추가하기
        if len(graph) < n:
            heapq.heappush(graph, input_data[j])
        elif len(graph) == n:
            if graph[0] < input_data[j]:
                heapq.heappop(graph)
                heapq.heappush(graph, input_data[j])


# 큰것들 중에서 가장 작은값이 n번째 큰수
print(graph[0])





# (2) n번째로 큰 수 찾기, sorted(리스트,reverse=True) => 시간초과, 메모리초과
# sorted_data = sorted(graph, reverse=True)
# # print(sorted_data)
# print(sorted_data[4])

# (3) heap으로 n번째값 뽑아보기

