'''
과제 안 내신 분..? https://www.acmicpc.net/problem/5597

X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다
교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다
'''
# 실수) 30번 체크가 안되는 경우 실수가 나게 됩니다.
# 리스트의 갯수는 28개 / 28번 돌리면 30번을 체크하기 어렵다. 
# => 입력 갯수에 대한 반복보다는 번호 초점 맞춰서 1~30 나오게 반본을 돌려서 체크


# range(start,end) : 연속된 정수를 갖는 함수, 1~30까지
# list() : 여러가지 데이터에 대해서 리스트로 변환하고 싶다.
# num_list: 과제 미제출 리스트
num_list = list(range(1,31))
for i in range(28):
    answer = int(input())
    # 입력을 받으면 과제 미제출 리스트에서 해당 번호를 삭제
    # => .pop() : 인덱스로 삭제 
    # => .remove("찾는값") : 값을 찾아서 삭제
    num_list.remove(answer)

#print(num_list)
for i in range(len(num_list)):
    print(num_list[i])

 



# answer_list = []
# j = 0
    # answer_list.append(int(input()))
# print(list(sorted(answer_list)))
# sorted_answer_list = sorted(answer_list)
# for i in range(28):
#     print(sorted_answer_list[i], j + 1)
#     if sorted_answer_list[i] != j + 1:
#         print(sorted_answer_list[i] - 1)
#         j += 1
#     j += 1
