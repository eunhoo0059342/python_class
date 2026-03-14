# 수들의 합2 https://www.acmicpc.net/problem/2003

'''

문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

# 입력예제
4 2      
1 1 1 1  

# n=4(입력받을 숫자갯수) m="찾고자하는 합"
# 경우의 수로 조합해서 m이 되도록하는 경우가 몇갠가? 
'''



from tkinter import S


n, m = list(map(int, input().split(" ")))
num_lst = list(map(int, input().split(" ")))


'''
<쉬운방법>
시간제한갖지말고 일단 예상결과가 나오도록 풀어봐
여튼 굉장히 노가다 => 5랑 같은것을 찾아야한다. 

<고민을하는 방법 - 투포인트>
포인트 : C언어 데이터를 위치(메모리주소)를 가리키는 포인트
=> '위치'를 다루는 변수
start =0
end = 0

10 5
1 2 3 4 2 5 3 1 1 2  
=> 연속된합으로 구해야한다.
=> 특정 값을 찾을때가지 start와 end 위치를 변경해주기
=> start ~ end까지 수열의 합의 범위
1            (num)1<5(m) => 큰수가 필요 (end =>오른쪽)
1 2          3<5
1 2 3        6>5 => 숫자가 큰데? 작은숫자를 버려보기 (start=> 오른쪽)
  2 3        5=5 => 갯수up => 큰수가 필요
  2 3        9>5
    3 4      7>5
      4      4<5
      4 2    6>5 
'''



s_idx = 0    # 시작인덱스
l_idx = 0    # 끝인덱스
num = 0      # 수열의 합
count = 0

while l_idx < n:
    print(num, "  / 시작",s_idx,"끝",l_idx, '카운트', count)
    if num == m:
        count += 1
        l_idx += 1
    elif num > m:
        num -= num_lst[s_idx]
        s_idx += 1
    elif num < m:
        l_idx += 1
        num += num_lst[l_idx]
            

print(count)



# 과제)
# 부분합 https://www.acmicpc.net/problem/1806
# 용액 https://www.acmicpc.net/problem/2467


















