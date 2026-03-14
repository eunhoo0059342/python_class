# 그래프 종류
# - 트리

# (1) heapq모듈 삽입하기
import heapq

# (2) q를 저장할 리스트를 하나 생성
q_lst = []

# (3) 삽입하기 heapq.heqppush(큐리스트,숫자)
# - 삽입예제 : 5,7,2,4

heapq.heappush(q_lst, 5)
heapq.heappush(q_lst, 7)
heapq.heappush(q_lst, 2)
heapq.heappush(q_lst, 4)
print(q_lst) # 내부적으로 힙 구조(트리)를 계산 

# (4) 뽑기: 제일 작은 숫자부터 뽑힌다. heapq.heapop(큐리스트)
print(heapq.heappop(q_lst))
print(heapq.heappop(q_lst))
print(heapq.heappop(q_lst))
print(heapq.heappop(q_lst))


# (5) 최대값부터 뽑고싶다.
# (5-1) 음수 개념을 사용한다. 
# - 넣을때 - 붙여서 추가 해준다.
heapq.heappush(q_lst, -5)
heapq.heappush(q_lst, -7)
heapq.heappush(q_lst, -2)
heapq.heappush(q_lst, -4)
print(q_lst)

# (5-2) 빼기 : 음수형태로 나옵니다. 
print(-1*heapq.heappop(q_lst))
print(-1*heapq.heappop(q_lst))
print(-1*heapq.heappop(q_lst))
print(-1*heapq.heappop(q_lst))



import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
# import networkx as nx
# import wizLib
import matplotlib

#data
myGraph=defaultdict(dict)
 
class GraphControl:
    def __init__(self):
        self.visual=[]
 
    def addEdges(self, start, end, dist):
        myGraph[start].update({end: dist})
        myGraph[end].update({start: dist})
        temp=[start, end, dist]
        self.visual.append(temp)
 
    def visualize(self):
        pass
        # G=nx.Graph()
        # for item in self.visual:
        #     u, v, weight = item
        #     G.add_edge(u, v, weight=weight)
        # pos={
        #     'A': (1, 3),
        #     'B': (2, 2),
        #     'C': (3, 1),
        #     'D': (2, 5),
        #     'E': (3, 4),
        #     'F': (4, 3),
        #     'G': (3, 7),
        #     'H': (4, 6),
        #     'I': (5, 5),
        #     'J': (4.5, 7)
        # }eLa=nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_nodes(G, pos)
        # nx.draw_networkx_edges(G, pos)
        # nx.draw_networkx_labels(G, pos)
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=eLa, font_size=10)
        # wizLib.showPlt(plt)
        # 
 
G=GraphControl()
G.addEdges('A', 'D', 3)
G.addEdges('B', 'E', 2)
G.addEdges('C', 'F', 4)
G.addEdges('D', 'E', 4)
G.addEdges('E', 'F', 5)
G.addEdges('D', 'G', 1)
G.addEdges('G', 'E', 1)
G.addEdges('E', 'H', 2)
G.addEdges('G', 'H', 3)
G.addEdges('H', 'F', 4)
G.addEdges('F', 'I', 2)
G.addEdges('H', 'I', 1)
G.addEdges('G', 'J', 4)
G.addEdges('H', 'J', 5)
G.addEdges('I', 'J', 3)
G.visualize()




# 다익스트라 dijkstra algorithm 알고리즘 함수로 구현해보기
# 필요한값: 시작노드(A/B/C), 도착노드(J),그래프(myGraph)
# 각노드마다 최적화 된 코스트를 갖고 있어야 계산 리스트를 갖고 있을거예요.

'''
myGraph = {
    'A': {'D': 3},
    'D': {'A': 3, 'E': 4, 'G': 1}, 
    'B': {'E': 2}, 
    'E': {'B': 2, 'D': 4, 'F': 5, 'G': 1, 'H': 2}, 
    'C': {'F': 4}, 
    'F': {'C': 4, 'E': 5, 'H': 4, 'I': 2}, 
    'G': {'D': 1, 'E': 1, 'H': 3, 'J': 4}, 
    'H': {'E': 2, 'G': 3, 'F': 4, 'I': 1, 'J': 5}, 
    'I': {'F': 2, 'H': 1, 'J': 3},
    'J': {'G': 4, 'H': 5, 'I': 3}
}
'''
def dijkstra_algorithm(start, end, graph):
    #print(myGraph)
    # (1) 노드의 갯수: myGraph의 길이
    # (2) 노드의 갯수만큼 무한대float()으로 셋팅 리스트 => 각 노드별 최적화된 코스트 계산을 저장하는 용도
    # {'A': inf, 'D': inf, 'B': inf, 'E': inf, 'C': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf, 'J': inf}
    cost_lst = {}
    for k,v in myGraph.items():
        cost_lst[k] = float('inf')
   
    # (3) 시작노드의 코스트는 0으로 셋팅
    cost_lst[start] = 0
    # (4) 탐색할 노드를 queue - heap으로 생성하기
    # 변수이름 = []
    # (5) 첫 시작노드는 queue 넣기
    # heapq.heappush(큐이름, [우선순위(코스트), 노드이름])
    q = []
    heapq.heappush(q, [cost_lst[start], start])
    visited_lst = []
    
    # (6) 큐가 빌때까지 반복해서 계산
    # - 큐에서 뽑기 => heapq.heappop(큐이름) => 우선순위(코스트) 작은것부터 나오게된다.
    # - 뽑은 노드랑 graph에서 연결된 노드를 찾아야한다.
    while len(q) > 0:
        heappop_q = heapq.heappop(q)
        #print("-- 뽑힌노드", heappop_q)
        cost, nod = heappop_q
        # 뽑힌노드는 방문에 넣어주기
        visited_lst.append(nod)
        
        # graph[nod] => 딕셔너리, 반복문통해서 뽑아주기
        for k,v in graph[nod].items():
            # k :연결된 노드이름
            # v : 엣지 코스트
            #print("연결된 노드:",k,"/ 엣지:", v)
            # <연결된 노드들의 코스트 계산>
            # (1)뽑힌노드의 코스트 + 엣지가중치를 더해주기
            # (2) 연결된 노드의 코스트 (1)에서 계산된 코스트 중에서 더 작은 값을 선택
            cost_num = cost + v
            cost_lst[k] = min(cost_num, cost_lst[k])
            # print(cost_num, cost_lst)

            # 다음 탐색 예정으로 heapq 추가해주기 
            # heapq.heappush(큐이름, [코스트, 노드 이름])
            #노드 이름이 방문하지 않은 노드들만 추가해주기
            if k not in visited_lst:
                heapq.heappush(q, [cost_lst[k], k])
        # print(q)
        #print()
    # 전체 노드의 코스트 출력을 확인하기
    # 결과 도착지점의 코스틀 return 하기
    print(cost_lst)
    return cost_lst[end]

print("A를 거쳐 가는 길 :",dijkstra_algorithm('A', 'J', myGraph))
print("B를 거쳐 가는 길 :",dijkstra_algorithm('B', 'J', myGraph))
print("C를 거쳐 가는 길 :",dijkstra_algorithm('C', 'J', myGraph))


