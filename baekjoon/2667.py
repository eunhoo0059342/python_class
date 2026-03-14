# 단지번호붙이기 https://www.acmicpc.net/problem/2667
# => dfs

from collections import deque
from turtle import write_docstringdict

w_h = int(input())

m_lst = []

for i in range(w_h):
    m_lst.append(list(map(int, input())))

print(m_lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def loute(s_x. s_y):
    
    return [s_x, s_y]
print(loute(1,1))