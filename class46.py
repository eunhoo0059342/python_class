import random
import datetime as dt
random.seed(20)
from collections import deque

# IC : 고속도로노드
class Interchange:
    def __init__(self, name):
        self.name=name     # 고속도로 이름
        self.pass_list=[]  # 지나간 차량의 리스트
        for i in range(30):
            passtime=dt.datetime(year=2050, month=3, day=13, hour=random.randint(10, 18), minute=random.randint(0, 59))
            self.pass_list.append((random.randint(1000, 9999), passtime))
            if (self.name=='West Daventown' or self.name=='Katherineton Lake' or self.name=='Seanchester Ville') and i==15:
                self.pass_list.append((3730, passtime))
 
    def __str__(self):
        return '{}'.format(self.name)
 
#cityInterChange => IC 리스트와 현재 그래프 연결 상태를 담고 있는 클래스
# cityInterChange 데이터 : 인접리스트로 구현된 그래프
# 고속도로 연결 그래프 : 고속도로끼리 어떻게 연결이 되어있는가
class CityInterChange:
    def __init__(self):
        self.graph={}
        self.node_list=[]
 
    # 노드추가
    def addVertex(self, V):
        self.graph[V]=[]
    # 엣지추가
    def addEdge(self, startV, endV):
        if endV not in self.graph[startV]:
            if startV != endV:
                self.graph[startV].append(endV)
                self.graph[endV].append(startV)
 
    def printIC(self):
        for i in self.node_list:
            print(i)
 
    def printConnection(self):
        for key in self.graph:
            print(key, ' :', end=' ')
            adj_list=self.graph[key]
            for i in range(len(adj_list)):
                print(adj_list[i], end=' ')
            print()
 
# 인스턴스 :그래프 객체를 생성
ICs=CityInterChange()
namelist = ['South Sarahton', 'West Daventown', 'New Romerochester', 'Johnstadburhg', 'East Roberstad', 'Portborough', 'South Gregory', 'Davisborough', 'Katherineton Lake', 'Seanchester Ville', 'Jerry Haven', 'Dorothytonbury', 'Port Reyesview', 'North Michaelbury', 'New Claireland', 'East Nicholsland']
 
# 그래프 연결을 미리 셋팅
for i in range(len(namelist)):
    newIC=Interchange(namelist[i])
    ICs.node_list.append(newIC)
    ICs.addVertex(newIC)
 
for i in range(len(namelist)*3):
    ICs.addEdge(ICs.node_list[random.randint(0, len(namelist)-1)], ICs.node_list[random.randint(0, len(namelist)-1)])

def sortByValue(dic) :
    sorted_values = sorted(dic.values()) # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in dic.keys():
            if dic[k] == i:
                sorted_dict[k] = dic[k]
                break
    return sorted_dict



# ICs출력해주세요. => printConnection 메서드
# 각 고속도로별 연결되 고속도로가 누가 있는지 

# BFS(너비우선 탐색) - 큐
# - 두개의 데이터 : 그래프, 찾을 값
# collection모듈 deque객체

def bfs(graph, car_nu, nod_lst):
    # (1) 큐를 하나 만들어주기 
    q = deque()
    # (2) 시작노드를 결정하기 => 노드리스트의 0번째를 시작으로 하기
    # - 큐에다가 시작노드를 추가
    start_nod = nod_lst[0]
    q.append(start_nod)   
    # (3) 어떤 순서로 방문을 햇는가? visited 리스트 
    visited_lst = []
    

    ### 탐색시작 ###
    # - Q 다 빌때까지 반복하게 됩니다.
    # - 탐색할 노드를 하나 Q에서 뽑습니다.(가장 왼쪽.popleft())
    # - 뽑은 노드는 visited_list에 추가해줍니다.
    # - 그래프인접행렬에서 뽑은 노드랑 연결된 다른 노드를 찾아서 
    # - 찾은 노드들을 q에 추가합니다.(가장 오른쪽)

    while True:
        if len(q) == 0:
            break
        # 뽑은 IC
        nod1 = q.popleft()
        visited_lst.append(nod1)
        # print(graph[nod1])
        # 뽑은 ic에서 지나간 차량리스트 passlist속성에서 3730번이 있는가?
        #print("----TODO: 3730 차량이 어디에 있는가?")
        for i in range(len(nod1.pass_list)):
            # print("--")
            # 튜플(차량번호, 통과한 시간)
            # print(nod1.pass_list)
            if nod1.pass_list[i][0] == 3730:
                print(nod1.name, nod1.pass_list[i][1])
        for i in range(len(graph[nod1])):
            # 그래프안에 들어간 데이터는 객체 IC
            # graph[nod1][i]가 visited_list 안에 이미 방문한 것인가?
            if graph[nod1][i] not in visited_lst:
                q.append(graph[nod1][i])
                # 
        
    
print("\n-------")
print(bfs(ICs.graph, 3730, ICs.node_list))

# West Daventown 2050-03-13 12:41:00
# Katherineton Lake 2050-03-13 13:05:00
# Seanchester Ville 2050-03-13 17:03:00
