# https://www.acmicpc.net/problem/5532
'''
상근이는 초등학교에 다닐 때, 방학 숙제를 남들보다 먼저 미리 하고 남은 기간을 놀았다. 방학 숙제는 수학과 국어 문제 풀기이다.

방학은 총 L일이다. 수학은 총 B페이지, 국어는 총 A페이지를 풀어야 한다. 상근이는 하루에 국어를 최대 C페이지, 수학을 최대 D페이지 풀 수 있다.

상근이가 겨울 방학동안 숙제를 하지 않고 놀 수 있는 최대 날의 수를 구하는 프로그램을 작성하시오.
'''
l = input()
a = input()
b = input()
c = input()
d = input()
e = []

vacation = {'방학': l, '수학':b, '국어': a, '국어최대': c, '수학최대': d}
if int(vacation['국어']) / int(vacation['국어최대']) == int(vacation['국어']) // int(vacation['국어최대']):
    e.append(int(vacation['국어']) / int(vacation['국어최대']))
elif int(vacation['국어']) / int(vacation['국어최대']) != int(vacation['국어']) // int(vacation['국어최대']):
    e.append(int(vacation['국어']) // int(vacation['국어최대']) + 1)
    print(int(vacation['국어']) // int(vacation['국어최대']) + 1)
if int(vacation['수학']) / int(vacation['수학최대']) == int(vacation['수학']) // int(vacation['수학최대']):
    e.append(int(vacation['수학']) / int(vacation['수학최대']))
    print(int(vacation['수학']) / int(vacation['수학최대']))
elif int(vacation['수학']) / int(vacation['수학최대']) != int(vacation['수학']) // int(vacation['수학최대']):
    e.append(int(vacation['수학']) // int(vacation['수학최대']) + 1)
    print(int(vacation['수학']) // int(vacation['수학최대']) + 1)
print(int(vacation['방학']) - max(e))