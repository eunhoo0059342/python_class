'''
https://www.acmicpc.net/problem/1157

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
'''
input_word = input()

alpha_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, 'T': 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

s_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
b_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in range(len(input_word)):
    for j in range(len(s_alpha)):
        if input_word[i] == s_alpha[j] or input_word[i] == b_alpha[j]:
            alpha_dict[b_alpha[j]] += 1

# 추천 코드
# - 대소문자 구분없을때는 입력값을 대문자, 또는 소문자로 변환 해서 접근하면 좋습니다.




# 최대값최솟값을 구하는 알고리즘 방식
# max
# min
# 최댓값 = 7
# [1,2,7,4,5]

#################################
# 1. value 최댓값
# - 딕셔너리중에서 아무값
# 2. 최대value를 갖는 key 리스트
# - 더 큰 최대값이 있으면 교체이다.
# - 같으면 max_key_lst 요소추가

max_value = alpha_dict["A"]
max_key_lst = ["A"]
# 9
# ['T']
for k,v in alpha_dict.items():
    # (1) 딕셔너리 v랑 max_value랑 비교해서 더 큰값으로 교체(저장하기)
    # print(v)
    if k=='A':
        continue

    if max_value < v:
        max_value = v
        max_key_lst = [k]
    elif max_value == v:
        max_key_lst.append(k)

if len(max_key_lst) >= 2:
    print("?")
else:
    print(max_key_lst[0].upper())
