'''
https://www.acmicpc.net/problem/1806    
'''


n, s = list(map(int, input().split(" ")))
num_lst = list(map(int, input().split(" ")))

s_idx = 0
l_idx = 0
num = 0
length = 0
ex_length = 0


while l_idx < n:
    print(num, "  / 시작",s_idx,"끝",l_idx, '길이', length)
    if num == s:
        length = l_idx - s_idx
        l_idx += 1
    elif num > s:
        num -= num_lst[s_idx]
        s_idx += 1
    elif num < s:
        l_idx += 1
        num += num_lst[l_idx]

    if ex_length < length:
        ex_length = length



print(ex_length)
