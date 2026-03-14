# 동전 O https://www.acmicpc.net/problem/11047
# 그리디 알고리즘
'''
동전의 갯수가 가장 적은 방법

10가지 4200원
1
5
10
50
100
500
1000  4장 => 4200//1000 = 4  / 남은돈 4200%1000=200
5000
10000
50000
'''

ea, num = map(int, input().split(" "))
count = 0 # 동전사용갯수
# print(ea, num)
worth_lst = []
for i in range(ea):
    input_data = int(input())
    # 좋았음
    if input_data > num:
        continue
    worth_lst.append(input_data)
# print(worth_lst)

# 4장 => 4200//1000 = 4  / 남은돈 4200%1000=200
for i in range(len(worth_lst)-1,-1,-1):
    count += num // worth_lst[i] # 동전갯수 추가(몫)
    num = num % worth_lst[i]     # 남은돈
print(count)


# <이슈: 시간초과 > 
# for i in range(len(worth_lst)-1,-1,-1):
#     while num >= worth_lst[i]:
#         num = num - worth_lst[i]
#         count += 1
# print(count)


# range(시작,끝,-1)
# for i in range(len(worth_lst)-1,-1,-1):
#     print(i)

# for i in range(len(worth_lst)):
#     print(len(worth_lst)-1-i)
# 4200 원 돈 단위 1000


# while worth_lst:
#     if num > worth_lst[len(worth_lst)-1]:
#         num - worth_lst[len(worth_lst)-1]
#         count += 1
#     else:
#         worth_lst[len(worth_lst)-1].pop()
