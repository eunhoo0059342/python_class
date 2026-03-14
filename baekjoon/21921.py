# 블로그 https://www.acmicpc.net/problem/21921
# => 누적합 (구간이 안주어져서 여러개의 구간을 체크 해야할때)
# => 
'''
슬라이딩 윈도우
: 구간이 정해져있을때, 구간의 크기만큼 리스트만들어서 데이터를 넣다 뺐다 하는 알고리즘

구간 2
[5,1] <- 큐사용(오른쪽에서 들어오고, 왼쪽으로 빠진다.)
1 4 2 5 1
'''
'''
문제)
찬솔이는 X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
찬솔이를 대신해서 X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

입력)
첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

출력
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.

제한
'''

from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write()

n, x = list(map(int, input().split(" ")))
day_visit = list(map(int, input().split(" ")))

# print(n, x)
# print(day_visit)

# x 간격을 저장할 초기 윈도우를 만들기 (초기 맨앞부터 x개만큼)
# 슬라이싱 :  변수이름[시작:끝] (맨앞부터 시작하면 0은 빼도 된다.)

# day_visit 탐색하면서 윈도우를 넣다(append) 뺐다(popleft)
# 5 2
# 초기윈도우 0~1 들어가 있어
# 반복 시작은 하나 빼고 x(2)부터들어가 
# 윈도우가 [4,2][2,5][5,1]로 바뀌도록 코드를 만들어주세요.

# 최대값알고리즘
# : 임시 최대값을 정하고 반복돌리면서 최대값보다 큰 수를 찾아서 교체 

w = deque(day_visit[:x])
# 같은 최대값이 몇개 나오냐?
max_sum = sum(w)
count = 1

for i in range(n-x):
    w.popleft()
    w.append(day_visit[x+i])
    if max_sum < sum(w):
        # 새로운 큰애가 나오면 카운트 초기화
        max_sum = sum(w)
        count = 1
    elif max_sum == sum(w):
        count += 1
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)