#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#반복문인데 끝날 때마다 개수 +1과 print("\n")을 한다 
line = input()
answer = []
for i in range(int(line)):
    answer.append("*")    
    print(''.join(answer))


