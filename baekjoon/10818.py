'''
https://www.acmicpc.net/problem/10818
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''
answer = input()
num = input().split(" ")
num2 = []
for i in range(int(answer)):
    num2.append(int(num[i]))
# print(num2)
print(min(num2), max(num2))