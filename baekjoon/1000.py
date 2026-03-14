#백준알고리즘 문제 baekjoon폴더 > 문제번호.py 파일생성하기

'''
A+B : https://www.acmicpc.net/problem/1000

문제)
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력)
1 2
'''


# 변수 = input() :  한줄 입력하기 
# - 입력한 값은 항상 문자열 데이터

########################
# 예제) 숫자 10을 입력받아서 1을 더한값을 출력해주세요.

# answer = int(input())  # <- 입력받으값이 무조건 숫자일때, int(input())
# print(int(answer) + 1)
# TypeError: can only concatenate str (not "int") to str


########################
"1 2"

# 문자열을 쪼개서 리스트타입으로 변경하는 방법
# => 문자열변수.split("구분인자")


# 예제) "1 2"를 입력받아서, 리스트 변환해주세요.
# answer = input().split(" ")
# print(answer)
# new_num = []
# for i in range(len(answer)):
#     print(int(answer[i]))


# 누적합계 
#(1)합(숫자을 저장할 변수를 하나만 만들기 
#(2)0으로 초기화
#(3) 더
answer2 = input().split(" ")
num = 0
for i in range(len(answer2)):
    #print(int(answer2[i]))
    num += int(answer2[i])
print(num)
#eunhoo345427
    









