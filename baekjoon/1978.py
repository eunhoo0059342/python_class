'''
https://www.acmicpc.net/problem/1978
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
'''

# 소수 : 1과 자기자신만이 약수로 갖는 수
#  => 1과 자기자신 빼고는 나눴을때 나머지 0이 아니여야한다.
#  => 1은 소수가 될 수 없다.



num = int(input())
num1 = input().split(" ")
# print(num1)

# 소수를 판단하는 함수
# 입력 : 숫자
# 결과 : 소수이면 True 아니면 False

# num 13 나눴을때 나누어떨어지는 수가 1과 자기 자신이면 된다.
# -> 맨앞과 맨뒤를 제외하고 나눴을때, 나누어떨어지면 안된다.
# -> 2, num
def prime_num(n):
    # 2~num앞까지 반복해서 나눠보기 
    #print("--",num)
    # 만약에 num이 1이면, 바로 False
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


b = 0
for i in range(num):
    p = prime_num(int(num1[i]))
    if p == True:
        b += 1
print(b)
