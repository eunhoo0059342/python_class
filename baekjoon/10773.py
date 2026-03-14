'''
제로 https://www.acmicpc.net/problem/10773

문제
나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며,
정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.(추가하기)
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
'''
class Stack:
    def __init__(self):
        self.lst = []
    
    def push(self, push_data):
        self.lst.append(push_data)
    
    def pop(self):
        # 리스트삭제 : 리스트변수.pop(인덱스) => 인덱스번호를 안적으면 맨 뒤에서 삭제
        # pop으로 뽑은 값을 결과값으롭 반환해준다.
        # isempty메서드를 사용해서 비어있는지 체크하고 비어있으면, None을 반환하기, 안비어있으면 뽑은 값
        if self.isempty() == True:
            return None
        else:
            return self.lst.pop()
            

    def isempty(self):
        # 비어있는지 체크하는 메서드(isempty)
        # - 비어있으면 True, 아니면 False값을 반환하기
        if self.size() == 0:
           return True
        else:
           return False
    
    def size(self):
        return len(self.lst)

k = input()
stack = Stack()
for i in range(int(k)):
    input_data = int(input())
    if input_data != 0:
        stack.push(input_data)
    else:
        stack.pop()    

print(sum(stack.lst))



# 괄호 https://www.acmicpc.net/problem/9012
