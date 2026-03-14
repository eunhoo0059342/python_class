'''
럭비클럽 https://www.acmicpc.net/problem/2083

문제)
올 골드 럭비 클럽의 회원들은 성인부 또는 청소년부로 분류된다.
나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부이다. 그 밖에는 모두 청소년부이다. 클럽 회원들을 올바르게 분류하라.


입력)
각 줄은 이름과 두 자연수로 이루어진다. 두 자연수는 순서대로 나이와 몸무게를 나타낸다. 
입력의 마지막 줄은 # 0 0 이다. 이 입력은 처리하지 않는다.
이름은 알파벳 대/소문자로만 이루어져 있고, 길이는 10을 넘지 않는다.

Joe 16 34
Bill 18 65
Billy 17 65
Sam 17 85
# 0 0

'''

# for <= 횟수 반복

# # 조건이 만족하면 반복
# while True : 
#     반복할 코드

#####
# 문제에서는  # 0 0 이 마지막 줄이다. 
#   => 마지막줄에 # 0 0 입력을 종료한다. 
# (1) 항상 만족하는 while문을 만들어준다.
# - 무한 반복: 무한반복은 절대 안된다. why? 다음 코드를 절대 할수없기때문에, 종료도 안된다.

# 입력리스트 저장해주시면된다.
input_list = []
while True:
    # 무한반복 탈출 조건을 걸어서 반복문을 끝내주기 => break : 반복문 탈출
    answer = input().split(" ")
    # 탈출조건
    if answer == "# 0 0".split(" "):
        break
    # 탈출조건 외
    input_list.append(answer)
for i in range(len(input_list)):
        if int(input_list[i][1]) > 17 or int(input_list[i][2]) >= 80:
            print(input_list[i][0], "Senior")
        else:
            print(input_list[i][0], "Junior")

# print(input_list)
# a = input().split(" ")
# b = input().split(" ")
# c = input().split(" ")
# d = input().split(" ")
# e = input().split(" ")
# aa = {"이름": a[0], "나이": int(a[1]),"몸무게": int(a[2])}
# bb = {"이름": b[0], "나이": int(b[1]),"몸무게": int(b[2])}
# cc = {"이름": c[0], "나이": int(c[1]),"몸무게": int(c[2])}
# dd = {"이름": d[0], "나이": int(d[1]),"몸무게": int(d[2])}
# if aa["나이"] > 17 or aa["몸무게"] >= 80:
#     print(aa["이름"], "Senior")
# else:
#     print(aa["이름"], "Junior")

# if bb["나이"] > 17 or bb["몸무게"] >= 80:
#     print(bb["이름"], "Senior")
# else:
#     print(bb["이름"], "Junior")
# if cc["나이"] > 17 or cc["몸무게"] >= 80:
#     print(cc["이름"], "Senior")
# else:
#     print(cc["이름"], "Junior")
# if dd["나이"] > 17 or dd["몸무게"] >= 80:
#     print(dd["이름"], "Senior")
# else:
#     print(dd["이름"], "Junior")

