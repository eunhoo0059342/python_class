
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
        # (2) 내 뒤쪽값으로 최솟값 찾기 
        #     - 모든 리스트를 비교해서 임시최소값보다 작으면 교체 크면 pass 한바퀴 다 돌면 최소값이 나옵니다.
        min_num = i
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



'''
버블정렬 BubbleSort()
- 입력 : 리스트
- 출력 : 정렬된 리스트
- 기능 : 앞뒤값을 비교해서 큰애가 뒤로 먼저 정해지는 형태의 정렬
'''
print("02) 버블정렬 ==========================")
def BubbleSort(num_list):
    # (2) 반복 
    for j in range(len(num_list)-1):
        # 맨 뒤값을 고정으로 갖는 방법
        # 이미 결정된 번호는 더이상 체크 안해도 된다.
        for i in range(len(num_list)-j-1):
            # print(num_list[i], num_list[i+1])
            # (1)앞의 값이 크면 교체
            if num_list[i] > num_list[i+1]:
                tmp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = tmp    
            # print(num_list)
        # print("--")
    return num_list





num_list = [4,5,1,3,2]
print(num_list)
sorted_num = BubbleSort(num_list)
print(sorted_num)


'''
삽입정렬 InsertionSort()
- 입력 : 리스트
- 출력 : 정렬된 리스트
- 기능 : 정렬한 숫자를 따로 저장해서 삽입할 위치를 찾는게 목표
        기준보다 큰 숫자는 뒤로 당겨져서 정리가된다.

4 1 3 5 2
  ------- 삽입할데이터 1 / 1번째
4 4 3 5 2
1 4 3 5 2  

'''
# (1) 삽입할 데이터를 뽑아서 출력을 해보자.
# - 삽입할 데이터, 인덱스번호를 따로 변수에 저장
def InsertionSort(num_list):
    print(num_list)
    resorted_lst = []
    for i in range(1, len(num_list)):
        print(num_list[i])
        value = num_list[i]
        index = i  # <-앞데이터랑 비교를 할것이다. 
        #(3) index가 0보다 크면 앞데이터랑 비교 (index=0이면 앞의 값이 존재하지 않는다.)
        # - 만약에 앞에값(i-1번째)이 현재value값보다 크면 // 뒤에 값을 밀리기
        # - 인덱스를 한칸 앞으로 이동해주기
        while index > 0:
            # 탈출조건
            if num_list[index-1] <= value:
                break
            # print("뒤로미루기")
            # (4) index-1번째 요소값를 한칸 뒤로 미루기 ( 앞의 값을 현재위치(index)에 수정하기 )
            num_list[index] = num_list[index - 1]
            index -= 1
            # print(num_list)
        
        # 조정한 index위치에다가 삽입할 데이터(value)를 저장해주기
        num_list[index] = value
        # print(num_list,"조정끝")
        # print("---")



num_list=[4,1,3,5,2]
print(InsertionSort(num_list))



####################################





