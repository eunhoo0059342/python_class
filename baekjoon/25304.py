'''
영수증 https://www.acmicpc.net/problem/25304

<문제>
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,

구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.


<입력>
첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.


260000   # 총금액 X
4        # 물건의 종류 N
20000 5
30000 2
10000 6
5000 8


260000     # 총금액 X -> 무조건 숫자 타입 바로 int(input()) 사용하면 편하다.
100        # 물건의 종류 갯수 N => 무조건 숫자타입
20000 5
30000 2
'''


# 무조건적으로 되는 것은 정적
# 입력하는 값에 따라서 언제는 1개 언제는 5개 언제는 100개 동적 

# x = int(input())
# n = int(input())

# input_data = []
# # n의 갯수만큼 (반복해서) 밑에 가격을 입력받을 거다.
# for i in range(n):
#     a = input()
#     input_data.append(a)
# # 입력데이터가 리스트형태로 모여서 
# print(input_data)

# 리스트축약형
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# arr = []
# for i in range(100):
#     arr.append(0)
    

# print(arr)

# 조건을 만족하는 리스트를 축약해서 쉽게 생성하는 기능
# [{표현식} for {변수} in {반복자/연속열} if {조건표현식}]
# print([0 for i in range(100)])

# 예제 ) 입력을 5개 받은것으로 리스트만들고싶어요.
# print([int(input()) for i in range(5)])

# 예제 ) 입력이 한줄에 여러개 들어오면 split() 도 안에서 축약형 사용이 가능하다.
# print([input().split(' ') for i in range(5)])

# print([i for i in range(10) if i%2==0])




#예제1) 1~30까지의 리스트를 만들어주세요.
# a = []
# for i in range(30):
#     a.append(i + 1)
#     i = i + 1
# print(a)
# 예제2) 여러줄 입력이 들어올때, 띄어쓰기를 기준으로 split()해서 이차원리스트로 만들어주세요.
# 20000 5
# 30000 2
# 10000 6
# 5000 8
# input_data = []
# for i in range(n):
#     b = input().split(" ")
#     input_data.append(b)
# print(input_data)

# 예제3)  0~50까지 중에서 3의 배수만 이루어지게 리스트를 만들어주세요.(조건까지~)
# c = []
# for j in range(50):
#     # print(j+1)
#     j = j + 1
#     if j % 3 == 0:
#         c.append(j)
# print(c)
#############여기까지가 문제 입력받기###################
x = int(input())
n = int(input())

input_data = []
b = []


for i in range(n):
    a = input().split(" ")
    input_data.append(a)
    b.append(int(input_data[i][0]) * int(input_data[i][1]))
if x == sum(b):
    print("Yes")
else:
    print("No")



    




# https://www.acmicpc.net/problem/2480









