'''
https://www.acmicpc.net/problem/10845

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
'''
from collections import deque
# (1) 초기 deque를 생성하기
# 큐변수 = deque([]) 
# (2) 오른쪽추가 .append("추가할내용")
#     왼쪽추가   .appendleft()
# (3) 오른쪽맨끝삭제 .pop()
#     왼쪽맨끝삭제  .popleft() 

input_num = input()
lst = []
que = deque([])

# 입력처리 => 리스트 관리
# 받은거 그대로 저장하기
for i in range(int(input_num)):
    input_data = input()
    lst.append(input_data.split(" "))

# lst => 이차원리스트
for i in range(len(lst)):
    # print(lst[i])
    # ['front']
    if lst[i][0] == "push":
        que.append(lst[i][1])
    elif lst[i][0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif lst[i][0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif lst[i][0] == 'size':
        print(len(que))
    elif lst[i][0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif lst[i][0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            pop_num = que.popleft()
            print(pop_num)
# print(que)

# 4줄 => 삼항연산자 조건 ? true일때 :false일대
# 삼항연산자 => 데이터만 나오는 경우
# 변수 = 참일때값 if 조건문 else 거짓일때값

if len(que) == 0:
    print(-1)
else:
    print(que[0])

answer = -1 if len(que) == 0 else que[0]
print(answer)





