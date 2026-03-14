'''
그래프
- 연결점 Node
- 연결선 Edge

=> 파이썬 어떻게 표현을 할까
    - 큐랑 스택: (1차원)리스트
    - 그래프 :2차원리스트(행렬 metrix => 인접리스트)

'''



#data
import random
random.seed(104)
 

# 객체(Object) : 데이터+ 기능 한번에 담을 수있는 구조
# - 속성  : 데이터 => 변수
# - 메서드 : 기능 => 함수

# <객체다루기>
# (1) 객체 정의     => class : 객체의 틀을 설계
# (2) 실물 객체 생성 => 인스턴스 생성

# <class생성하기>
# (1) __init__ 메서드 (생성자) : 객체를 생성할때 초기값을 셋팅

# 그래프 = 이차원리스트 
# => (1) 인접리스트 / 노드 리스트 필요하다.
# => (2) 엣지를 추가(양방향)
class Graph():
    def __init__(self, nod_lst):
        # nod_list의 크기만큼 0으로 셋팅된 이차원리스트를 만들어주기
        
        self.nod_lst = nod_lst
        self.g_lst = [[0 for j in range(len(nod_lst))] for i in range(len(nod_lst))]
        self.g_dict = {}

    # 엣지추가하기 : 연결선을 만들려면 점 2개(노드)  
    def append_edge(self, nod1, nod2):
        if nod1 <= 0 or nod2 <= 0:
            return
        elif nod1 > len(self.nod_lst) or nod2 > len(self.nod_lst):
            return
        else:
            self.g_lst[nod1][nod2] = 1
            self.g_lst[nod2][nod1] = 1
        
    def addVertex(self, V):
        self.g_dict[V] = []
 
    def delVertex(self, V):
        if V in self.g_dict.keys():
            del self.g_dict[V]
 
    def addEdge(self, nod1, nod2):
        if nod2 not in self.g_dict[nod1]:
            if nod1 != nod2:
                self.g_dict[nod1].append(nod2)
                self.g_dict[nod2].append(nod1)
    def printGraph(self):
        for key in self.g_dict.keys():
            adj_list = self.g_dict[key]
            print(key, end=' : ')
            for i in range(len(adj_list)):
                print(adj_list[i], end=' ')
            print()
 
    def printGraph2(self):
        for i in range(len(self.g_lst)):
            print(self.g_lst[i])

    # g_dict에서 안젤라(Angella) 연결된 사람들의 이름을 찾아보기
    # value에 안젤라가 포하되어잇는 Key을 출력하기 key이름들을 리스트로 묶어서 출력하기 
    #딕셔너리의반복
    # for 키,값 in 딕셔너리.items()
    def find_name(self):
        for k, v in self.g_dict.items():
            # print(k)
            # print(v)
            for j in range(len(v)):
                if v[j] == 'Angella':
                    print(k)
# 안젤레라의 지인: 노드
name_list = ['Melissa','Chen','Lewis','Lisa','Jeffrey','Miguel','Oscar','Angella','Leslie','Erik','Dana','Kristen','Roy','James','Allison','Robin','Margaret','Cynthia','Leonard','Natatsha','Oliver','Hudson','Ava','Jack','Rbecca','Graham','Jordan','Davis','Josha','Lance','Cindy','Laura']
map_graph = Graph(name_list)
 
for name in name_list:
  map_graph.addVertex(name)

for i in range(len(name_list)):
    map_graph.append_edge(random.randint(0,  len(name_list)-1),random.randint(0, len(name_list)-1))
    map_graph.addEdge(map_graph.nod_lst[random.randint(0,  len(map_graph.nod_lst)-1)], map_graph.nod_lst[random.randint(0, len(map_graph.nod_lst)-1)])

map_graph.delVertex('Angella')
print(map_graph.nod_lst)
print(map_graph.g_lst)
map_graph.printGraph()
map_graph.find_name()

# (1) 인접리스트 => 안젤라가 몇번인지를 체크해서 
#  =>리스트에서 인덱스 찾아주느 메서드 리스트.index('찾는내용')

# (2) 인접딕셔너리 => 그래프를 구성할수 있다.









