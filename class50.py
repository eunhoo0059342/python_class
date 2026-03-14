# 5번창고과 분류실을 동시에 관리하는 업체를 찾기


#data
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

# 트리구조
# key(부모) - value(자식)

# 창고5번과 분류실을 자식으로 갖는 노드는 누구인가?
# - A업체

# 조직도 (트리구조)
# - 앞에 부서명(부모) : 관리하는 업체들(자식)

data_array = {
    '병원': ['관리부'],
    '관리부': ['물류팀', '행정팀', '미화팀'],
    '물류팀': ['전자기기', 'A업체'],
    '행정팀': ['행정실'],
    '미화팀': ['B업체', 'C업체', 'D업체'],
    '전자기기': ['창고1'],
    'A업체': ['창고2', '창고3', '창고4', '분류실'],
    '행정실': [],
    'B업체': ['A병동'],
    'C업체': ['B병동, C병동'],
    'D업체': ['창고6'],
    '창고1': [],
    '창고2': [],
    '창고3': [],
    '창고4': ['보관실', '운반실'],
    '분류실': [],
    'A병동': ['102'],
    'B병동': ['응급실', '200'],
    'C병동': ['300'],
    '창고6': [],
    '보관실': [],
    '운반실': ['창고5'],
    '102': [],
    '응급실': [],
    '200': [],
    '300': [],
    '창고5': []
}
# 노드리스트 keys
keys = list(data_array)
 
 
# 노드 : 숫자나 문자열 => 객체(여러개의 데이터+기능)
# - 
class TreeNode:
    def __init__(self, data):
        self.data = data # 노드 이름
        self.parent = None # <- 부모를 찾기
        self.children = [] # 자식들
 
    # def __str__(self):
    #     return self.data
 
 
class Tree:
    def __init__(self):
        self.root = TreeNode('병원')  # 최상단

        # 역할은 동일
        self.node_list = [] # 노드리스트 - 노드객체로
        self.room_list = [] # 룸리스트 - 노드 이름들만

        self.node_list.append(self.root)
        self.room_list.append('병원')
 
    def add_node(self, data):
        if data not in self.room_list:
            self.room_list.append(data)
            self.node_list.append(TreeNode(data))
 
    def find_node(self, string):
        for node in self.node_list:
            if node.data == string:
                return node
        return False
 
    # 부모, 자식 데이터를 각 노드에 추가하는 역할을 함 => 데이터 삽입
    def define_relationship(self, data_dict):
        #sub 관계 설정
        for key in keys:
            for item in data_dict.get(key):
                if item != None:
                    self.find_node(key).children.append(self.find_node(item))
                    if self.find_node(item) != False:
                        self.find_node(item).parent = self.find_node(key)
 
 
tree = Tree()
# 트리에 데이터 추가
for key in keys:
    tree.add_node(key)
tree.define_relationship(data_array)

# 객체 - 데이터 여러개, 메서드 여러개 들어가서 한번에 들고있는 게 객체
# Tree의 속성, root, room_list 한번 출력해보기
print("트리의 root는?")
# 루트 노ㄷ의 이름을 출력하시오.
print(tree.root.data)
# 루트 노드의 부모랑 자식을 출력해보기
print(tree.root.parent)
print(tree.root.children)

print("\n트리에 들어가있는 노드 리스트는?")
# print(tree.room_list, "글자로만")
# print(tree.node_list, "객체로")

print("----")

# 내가 창고5랑 분류실을 동시에 갖는 조상(부모요소)를 찾기 => 함수
# = 트리, 대상1,대상2
def found(tree, a, b):
    # tree의 node_list(객체)중에서 a(객체)가 있냐?
    # => 반복문으로 다 꺼내서 하나씩 비교해서 찾아
    # => 객체의 data(속성이름)와 대상1의 이름이 같은게 있는지 찾기
    node_a = None
    node_b = None
    # 1. "창고5", "분류실" 객체 찾기
    for i in range(len(tree.node_list)):
        treenode=tree.node_list[i] # 객체
        # print(treenode, treenode.data)
        if treenode.data == a:
            # 객체
            # print(i,treenode.data,treenode.parent,treenode.children)
            node_a = treenode
        elif treenode.data == b:
            # print(i,treenode.data,treenode.parent,treenode.children)
            node_b = treenode

    # 2. a와 b 노드의 조상을 찾기 - 반복하면서 Tree를 타고 올라가기
    # 조상리스트에 찾은 부모를 추가하기
    # node_a를 부모로 바꿔
    parent_a = []
    while node_a:
        print("부모",node_a.parent )
        parent_a.append(node_a.parent)
        node_a = node_a.parent
    print(parent_a)
    
    parent_b = []
    while node_b:
        parent_b.append(node_b.parent)
        node_b = node_b.parent
    print(parent_b)

    # a부모와 b부모가 제일 처음으로 같은 구간을 찾아주세요!

    for i in range(len(parent_a)):
        for j in range(len(parent_b)):
            if parent_a[i] == parent_b[j]:
                if parent_a[i] : 
                    # print(i, parent_a[i].data)
                    return parent_a[i].data
                    
    
print(found(tree, "창고5", "분류실"))


# 청소년 IT 경시대회 대회안내문
# https://kitpa.org/contest/5



# <연습과제>
# 풀다가 막힌건 TODO
# 숫자의 개수 https://www.acmicpc.net/problem/2577 
# 더하기 사이클 https://www.acmicpc.net/problem/1110