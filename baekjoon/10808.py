'''
알파벳 개수 https://www.acmicpc.net/problem/10808
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
'''

answer = list(input())
# answer = "beakjoon"
alphabet_num = {'a':0, 'b':0, 'c':0, 'd':0,'e':0,'f':0,'g':0, 'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
# print(answer)
# print(alphabet_num)
# list_1 = alphabet_num.items

# 딕셔너리 반복
for k,v in alphabet_num.items():
    # o 가 "beakjoon" 안에 있어? 
    # print(k,v)
    if k in answer:
        # 1이 아니라, 있는 갯수 
        alphabet_num[k] = alphabet_num[k] + answer.count(k)

resert = ''
c = list(alphabet_num.values())
for i in range(len(c)):
    resert += str(c[i]) + ' '
print(resert)


####### 문자로 반복을 돌리고 ########
for i in range(len(answer)):
    print(answer[i])
    k = answer[i]
    # 이 문자를 alphabet_num의 key로 활용하기
    alphabet_num[k] = alphabet_num[k] + 1
print(alphabet_num.values())