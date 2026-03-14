'''
최소힙 https://www.acmicpc.net/problem/1927

입력)
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.

만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
x는 231보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.

출력)
입력에서 0이 주어진 횟수만큼 답을 출력한다. 
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.


heap - 우선순위 큐
     - 트리구조
heap 모듈을 import
(1) 리스트를 heap구조(트리)로 만들고싶다.
heapq.heapify(리스트)
(2) 삽입
heapq.heappush(큐이름,넣는데이터)
(3) 추출
heapq.heappop(큐이름)

'''
'''
표준입출력
- 우리는 키보드가 표준입력
- 알고리즘 채점 파일을 읽어서 채점

input() , print() 키보드를 통해서 콘솔로 받는것만 최적화

sys 모듈
- sys.stdin.readline()
- sys.stdout.write("쓸내용")

<함수를 새로운 이름으로 변경>
변경할 함수이름 = 기존함수이름
'''


import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write
# - 개행X => \n
# - 문자열 변경해줘야 출력이된다. => f-string
# - 엄청 빠름

'''
<문자의 포맷팅>
1. f-string

2. 문자열포맷코드
%d : 정수
%f : 실수
%s : 문자열
print("%d" %숫자변수)
'''

n = int(input())
q = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(f"{x}\n")
        else:
            # 추출X 제일작은값을 알고싶어 => 0번째 가장 작다=> q[0]
            min_q = heapq.heappop(q)
            print(f"%d\n" %min_q)
            
    else:
        heapq.heappush(q, x)
# print(q)  