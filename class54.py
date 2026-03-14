'''
정렬 알고리즘

<리스트 정렬>
리스트.sort(옵션) : 원본이 바꾸는 기능 대신, 결과값은 없어요.
sorted(리스트,옵션): 결과값으로 정렬된 리스트가 나오는것
- 기본 정렬 : 오름차순
- 내림차순 정렬 : 내림차순 reverse=True 옵션
- 정렬기준바꾸기 : key= 함수이름
          
'''
num_list = [3,5,1,7,13,4]

print("전",num_list)
sor_num_lst = sorted(num_list)
print("후", sor_num_lst)

print("전",num_list)
num_list.sort(reverse=True)
print("후",num_list)

# 문자열은 사전순서대로 정렬
# - 맨앞글자 먼저 비교 정렬 -> 두번째 글자 ...
num_list = ['31','255','7','1','13','1234']
print(sorted(num_list))
# 글자길이 순서대로 정렬하고싶은데...
# key=함수이름만 옵션
print(sorted(num_list, key=len))
print()

# 다중데이터 정렬
# 0번째 열부터 정렬
# 정렬 기준 변경 : 나이순서대로 정렬하고 같은 나이일경우에는 이름순서대로 정렬
# => key : 내만든 함수도 적용이 가능하다.
student = [('짱구',5),('유리',7),('맹구',5),('훈이',5),('짱아',1),('철수',15),('철수',9)]

def swich(data):
    # data = ('짱구',5)
    return (data[1],data[0])

print(swich(('짱구',5)))

print(sorted(student, key=swich))
# 한줄함수 lambda 매개변수(x): return작성할 코드 
print(sorted(student, key=lambda x: (x[1], x[0])))




