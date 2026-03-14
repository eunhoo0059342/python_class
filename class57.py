# route= [  
# [1,9,1,1,1,1,1,1],
# [1,0,1,0,0,0,0,1],
# [1,@,0,0,1,1,0,1],
# [&,*,%,1,1,1,0,1],
# [1,$,0,0,0,0,0,1],
# [1,0,1,1,1,1,1,1],
# [1,0,0,0,0,0,0,5],
# [1,1,1,1,1,1,1,1]]



# # 현재 위치 :   i, j         (3,1)
# # 위값 위치 :   i-1, j       (2,1)
# # 아래값 위치:   i+1, j       (4,1)
# # 왼쪽값 위치:   i, j-1       (3,0)
# # 오른쪽값위치:   i, j+1       (3,2)

############################################

# 0 ~ 6
# 0 공간 <-감시공간
# 1~5 : 여러가지 CCTV종류
# 6 : 벽위치

# => cctv가 감시할수 있는 범위 7변경하기
# => 7이 아닌 0번 감시사각지대가 된다.


#data
#initial condition
from stringprep import map_table_b2
from numpy import append


camera_list=[1,2,3,4,5]
map_data=[]
map_string=[
    "2 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 6 6 6 6",
    "6 6 6 6 6 6 6 6 6 6 6 6 6 0 6 0 6 0 0 0",
    "1 0 0 0 0 0 0 6 0 0 0 0 6 0 6 0 0 0 5 0",
    "0 6 5 0 0 5 0 6 0 5 0 0 6 0 6 0 6 0 0 0",
    "0 6 0 0 0 0 0 6 0 0 0 1 6 0 6 0 6 2 0 0",
    "0 6 0 0 0 0 0 6 2 0 0 0 6 0 6 0 6 6 6 6",
    "0 6 6 6 6 6 6 6 0 0 0 0 6 0 6 0 0 0 0 2",
    "0 0 0 0 0 0 0 0 0 0 0 2 6 0 0 0 6 6 6 6",
    "0 0 5 0 0 5 0 0 0 5 0 0 6 0 6 0 6 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 6 0 6 0 6 0 5 0",
    "6 6 6 6 0 0 6 6 6 6 6 6 6 0 0 0 6 0 0 0",
    "0 5 0 6 0 0 6 0 0 0 2 0 0 0 6 0 6 0 5 0",
    "0 0 0 0 0 0 6 4 0 0 0 0 0 0 6 0 6 0 0 0",
    "0 5 0 0 0 0 6 0 0 0 0 5 0 0 6 2 0 0 0 0",
    "0 0 0 6 0 0 6 0 5 0 0 0 0 0 6 0 6 0 5 0",
    "3 0 0 6 0 1 6 0 0 0 4 0 0 3 6 1 6 0 0 0"
]


# (1) 이차원리스트로 만들어주세요!
lst = []
for i in range(len(map_string)):
    # lst2 = list(map(int,map_string[i].split()))
    lst2 = []
    for j in range(len(map_string[i])):
        if map_string[i][j] == ' ':
            continue
        lst2.append(int(map_string[i][j]))

    lst.append(lst2)
print(lst)
# b = [list(map(int,map_string[i].split())) for i in range(len(map_string))]

# print(b)
# 리스트 축약형
# - 반복문을 사용해서 리스트를 만든다 
# [값 for 문]
# a = [i*2 for i in range(100)]
# print(a)


#------------------------
# (1)lst에서 1~5까지 의 감시카메라를 찾아보기

# cctv번호를 받아서 lst에 감시구역을 찾는 함수 
# - 입력 : cctv 위치 (행,열), cctv번호
# - 결과 : 결과 없음

def find_cctv(i, j, cctv_num):
    '''
    3.10번전때 if문비슷한 조건문등장 => 다른프로그래밍 언어(switch case)에는 있으나, 파이썬에 없었는데 
    match ~ case 
    match 기준변수:
        case 경우1:
            경우1일때 쓸코드
        case 경우2:
        ...
    '''
    # cctv 번호(cctv_num, 기준 변수)에 따라서 하는 행동을 다르게 하기
    # 1 : 좌우
    # 2 : 상하
    # 3 : 우상좌하 오른쪽 위 대각선
    # 4 : 좌상우하 왼쪽 위 대각선
    # 5 : 모든방향
    match cctv_num:
        case 1:
            print("cctv 1 - 상하")
            # 위체크
            up_check(i, j)
            # 아래체크
            down_check(i,j)
        # case 2:
        #     print('cctv 2 - 좌우')
        #     # 좌체크
        #     # 우체크
        # case 3:
        #     print('cctv 3 - 우상좌하')
        #     # 오른쪽 위체크
        #     # 왼쪽 아래 체크
        # case 4:
        #     print('cctv 4 - 좌상우하')
        #     # 왼쪽위체크
        #     # 오른쪽아래체크
        # case 5:
        #     print('cctv 5 - 전방향')
        #     # 위체크
        #     # 아래체크
        #     # 좌체크
        #     # 우체크
        #     # 오른쪽 위체크
        #     # 왼쪽 아래체크
        #     # 왼쪽 위체크
        #     # 오른쪽 아래체크

# 8개의 체크사항을 함수로 만들기
# - cctv 위치(행,열)
def up_check(i, j):
    print(i,j,lst[i][j])
    # 1) 인덱스 맨첫번째줄까지 변경이 가능 i>=0이면 반복하기
    # 2) 6벽을 만나기 전까지 반복(안만나면 탐색, 만나면 탐색 스톱)
    # 3) 위로 올라가면서 현재값을 7로 바꾸기(행값을 -1씩)
    # 4) 감시카메라가 나오면 변경하기 전에 넘어가기(다음반복으로 바로 이동하기)
    #  - 감시카메라가 아니면 7로 변경하기
    while i >= 0:
        if lst[i][j] == 6:
            break
        elif lst[i][j] >= 1 and lst[i][j] <= 5:
            i -= 1
            continue 
        lst[i][j] = 7
        i -= 1

def down_check(i,j):
    while i <= len(lst)-1:
        if lst[i][j] == 6:
            break
        elif lst[i][j] >= 1 and lst[i][j] <= 5:
            i += 1
            continue
        lst[i][j] = 7
        i += 1

# TODO : 좌,우, 우상,좌하, 좌상,우하 만들어오기




for i in range(len(lst)):
    # print(lst[i])
    for j in range(len(lst[i])):
        # print(lst[i][j])
        if lst[i][j] >=1 and lst[i][j] <= 5:
            # print('cctv', lst[i][j])
            find_cctv(i, j, lst[i][j])
            # CCTV번호에 맞춰서 탐색을 다르게 하기 => cctv번호를 받아서 감시구역을 찾는 함수 
    


for i in range(len(lst)):
    print(lst[i])


# 청소년 데이터활용공모전 ~ 11.18(목)
# https://www.kywa.or.kr/pressinfo/notice_view.jsp?no=35625



