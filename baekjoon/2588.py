# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# 예제 입력:472
#          385
a = []
b = []
num = input()
num2 = input()
for i in range(len(num)):
    b.append(num2)
a.append(num)
f = int("".join(a))
g = int("".join(b[0]))
c = g // 100
d = (g - c * 100) // 10
e = g % 10
print(f * e)
print(f * d)
print(f * c)
print(f * (c * 100 + d * 10 + e))

