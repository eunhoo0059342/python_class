'''
https://www.acmicpc.net/problem/2884
45분 일찍 알람 설정하기
'''

'''
시간에 대한 특징을 정확하게 이해할 것
=> 한글로 어느정도 정리가 필요하다.
=> 수학

'''




t = input().split(" ")
time = {"시": int(t[0]), "분": int(t[1])}
answer = ''
# print(time)

time['분'] -= 45

# 9시 45분 => 9시 0분
if time["분"] >= 60:
    time["시"] += 1
    time["분"] -= 60
    answer += str(time)
    if time["시"] < 0:
        time['시'] += 24
    print(time["시"], time["분"])
# 0분보다 작으면, -1분부터~ 시를 빼고, 분을 60추가
elif time["분"] < 0:
    time["시"] -= 1
    time["분"] += 60
    answer += str(time)
    if time["시"] < 0:
        time['시'] += 24
    print(time["시"], time["분"])
else:
    answer += str(time)
    if time["시"] < 0:
        time['시'] += 24
    print(time["시"], time["분"])