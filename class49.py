# 유전자 편집 - 회문 찾기

# <회문>
# ATGTA
# 0   4
#  1 3
#   2
#data 
genetic_string = 'ATGTAATGGTTGCAGTCAATTGATGTCGTGCTCGAGCTGCAGCTAGCGATCGAGGCTTCCAGCGTAGCGTAGCGCGGTACGTCA'
                # 0번째 ATGTA
                #  1번  TGTAA
                #        ATGGT  



# 1. 첫글자부터 ~ 5글자씩 글자씩 잘라서 출력해주세요.

# <반복문의 형태>
# for 문      -> 횟수      => 반복변수 i가 for문안에서 정의
# while 문    -> 특정 조건  => 반복변수가 정의되어있지않다. => 내가 직접 정의해서 만들어야합니다.  

def judge(s):
    if len(s) == 5:
        # if s[0] == s[4]:
        #     if s[1] == s[3]:
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False


        #예)) 
        # 5글자 2글자씩 같은지 검사하는 횟수는 2번
        #    6글자 3번
        #    7글자 3번

        # 
        for i in range(len(s)//2):   #i=0~1
            # 반복하고싶은거 => 대상, i를 활용해서
            # s의길이=5
            # i=0 - 4
            # i=1 - 3
            if s[i] == s[len(s)-(i+1)]:
                continue
            else:
                return False
        return True
    else:
        return

# 슬라이싱 => 변수이름[시작번호:끝번호] : start번호부터 end번호까지 구간을 자르는 명령어 
true_lst = []
# (1-1)앞값이 바뀌는 순가 => 전체길이에서 -4개전까지만 가능~
for i in range(len(genetic_string)-4):  
    # (1-2)앞값을 기준으로 5글자를 자르는 구간
    # print(genetic_string[i])
    s = ''
    # 반복변수 j
    j = i
    while len(s) < 5:
        s += genetic_string[j]
        j += 1
    # print(s,end="")
    # 회문인지 아닌지 판단하기 => judge(데이터)
    # print(judge(s))
    # True 인것만 모아서 리스트 만들기

    if judge(s):
        true_lst.append(s)
        print(s)
print(true_lst)
    
    # # (2) i번부터 5개씩 출력하는 슬라이싱을 작성해주세요~!
    # print(genetic_string[i:i+5])


    # 2. 회문인지를 판단 => 함수
    # - n개의 글자를 갖는 문자열이 필요 
    # - 회문이면 True 아니면 False 결과로 내보내기


# s1 = 'ATGTA' # => 값이 회문인지
#     # 0   4
#     #  1 3
#     #   2
#     # 5글자를 2글자씩 같은지 검사하는 횟수는 2번
# s2 = 'TGTAA'










print("mission 2 -------")
# 회문인값을 출력하기
genetic_string = 'ATGTAATGGTTGCAGTCAATTGATGTCGTGCTCGAGCTGCAGCTAGCGATCGAGGCTTCCAGCGTAGCGTAGCGCGGTACGTCA'
# /ATGTA/ATGGTTGCAGTCAATTGATGT/CGTGC/
# 앞의 회문 마지막번호+1 ~ 다음회문 첫글자전까지

first_index_lst = []
for i in range(len(genetic_string)-4):
    # 5개씩 슬라이씽 한 값이 회문(ture_list)안에 있는지를 체크하기 
    if genetic_string[i:i+5] in true_lst:
        # 각 회문의 첫번째값의 인덱스번호가 저장된 리스트만들어주세요.
        print(genetic_string[i:i+5], i, i+5)
        first_index_lst.append(i)
print(true_lst)
print(first_index_lst)

# 회문사이의 데이터 몇구간 일까? (회문은 6개, )
# 과졔) 회문사이의 문자열 찾아주세요~! => 슬라이싱 잘 쓰면 쉽고
# ['ATGTA', 'CGTGC', 'GCTCG', 'CGAGC', 'AGCGA', 'GCGCG']
# [0, 26, 29, 32, 44, 71]
# 회문은 6개 회문사이는? 5번
# 0~26번사이 / 
for i in range(len(first_index_lst)-1):
    front_num = first_index_lst[i]+len(true_lst[i])
    back_num = first_index_lst[i+1]
    print(front_num, back_num)
    # 구간 슬라이싱
    print(genetic_string[front_num:back_num])






# <연습과제>
# 숫자의 개수 https://www.acmicpc.net/problem/2577
# 더하기 사이클 https://www.acmicpc.net/problem/1110