'''
https://www.acmicpc.net/problem/1924

오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다.
참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
'''
import datetime

month, day = list(map(int, input().split(" ")))

time1 = datetime.datetime(2007, 1, 1)
time2 = datetime.datetime(2007, month, day)

days_lst = ['MON', 'TUE', 'WED', "THU", 'FRI', 'SAT', 'SUN']

if (time2 - time1).days > 0:
    # print((time2 - time1).days)
    time1_day = time1.day
    while time1_day > 6:
        time1_day -= 6
        # print(time1_day)
    print(days_lst[time1_day +1])
else:
    # print((time2 - time1).days)
    print(days_lst[(time2 - time1).days])