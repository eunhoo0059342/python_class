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





