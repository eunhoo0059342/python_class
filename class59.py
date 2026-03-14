# 재귀함수 : 나 자신을 불러서 하는 함수
# - 큰 덩어리의 문제를 작게 쪼개서 해결할때


# 재귀함수 대표예제)
# - 피보나치 수열
# an+1 = an + an+1


# 피보나치 수열 10번째
# 0 1 1 2 3 5 8 13 21 ...
# 입력 - 몇번째 수n
# 결과 - n번재 수
# 점화식 : an+2 = an + an+1 (n>=2)
# an = an-2 + an-1
# - 0번째 , 1번째 고정 - 피보나치로 구할수 있는게 아니야 => 종료조건



from re import A


n=10
def fibonacci(n): # n번째 피보나치숫자
    # - 0번째 , 1번째 고정 - 피보나치로 구할수 있는게 아니야 => 종료조건
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # n번째 = 
    # n-1번째 피보나치숫자
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))


# 팩토리얼 5! 5*4! 

def factorial(n):
    # if n == 0:
    #     return 0
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))
print(factorial(1))

#--------------------------------------
# 그래프 탐색 BFS DFS
print("====")

#data
# 2 탐색시작
# 0 길
# 1 벽

string=[
    "0 0 1 0 0 0 0 0 0 0",
    "2 1 0 1 1 1 1 1 0 0",
    "0 1 0 0 1 0 0 1 0 0",
    "0 1 0 0 1 0 0 1 1 1",
    "1 1 0 2 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 1",
    "1 1 1 0 1 0 0 0 0 0",
    "0 0 0 0 0 1 0 1 1 0",
    "1 1 1 0 1 1 1 1 0 1",
    "0 0 0 2 0 0 0 0 0 0",
]
 
# 리스트안에 문자열 => 이차원리스트
# string 데이터를 이차원리스트 변경
mapp = []
for i in range(len(string)):
    i_string = string[i].split(" ")
    # print(list(map(int, i_string)))
    mapp.append(list(map(int, i_string)))
print(mapp)


7


# dfs하는 함수
# - 입력 :  시작위치 행,열
# - 결과 : 없음. => lst 바로 체크 할거라서 

'''
탐색하는 방법
1. 시작할건지
2. 탐색예정노드리스트 : 시작노드로부터 연결된 노드를 체크해서 관리
3. 방문한노드 체크 : 재방문 안할거라서 => 재방문하면 도돌이표 똑같은 상황반복을 피하기 위해서 체크
4. 모든 노드를 다 탐색하면 종료

'''
# 스택활용탐색 
def dfs_stack(i, j):
    print("시작위치",i,j) # 노드 (i행,j열)
    # 1. 탐색예정노드 리스트 만들어주세요. => 스택
    # (1-2) 시작노드를 탐색예정노드에 순서쌍형태로 추가
    # 2. 방문한노드 체크 - 방문한 노드기록 map에다가 안의 값3을 바꿔서 표시
    # - 왜냐며) 0번만 따라가고, 1나오면 더이상 탐색을 안할거라서
    will_lst = []
    start_nod = (i, j)
    will_lst.append(start_nod)
    # 3. 탐색은 탐색예정스택이 빌때까지 "반복"하면서 탐색하기
    # (3-1) 노드를 뽑기
    # (3-2) 방문노드로 체크하기 => mapp에다가 안의 값3을 바꿔서 표시
    # (3-3) 노드랑 연결된 노드들을 찾아 => 위,아래,좌,우 에서 0번만 탐색예정리스트에 추가하기 
    while will_lst:
        pop_will = will_lst.pop() #(i행,j열)
        i = pop_will[0]
        j = pop_will[1]
        print("pop_will",pop_will) # mapp i행 j열의 값을 방문했다(3) 변경하라
        # alpha=[a,b,c,d,e]  # 0번째 alpha[0]='f'
        mapp[i][j] = 3
        # (3-4) 위값이 있고(i>0), 위값이 0이면 추가
        # <다른의미>
        # 위치(인덱스)) : i행 j열
        # 위치에 있는 값(value) : 리스트[i][j]
        if i > 0 and mapp[i-1][j] == 0:
            will_lst.append((i-1,j))
        
        # (3-5) 아래값탐색 => i<마지막인덱스len -1보다 작아야합니다.
        if i < len(mapp)-1 and mapp[i+1][j] == 0:
            will_lst.append((i+1,j))
        
        # (3-6) 왼쪽탐색 : 왼쪽존재하고, 왼쪽값이 0일때 탐색
        if j > 0 and mapp[i][j-1] == 0:
            will_lst.append((i,j-1))
        # (3-7) 오른쪽탐색 : 왼쪽존재하고, 오른쪽값이 0일때 탐색
        if j < len(mapp[i])-1 and mapp[i][j+1] == 0:
            will_lst.append((i,j+1))


def dfs(i, j):
    print("탐색노드위치",i,j)
    # 방문체크
    mapp[i][j] = 3
    # 제귀함수 탈출조건 return 을 걸기

    # 넣을때 제약 - 안들어가면 함수가 끝나서탈출
    if i > 0 and mapp[i-1][j] == 0:
        # dfs 자기자신 부르기
        # will_lst.append((i-1,j))
        dfs(i-1,j)
    
    if i < len(mapp)-1 and mapp[i+1][j] == 0:
        # will_lst.append((i+1,j))
        dfs(i+1, j)
    
    if j > 0 and mapp[i][j-1] == 0:
        # will_lst.append((i,j-1))
        dfs(i, j-1)

    if j < len(mapp[i])-1 and mapp[i][j+1] == 0:
        # will_lst.append((i,j+1))
        dfs(i, j+1)




# (1) 독가스의 2 위치 찾아주세요. => i행 j열
for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        # print(mapp[i][j])
        if mapp[i][j] == 2:
            print(dfs(i, j))
            break

# 문제) mapp 독가스가 침범하지않는 0의 갯수를 구하여라
for i in range(len(mapp)):
    print(mapp[i])
    
count = 0
for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        if mapp[i][j] == 0:
            count += 1
print(count)