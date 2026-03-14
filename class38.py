'''
자료구조 (data structure) 8구조
1. 리스트
리스트=[1,2,3,4]

2. 스택(Stack)   => LIFO(Last in First out)
|     |         => 리스트로 구현
|     |         => 넣는 기능(push 메서드)
|     |         => 빼는기능(pop 메서드)
|     |         => 사이즈체크하는 메서드 (size)
|  B  |         => 비어있는지 체크하는 메서드(isempty)
|__A _|         => 제일 위값을 top / 제일 아래값을 bottom

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

        

stack1 = Stack()
print(stack1.lst)
# A를 추가하기(push)
stack1.push('A')
stack1.push('B')
stack1.push('C')
print(stack1.lst)
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1.lst[-1])
print(stack1.pop())


# 쌓이는 데이터들에 대한 관리를 할때 사용하기
# - 웹브라우저 : 뒤로가기버튼
# - ctrl+z  
# - 괄호 검사 
