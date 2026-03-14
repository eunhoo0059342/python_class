'''
 https://www.acmicpc.net/problem/2577

세 개의 자연수 A, B, C가 주어질 때 A * B * C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 A * B * C = 150 * 266 * 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
'''

def num(a, b, c):
    num1 = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    # num1 = [0]*10
    d = str(a * b * c)
    e = []
    for i in range(len(d)):
        e.append(d[i])
        # print(d)
        # print(int(d[i]))
        num1[d[i]] += 1
    num2 = list(num1.values())
    #print(num1)
    #print(num2)

    return num2
    # return : 결과반환 / 함수를 종료
    

answer = num(int(input()), int(input()), int(input()))
# print(answer)
for i in range(len(answer)):
    print(answer[i])