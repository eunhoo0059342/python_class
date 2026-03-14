# 스택/큐 
# 그래프Graph

#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?CB286C7786FA7145DE6F630EEF363AE1489C

#data
import matplotlib.pyplot as plt # 데이터 시각화(그래프, 차트)
import networkx as nx
import wizLib

# 무시 ---
class GraphVisualization:
    def __init__(self):
        self.visual=[]

    def addEdge(self, a, b):
        temp=[a, b]
        self.visual.append(temp)

    def visualize(self):
        G=nx.Graph()

        for item in self.visual:
            a, b = item
            G.add_edge(a, b)

        pos=nx.shell_layout(G)

        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)

        wizLib.showPlt(plt)

G=GraphVisualization()


print("mission1 =====가장많이 연결된 사람을 찾아보자===========")
## phonebook 연락처
# 데이터 송수신 기록표
phonebook = {1:'Sem',2:'Milan',3:'Sophie',4:'Evi',5:'Lars',6:'Joep',7:'Daan',8:'Dex',9:'Esmee',10:'Vera'}

#code
#그래프 구현하기
NODE_NUMBER=11

class Graph:
    def __init__(self):
        # 그래프의 인접리스트(행렬)
        # 10X10 맞지만 인덱스편의상 11*11
        # 연결이 안되어잇으면 0 / 연결이 되어있으면 1
        self.lst = []
        # (1)
        # for i in range(11):
        #     for_lst = []# 행 리스트
        #     for j in range(11):
        #         for_lst.append(0)
        #     self.lst.append(for_lst)
        # (2)축약형
        self.lst = [[0 for j in range(11)] for i in range(11)]
        
        # (3)
        # for i in range(11):
        #     self.lst.append([0]*11)
        # # (4)
        # print([[0]*11 for i in range(11)])
        
        # print([[0]*11]*11, "숫자 복제는 가능하나 리스트 *복제 사용불가")
    
    '''
    엣지(노드랑 노드를 연결하는 선)
    : 연결되면 1로 바꿔주기
    '''
    def edge(self, nod1, nod2):
        if nod1 <= 0 or nod2 <= 0:
            return
        elif nod1 > 11 or nod2 > 11:
            return
        else:
            self.lst[nod1][nod2] += 1
            self.lst[nod2][nod1] += 1
        G.addEdge(nod1, nod2)
         
    def printGraph(self):
        for i in range(NODE_NUMBER):
            for j in range(NODE_NUMBER):
                print(self.lst[i][j], end=' ')
            print()
        G.visualize()
    
g = Graph()
g.edge(1, 4)
g.edge(10, 5)
g.edge(7, 6)
g.edge(6, 1)
g.edge(2, 7)
g.edge(3, 6)
g.edge(7, 8)
g.edge(7, 9)
g.edge(9, 3)
g.edge(5, 7)
g.edge(10, 6)
g.edge(7, 4)
g.edge(9, 10)
g.edge(9, 1)


# g.printGraph()

# // g.lst 에대해서 제일 많은 값을 찾아보기 
sum_lst = []
max_num = 0
max_index = 0
for i in range(len(g.lst)):
    if sum(g.lst[i])>max_num:
        max_num = sum(g.lst[i])
        max_index = i
    sum_lst.append(sum(g.lst[i]))

print(sum_lst,max(sum_lst))
print(max_num,max_index)
print(phonebook[7])
