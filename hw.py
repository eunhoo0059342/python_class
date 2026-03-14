# =============================================
# Calculator 클래스 설계
# ---------------------------------------------
# ✅ 클래스 이름: Calculator
#
# ✅ 속성 (Attributes):
# - value: 현재 계산된 값 (처음값은 0)
#
# ✅ 메서드 (Methods):
# - add(x): 현재 값에 x를 더함
# - subtract(x): 현재 값에서 x를 뺌
# - multiply(x): 현재 값에 x를 곱함
# - divide(x): 현재 값을 x로 나눔 (0으로 나누기 예외 처리)
# - clear(): 현재 값을 0으로 초기화
# - get_result(): 현재 값을 반환
#
# ✅ 예외 처리:
# - divide(x): x가 0일 경우 "0으로 나눌 없습니다." 메세지 띄우기(ZeroDivisionError 예외 처리) 



class Calculate:
    def __init__(self):
        self.value = 0
    
    def add(self, x):
        self.value = self.value + x

    def subtract(self, x):
        self.value = self.value - x

    def multiply(self, x):
        self.value = self.value * x

    def divide(self, x):
        self.value = self.value / x
    
    def clear(self):
        self.value = 0

    def get_result(self):
        return self.value

# (1) 인스턴스 객체 생성하기
# (2) 인스턴스 속성 출력하기
# - 확인가능 , class밖에서 직접적으로 수정하시면 안된다.
# - 속성 값을 변경할려면 메서드를 만들어서 변경해줘야합니다.
# (3) num인스턴스에 3을 더해주세요. => 더하기 기능(메서드)
# (4) num인스턴스에 5을 곱해주세요. => 곱하기 기능(메서드)
# (5) num인스턴스의 결과를 출력해보자. => 결과 가져오기 기능(메서드)
# (6) num인스턴스 기존값을 다 지워주세요.
num = Calculate()
# x = int(input())
num.add(3)      #>>>> 결과: 3
num.multiply(5) #>>>> 결과: 15
print(num.get_result())
num.clear()
print(num.get_result())
