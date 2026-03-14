'''
팩토리얼2 https://www.acmicpc.net/problem/27433
# - 재귀함수로 푸세용
'''
# 7! = 7*6*5*4*3*2*1
# 7! = 7*6!
# 0!

n = int(input())

# factorial(1) 1*None
def factorial(n):
    # 종료지점은 자기자신을 더이상 부르면 안됩니다.
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))