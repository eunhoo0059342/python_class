'''
객체 Object : 속성(변수,데이터) + 메서드(함수,기능,코드 묶음)
- Class : 객체 틀, 설계
- 인스턴스 : 실체 나온 값, 실체를 갖고 있는 객체 




로또 객체 (1장)
- 데이터(속성) :
    - 로또 번호 6자리를 넣는 데이터 => 리스트
    - 당첨여부 : None
- 행동(메서드=함수) :
    - 로또 자동으로 뽑기 메서드
    - 결과가 주어졌을때 당첨확인하기
'''
import random


class Lotto():
    # 생성자(_init__메서드) : 첫생성할때, 
    def __init__(self):
        self.lotto_num = []
        self.lotto_rslt = None
        self.lotto_n()
        

    def lotto_n(self):
        # 자동뽑기를 계산하고 내 속성을 변경하고 싶다.
        # 1) 내 속성에 대해서 다 계산할것
        # 2) 변수로 계산하고 속성에 반영하기
        num_lst = []
        while len(num_lst) < 6:
            num_lst.append(random.randrange(1, 46))
        self.lotto_num = sorted(num_lst)
        # return

    # 매개변수 : 외부에 있는 값을 가져올때, 내부의 속성르 사용하고 싶은면 self에 들어가 있다.
    def lotto_result(self, result, bonus):
        # 1등) 6개 다 맞기
        # 2등) 5개 + 보너스번호 맞기
        # 3등 5개
        # 4등 4개
        # 5등 3개

        # 결과 : result
        # 내로또번호 : self.lotto_num
        corret_count = 0
        bonus_count = 0
        # 몇개 당첨되었는지 체크
        for i in range(6):
            if result[i] in self.lotto_num:
                corret_count += 1
        if bonus in self.lotto_num:
            bonus_count += 1

        # 당첨 갯수에따른 당첨결과 반환
        if corret_count == 3:
            self.lotto_rslt = "5등"
            
        elif corret_count == 4:
            self.lotto_rslt = "4등"
            
        elif corret_count == 5 and bonus_count == 1:
            self.lotto_rslt = "2등"    
            
        elif corret_count == 5:
            self.lotto_rslt = "3등"
            
        elif corret_count == 6:
            self.lotto_rslt = "1등"
            
        else:
            self.lotto_rslt = "꽝"
        return self.lotto_rslt
    



# # 인스턴스 생성하기
# a = Lotto()

# print(a.lotto_num)
# print(a.lotto_rslt)
# a.lotto_result(result, reulst_bonus)
# print(a.lotto_num)
# print(a.lotto_rslt)



## 1170회 당첨결과의 형태는 변경해도 됩니다.
result = [3,13,28,34,38,42]
reulst_bonus = 25

# 로또를 1장 뽑아보기 - 생성할때, 바로 뽑기
# 로또를 5장 뽑아주세요. => 리스트

lotto_list=[]
input_num = int(input())

for i in range(input_num):
    lotto = Lotto()
    lotto_list.append(lotto)
# lotto1 = Lotto()
# print(lotto1.lotto_num)
# lotto2 = Lotto()
# print(lotto2.lotto_num)
# lotto3 = Lotto()
# print(lotto3.lotto_num)
# lotto4 = Lotto()
# print(lotto4.lotto_num)
# lotto5 = Lotto()
# print(lotto5.lotto_num)

# # 리스트에 객체 추가하기
# lotto_list.append(lotto1)
# lotto_list.append(lotto2)
# lotto_list.append(lotto3)
# lotto_list.append(lotto4)
# lotto_list.append(lotto5)
print(lotto_list)


for i in range(len(lotto_list)):
    l = lotto_list[i] #== 인스턴스 # <__main__.Lotto object at 0x0000021DA8A50AD0>
    # 인스턴스명.메서드이름()
    print(l.lotto_result(result, reulst_bonus))
    

# print(type("hello"))
# a= "hello"
# print(a.split("l","i"))


