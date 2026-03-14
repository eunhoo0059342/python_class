'''
요세푸스 문제 https://www.acmicpc.net/problem/1158

요세푸스 문제는 다음과 같다.
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
'''

# 순열 : 순서대로 나열(nPr)
# 제거되는 순서를 기록하기
# from collections import deque



input_data = input().split(" ")
n = int(input_data[0])
k = int(input_data[1])
lst = []
index = 0

# 연속된 정수 리스트 만들때 Tip) list(range(범위))
que = list(range(1,n+1))

for i in range(n):
    # index += (k-1)
    index = (index+(k-1)) % len(que)
    # print("제거할번호",index)
    # que.pop(index)
    lst.append(que.pop(index))
    # print(que)

rep_lst = str(lst).replace('[', '<').replace(']', '>')
print(rep_lst)


# que = []
# for i in range(n):
#     que.append(i+1)

# def form_circle(que, n):
#     for i in range(n):
        

# def pop_people(que, k):
#     pop_data = que.pop(2)
#     lst.append(pop_data)

# form_circle(que, n)
# print(que)
# pop_people(que)
# print(que)
# print(lst)

# count =0
# while count <= 10:
#     count +=1
#     # 탈출 조건
#     form_circle(que, n)
#     pop_people(que, k)
#     print(que)
#     if len(que) == 0:
#         break

# print(lst)