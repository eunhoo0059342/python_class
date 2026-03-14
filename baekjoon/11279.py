'''
최대 힙 https://www.acmicpc.net/problem/11279

''' 

import heapq
import sys

input = sys.stdin.readline
# 숫자가 클수록 작아지는 개념 : -7 -10
n = int(input())
q = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(x)
        else: 
            max_q = heapq.heappop(q)
            print(-1 * max_q)
    else:
        heapq.heappush(q, -1 * x)
            