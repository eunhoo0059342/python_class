'''
https://www.acmicpc.net/problem/9012

괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
'''

# 스택: LIFO(last in first out)
# - 
class Stack:
    def __init__(self):
        self.lst = []
    
    def push(self, push_data):
        self.lst.append(push_data)
    
    def pop(self):
        if self.isempty() == True:
            return None
        else:
            return self.lst.pop()
    def isempty(self):
        if self.size() == 0:
           return True
        else:
           return False
    
    def size(self):
        return len(self.lst)

t = input()

for i in range(int(t)):
    # 괄호문제
    # - 괄호를 스택에 저장해서 관리할것
    input_data = input()
    stack = Stack()
    result = ""
    for j in range(len(input_data)):       
        # ( : 열린괄호
        # ) : 닫힌괄호 
        # (1) 열린괄호는 스택에 넣어준다.
        # (2) 닫힌괄호는 맨위값(top)이 "("이면 빼준다.
        #     맨위값(top)이 "("아니면 "NO"(괄호가 실패해서 스톱)
        if input_data[j] == "(":
            stack.push(input_data[j])
        elif input_data[j] == ")":
            # 비어있지 않다 => '열린괄호'가 있다
            if stack.isempty()==False:
                stack.pop() 
            else:
                result= "NO"
                break
    # 스택이 비어있으면 Yes 비어있지 않으면 => No 
    if result!="NO" and stack.isempty() == True:
        print("YES")
    else:
        print("NO")



# https://www.acmicpc.net/problem/4949




################################
#     vps_num = 0
    # input_data = input()
#     for j in range(len(input_data)):
#         if input_data[j] == "(":
#             vps_num += 1
#         elif input_data[j] == ")":
#             vps_num -= 1
#         else:
#             print("NO")
#             break

#     if vps_num == 0:
#         print("YES")
#     else:
#         print("NO")

