# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# for i in range(a):
#     # print("*" * a)
#     b = ("*" * a).split("\n")
#     print(b)


#    *********   0번째 띄어쓰기 0개
#   ()*******()  1번째 띄어쓰기 1개
#  ()()*****()()
#       ***
#()()()()*
# ()()()***     0번째 띄어쓰기 3개
#      *****    1번째 띄어쓰기 2개
#     *******
#    *********

star = int(input())
a = star * 2 - 1  # 시작 줄의 별의 갯수 

for i in range(star):  
    print(' ' * i +("*" * a))
    a = a - 2
    
a = 3
for i in range(star-1):
    print(' ' * (star - i-2) + ("*" * a))
    a = a + 2



########## 선생님 답안 ##########
a = star * 2 + 1  # 시작 줄의 별의 갯수 
for i in range(star):
    a = a - 2
    print(' ' * i +("*" * a))
for i in range(star-1):
    a = a + 2
    print(' ' * (star - i-2) + ("*" * a))
    




# https://www.acmicpc.net/problem/25304
