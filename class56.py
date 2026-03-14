
'''
정렬알고리즘
(1)선택정렬 함수 (selectionSort)
- 입력 : 리스트
- 결과 : 정렬된 리스트
- 기능 : 앞에서부터 자리수를 결정할건데 -> 뒤쪽의 최소값과 비교해서 교체
'''
def seletctionSort(num):
    for i in range(len(num_list)):
        # 4자리 0이 들어가고, 1자리에는 4가 들어가야한다! 
        # => 인덱스 값을 찾아햡니다. 
        # => 최솟값알고리즘을 사용해서 인덱스 번호를 찾기
        # (1) 최솟값인덱스 변수를 만든다. 
        min_num = i
        # (2) 내 뒤쪽값으로 최솟값 찾기 
        #     - 모든 리스트를 비교해서 임시최소값보다 작으면 교체 크면 pass 한바퀴 다 돌면 최소값이 나옵니다.
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[min_num]:
                min_num = j
        # print(min_num, num_list[min_num])
        # 교체 i <-> min_num번째값의 교체하기
        tmp = num_list[i]
        num_list[i] = num_list[min_num]
        num_list[min_num] = tmp
    # 교체된 결과를 반환하고 싶으니깐. return
    return num_list


num_list = [4,5,1,3,2]
print(num_list)
print(seletctionSort(num_list))


# 교체알고리즘
a=10
b=5
tmp = a
a=b
b=tmp
print(a,b)




#data
'''
샘플 객체(Object)
* 객체 : 데이터 여러개 + 기능(메서드 여러개를 동시에 가질수있는 데이터의 구조

- 데이터 : name : 혈액주인
         collection_time : 체혈시간
         inspection_time : 검사시간 


# 체혈한 시간대로 정렬은 되어있다.  


'''
class sample:
    # 생성자: 
    def __init__(self, name, collection_time, inspection_time):
        self.name = name
        self.collection_time = collection_time
        self.inspection_time = inspection_time
    # __str__(): 객체 문자열처럼 보이게 하기 => 출력할때 내용이 보여요
    #  return 문자열 => 결과값이 <main object> 대신 출력할 값
    def __str__(self):
        # 객체의 이름/ 체혈시간 / 검사 시간 을 반환 f"문자열 {변수}"
        return f"{self.collection_time}, {self.inspection_time}, {self.name}"
 
import random
from tkinter import N
random.seed(66)
 
namelist = ['John.W','Judith.G','Brett.N.O','Tracy.H.N','Michael.B','Melissa.R','Andrea.F','Thomas.W.J','Veronica.C','Blake.W','Darren.V','Scott.C','Bill.R.C','Jeffrey.S','Dwayne.C','Bruce.F','Sara.P','Stromy.U.J','Lala.P.V','Maddox.B']
collection_time = [205503180530, 205503180613, 205503180733, 205503180814, 205503180945, 205503181242, 205503181256, 205503181581, 205503181600, 205503181621, 205503181641, 205503181747, 205503181728, 205503181729, 205503181823, 205503181902, 205503191125, 205503191325, 205503191400, 205503191505]
inspection_time = [205503200901, 205503201014, 205503200312, 205503200611, 205503200212, 205503200632, 205503200239, 205503200017, 205503200420, 205503200311, 205503200538, 205503200018, 205503200603, 205503200131, 205503200021, 205503200135, 205503200011,205503200511,205503200411,205503200451] 
random.shuffle(inspection_time)

tosort = []
for i in range(len(namelist)):
    tosort.append(sample(namelist[i], collection_time[i],inspection_time[i]))



# 1. tosort 데이터를 각각 출력해보기
# 이미 체혈시간대로 정렬은 완료
# => 우리가 해야할내용 TODO: 객체의 검사시간으로 객체 선택정렬하기
# for i in range(len(tosort)):
#     print(tosort[i])




# 객체를 선택정렬하는 함수
# 입력 - 객체 리스트 
# 기능 - 객체의 검사시간속성으로 선택정렬을 하기
# 결과 - 정렬된 리스트

# 교체할 객체 : tosort[i]
# [i ~ 끝까지] 중에서 객체의 검사시간(inspection_time)중 교체할 최소값이 있느 위치(인덱스)을 찾자.
# 12번 선택정렬하는 과정 -> 13번째 혈액샘플이 누구건지 알고싶어요.


def c_sort(tosort):
    n = 0
    for i in range(len(tosort)):
        min_num = i
        # print(tosort[i])
        for j in range(i, len(tosort)):
            if tosort[j].inspection_time < tosort[min_num].inspection_time:
                min_num = j
        # 다중 할당 활용 교체
        # a, b = b, a
        tosort[i], tosort[min_num] = tosort[min_num], tosort[i]
        n += 1
        if n == 12:
            return tosort        
       

    return tosort

# 사람기준 13번째 -> 12번째 객체의 이름(name)을 을 출력해라. 
a = c_sort(tosort)
print(a[12].name)
# for i in range(len(a)):
#     print(a[i])