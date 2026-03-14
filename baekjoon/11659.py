# 구간합 구하기4 https://www.acmicpc.net/problem/11659
'''
문제)
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 
둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

제한) 시간제한 1초
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

입력예제)
5 3         # 숫자갯수 테스케이스횟수
5 4 3 2 1   # 숫자리스트(공통 데이터)
1 3         # 구간 i j  1 2 3
2 4         # 구간 i j  2 3 4
5 5         # 구간 i j
1 4         # 1 2 3 4
# => 공통데이터를 사용해서 구간을 각자 구하면 중복된 처리를 하는 경우가 많다.
# => 중복처리를 줄일려면 어떻게 해야할까? 이번 문제의 알고리즘 이다.
# => 다이나믹프로그래밍(동적계획법)

# - 누적합 : 공통데이터가 주어지고, 구간에 대한 합을 구할때
        5 4 3 2 1
누적합   [5,9,12,14,15]
구간 1 3: 1~3까지의 누적합의 2번째
구간 2 4: 2~4구간 = 1~4구간의 합 - 1~1까지의 구간 합 = 2~4까지 구간
'''


# 시간복잡도 : 알고리즘 문제를 풀때 연산수행이 얼마만큼 걸릴까? 시간 척도
# - 연산했을때 가장 좋은 성과 : 오메가 표시법 테스트케이스가 1
# - 연산했을때 평균적인 성과  : 세타 표시법  테스트케이스가 50000
# - ✅️ 연산했을때 가장 나쁜 성과 : 빅오 표시법  테스트케이스가 100000
#  https://blog.kakaocdn.net/dna/s0pox/btq6Mbphdwr/AAAAAAAAAAAAAAAAAAAAADTkvh0sfj753Srh45X75ZPkv1RtI_4JmzaJG6QPehjZ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1769871599&allow_ip=&allow_referer=&signature=LTOjYs20UOFVIyONgKQP7BQjkas%3D

# (1) O(1) : 상수시간
# 입력에 상관없이 일정하게 연산하는것
# (2) O(logN): 로그시간
# for i in range(0,n,**2): # n입력하면 n의 갯수만큼 반복

# (3)O(n): 선형시간
# => 일반 for문
# for i in range(n): # n입력하면 n의 갯수만큼 반복

# (4)o(n^2) : 2차 시간 
# => 이중for문
# # for i in range(n): 






from numpy import s_


n, m = map(int, input().split(" "))
num_lst = list(map(int, input().split(" ")))
# 누적합 리스트을 구하기 >>> [5,9,12,14,15]
num = 0
sum_lst=[]
for i in range(n):
    num = num + num_lst[i]
    # print(num)
    sum_lst.append(num)
print(sum_lst)

# 구간 1 3: 맨앞부터 1~3까지의 누적합의 2번째
# 구간 2 4: 중간 2~4구간 = 1~4구간의 합 - 1~1까지의 구간 합 = 2~4까지 구간
# 구간 s l : s~l까지의 합
for i in range(m):
    # 변수 다중할당 : 구간 앞 구간 뒤 변수 처리 따로
    s_idx, l_idx = list(map(int, input().split(" ")))
    l_idx -=1
    s_idx -=1
    # 숫자 :  5 4 3 2 1
    # 누적합: [5,9,12,14,15]
    # 1~3까지의 구간: 0~2인덱스   12-15(0번째인덱스 앞 -1번째 안함) = 7
    # 2~5까지의 구간: 1~3인덱스   14-5 = 9
    # 2~2까지의 구간:
    if s_idx == 0:
        print(sum_lst[l_idx]-sum_lst[s_idx])
    else:
        print(sum_lst[l_idx]-sum_lst[s_idx-1])




# for i in range(m):
#     sum_idx = list(map(int, input().split(" ")))
    
#     j = sum_idx[0]
#     sum_lst= []
#     while j <= sum_idx[1]:
#         sum_lst.append(num_lst[j-1])
#     # TypeError: unsupported operand type(s) for -: 'str' and 'int'
#     # AttributeError: 'int' object has no attribute 'append'
#         j = j + 1
#     s_lst = sum(sum_lst)
#     print(s_lst)
