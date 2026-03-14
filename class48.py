'''
재귀함수(Recursive Function) : 함수 내부에서 자기 자신을 호출하는 함수
- return 에서는 자기자신을 호출하기
- 종료 조건을 추가해야합니다.
- 큰문제를 작게작게 쪼개서 해결할때 사용하게 된다.
=> 스택 구조
''' 
num = 0
# num 1씩 더해서 출력하기 -> 내가 num 500이 되면 그만하자
# return 나 자신을 호출신 
def recursive(num):
    num += 1
    
    # print(num)
    if num == 500:
        return num
    else:
        return recursive(num)

print(recursive(num))
# RecursionError: maximum recursion depth exceeded
# => 오버플로우 : 


# 다음시간에 풀어보도록 => 목요일 5시
# 피보나치 수열 : i+2번째는 = i+1 + i
# 1 2 3 5 8 13 21 34 55 ...


# https://www.acmicpc.net/problem/2747


# 가로 길이 128, 96 최대공약수  => 32
# 세로 길이 96, 10    => 10

# A 가로 128, 세로 96
# 

print("mission---------------")

# 최대공약수 만드는 함수
# (1) 숫자 2개가 주어진다.
# (2) n1/ n2를 나눴을때 나머지가 0이될때까지 나눌겁니다.
#  ---- 나머지가 1이 아닌경우, n2와 나머지와의 최대공약수를 구한다.
#  ---- 나머지가 0일 경우, n2(나눈숫자)가 최대공약수(정답)가 됩니다.

a, b = list(map(int, input().split(' ')))

def greatest(a, b):
    if a % b == 0:
        return b
    else:
        return greatest(b, a % b)
print(greatest(a, b))