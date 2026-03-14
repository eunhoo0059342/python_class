# 객체
# 
'''
<예외처리>
: 프로그램에서 다양한 상황에서 나오느 에러를 갑작스럽게 프로그램을 중단시키지 않고, 처리하는 방법

try-expect
1. 형태
try: 
    에러가 발생할수도 있는 코드묶음
    => 에러가 발생할수 있는 상황 = 예외
except: 
    예외가 발생했을때, 실해앟 코드

'''

# 예제) 10을 0으로 나눴을때, 에러가 발생하면 "0으로 나눌수 없습니다." 출력하기
try:
    print(10 / 0)
    # ZeroDivisionError: division by zero
except:
    print("0으로 나눌 수가 없습니다.")


# 예제2) 입력받은 숫자로 10을 나눠보기 
# - 이때 에러가 나면 "정상적으로 나누기가 안됩니다." 라고 출력하기

# input_num = input()
# try:
#     print(10 / int(input_num))
# except ZeroDivisionError :
#     print("0으로 나눌 수가 없습니다.")
# except:
#     print("정상적으로 나누기가 되지 않습니다.")


# 구체적으로 예외를 처리하고 싶을때
# => except 에러명 :
# 예제 ZeroDivisionError 에러가면 "0으로 나눌 수가 없습니다."라고 처리하고
# 그외에는 "정상적으로 나누기가 되지 않습니다."


# 예외 처리를 해야하는 구간 => 보통 입력받을때
# => 그 외에는 조건문으로 처리 해주셔야한다.

# 핸드폰 010-0000-0000
# abcd 
# 01000000000
# 구글 폼(설문지)을 작성해서 친구들한테
# while()
# # 입력을 인한 다음에 append할수 있도록
# try:
#     int()
#     if ~~~:
#     else : (에외, 동작이 되는 예외 => 에러나 다름없어.)
#         강제로 예외발생 => raise
#         @@@@
# except:
#     @@@@


# 예제3) 숫자를 입력받고 숫자가 3의 배수가 아닌경우 "3의 배수가 아닙니다."라고 출력하기
# input_num = input()

# try:
#     if int(input_num) % 3 == 0:
#         print(input_num)
#     else:
#         # 사람은 error 컴퓨터 success
#         # # 예외에서 한번에 처리하기 처리하고싶다. => raise
#         raise Exception("NumError")

# except:
#     print("3의 배수가 아닙니다.")

# <에러의 종류>
# SyntaxError : 문법 에러
# ZeroDivisionError : 0으로 나눌때
# NameError : 변수명, 함수이름 
# TypeError : 데이터타입이 잘못된경우
# Attribute(속성)Error : 대상.메서드 잘못사용하는 경우

# 사용자정의 예외를 만들기
# raise Exception("만들 예외메세지")



# 예외가 아닐때까지 입력아서 처리하기
# 숫자를 입력받아서 3의 배수이면 숫자를 출력하고, 3의 배수가 아니면 "3의배수가아닙니다" 츨력하고 3의 배수가 될때까지 입력받으시오.
# (1)입력받기
input_num = input()

# (2)입력을 반복해서 받기
# - 내가 정상적으로 3의 배수를 입력받으면 => 반복을 안합니다.
while True:
    try: 
        # 3배수를 받으면 반복을 그만 하기 => break
        if int(input_num) % 3 == 0:
            print(input_num)
            break
        else:
            raise Exception("NumError")
    except:
        # 98번줄에 error가 발생하면 except로 이동
        print("3의 배수가 아닙니다.")
        input_num = input()



            
    