'''
문자열 반복 https://www.acmicpc.net/problem/2675
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고,
두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.


입력) 
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

ex) 
2
-----
3 ABC
5 /HTP

'''

# 문자를 반복하는 함수
# 허용하는 문자 : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:
def str_code(s):
    # s[0] 몇번반복횟수 => 변수
    # s[1] 반복할 문자열 => 변수
    a = ''
    b = int(s[0])
    c = s[1]
    #print(b,"문자열반복횟수",c,"반복할 문자")
    # c='ABCD'
    # ABCD ABCD ABCD
    # 2AAA BBB CCC DDDD => c의 길이만큼 반복
    for i in range(len(c)):
        # c[i]가 허용하는 문자(0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:)에 들어가잇으면 반복한다.
        if c[i] in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:":
            a += c[i] * b

    # for i in range(len(s)-1):
    #     # print(s[i] * int(s[0]))
    #     if s[i] != " " or s[i] not in num == True:
    #         a += s[i] * int(s[0])
    #         # print(s[i])
    #     i = i + 1
    return a

# 문제가되는부분 : 주어진 입력과 맞지 않기때문에 오답
# (1) 첫번째줄 테스트갯수 T 입력받기> 숫자타입으로 받기
# (2) 테스트 갯수(t)만큼 입력받기
# (3) 문자열을 반복하는 함수str_code를 만들어보기
# 3 ABC => ['3','ABC']
#          ['A','B','C']
# 115 ABC  ['115','ABC']
t = int(input())
for i in range(t):
    print(str_code(input().split(" ")))