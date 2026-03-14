# Queue(큐): FIFO구조(first in first out)
#   ----------------             => 먼저들어간 먼저 나옵니다.
# <-out            <-in          => enqueue : 넣는기능
#   ----------------             => dequeue : 빼는 기능  => pop(0): 성능적으로 굉장히 안좋다
                              #  => 사이즈체크하는 메서드 (size)
from collections import deque

# 학년 100명 한줄로 세웟어
# - 옆으로 이동하기를 98명 => 컴퓨터 하기
# 0   0 0 0 0 0 0 0 
 
# 큐는 모듈로 사용하기
# collection모듈에 deque클래스를 사용할것이다.(디큐, 데크, 덱) 
# from collections import deque

# (1) 초기 deque를 생성하기
# 큐변수 = deque([]) 
# (2) 오른쪽추가 .append("추가할내용")
#     왼쪽추가   .appendleft()
# (3) 오른쪽맨끝삭제 .pop()
#     왼쪽맨끝삭제  .popleft() 
que = deque([2,3])
que.append('1')
print(que)
que.appendleft('0')
print(que)
que.pop()
print(que)
que.popleft()
print(que)

# https://www.acmicpc.net/problem/10845