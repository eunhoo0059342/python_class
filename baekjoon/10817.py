'''
https://www.acmicpc.net/problem/10817

세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
'''
'''
input_data = input().split(" ")
print(input_data)
sorted_input_data = sorted(input_data)
print(sorted_input_data[i])
'''

input_data = input().split(" ")
#input_data = [int(input_data[0]),int(input_data[1]),int(input_data[2])]

input_data = list(map(int,input_data))
input_data.sort()
print(input_data[1])


# 알고리즘 map() 적극적으로 활용해보세요.
# -> 숫자가 한줄에 여러개 나올때!
### 리스트안 요소에 int()함수를 모두 적용하고 싶어요.
# => map(함수이름,리스트) : 리스트 모든 요소에 함수를 적용해서 나오기
# => map(은 기본적으로 내용이 안보임 => list() 함수를 사용하면 보인다.


number = ['1','2','3','4','5']
# new_num = []
# for i in range(len(number)):
#     new_num.append(int(number[i]))
# print(new_num)

# <map object at 0x000001D76D729DB0>
print(list(map(int,number)))
