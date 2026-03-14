'''
https://www.acmicpc.net/problem/10867

N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.

첫째 줄에 수의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
'''


repetitions_num = int(input())

answer = ''

sorted_num_list = sorted((list(set(input().split(" ")))))   
# print(sorted_num_list)
for i in range(len(sorted_num_list)):
    # print(sorted_num_list[i])
    answer += sorted_num_list[i] + " "


# 1. 붙은 맨 뒤 띄어쓰기를 제거 하기
# => 문자열 메서드 .strip("찾는문자") : 양끝의 문자여을 제거할때 사용하기 =

# 2. 처음부터 뒤에 띄어쓰기 안붙이기
# => 리스트 추가한다음 => 문자여롤 합치기(사이사이 공백이 들어가게 처리가능^^)

print(answer.strip(" "))


