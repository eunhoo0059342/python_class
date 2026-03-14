import random   # 항상 제일 위에

# (과제) 로또를 뽑는 프로그램을 만들기 => lotto.py
# 함수로 만들기

# (1) 1~45번까지의 숫자중에서 랜덤하게 6개를 뽑습니다. ✅
# - 뽑았을때, 중복되면 안됩니다.        => 갯수 모자랄가능성이 보입니다. 수정
# - 뽑았을때, 숫자가 정렬되어있어야합니다. => 수정

# (2) 로또가 당첨번호랑 맞는지를 체크해서 결과를 출력하기 ✅
# - 3개맞으면 "4등"
# - 4개맞으면 "3등"
# - 5개맞으면 "2등"
# - 6개맞으면 "1등"

# (3) 터미널에서 키보드로 장수를 입력하면 자동으로 갯수만큼 여러장 로또뽑는기 ✅

# (4) 여러장 뽑은 로또번호의 당첨결과를 확인하기 - 로또는 즉석복권아닙니다.✅

# (5) 수동으로 로또번호 뽑기✅

# (6) 터미널에서 키보드로 장수를 입력하면 수동으로으로 갯수만큼 여러장 로또뽑는기 ✅ 

# (7) 반자동으로 로또번호 뽑기
# - 6개 번호를 뽑아야한다.
# - [수동의로 3개 : 1 2 3] [자동 3개 채우기]
# - [수동으로 1개][자동으로 5개 채우기]

# (8) 터미널에서 키보드로 장수를 입력하면 갯수만큼 여러장 로또뽑는기 
# - 다 입력하면 수동
# - 다 입력안하면 자동
# - 일부만 입력하면 반자동







# 로또번호 자동 생성 함수 --------------------------
# - 자동으로 6개의 번호를 뽑아주는 함수
# - 뽑았을때, 중복되면 안됩니다.
# - 뽑았을때, 숫자가 정렬되어있어야합니다.

# def lotto_num():
#     num_lst = []
#     # 6개가 될때까지 하는 것 => while 문
#     for i in range(10):
#         num_lst.append(random.randrange(1, 46))
#         set(num_lst)
#         if len(list(set(num_lst))) < 6:
#             num_lst.append(random.randrange(1, 46))
#         elif len(list(set(num_lst))) >=6:
#             break
#     # print(num_lst)
#     set_num_list = list(set(num_lst))
#     # print(sorted(set_num_list))
#     return set_num_list

 # tip) corret_count가 0-> 꽝 1->꽝 2-> 꽝, 3-> 4등,4->3등,5->2등,6->1등
    # => 조건 -> 값만 나오길 원할때  : 리스트, 딕셔너리 활용
    # result_list = ["꽝","꽝","꽝","4등","3등","2등","1등"]
    # return result_list[corret_count]


'''
lotto_num() 함수
- 기능 : 1부터 46번까지의 숫자중 6개를 랜덤으로 자동 뽑아서 로또리스트를 반환하는 함수
- 입력 : X
- 결과 : 로또 리스트

'''
def lotto_num():
    num_lst = []
    while len(num_lst) < 6:
        num_lst.append(random.randrange(1, 46))
        num_lst = list(set(num_lst))
    return sorted(num_lst)



'''
lotto_result 함수
- 기능 : 로또담첨번호와 구매한 *한장* 로또번호를 비교해서 당첨된 숫자 갯수만큼 결과를 반환하는 함수
- 입력 : 로또당첨번호(result,리스트) , 구매한로또번호(lotto,리스트)
- 결과 : 당첨결과(문자열)
'''
def lotto_result(result, lotto):
    corret_count = 0
    # 몇개 당첨되었는지 체크
    for i in range(6):
        if result[i] in lotto:
            corret_count += 1

    # 당첨 갯수에따른 당첨결과 반환
    if corret_count == 3:
        return "4등"
    elif corret_count == 4:
        return "3등"
    elif corret_count == 5:
        return "2등"
    elif corret_count == 6:
        return "1등"
    else:
        return "꽝"

   

'''
lotto_result_all() 함수
- 기능 : 로또담첨번호와 구매한 *여러장의* 로또번호를 비교해서 당첨된 숫자 갯수만큼 결과 리스트로 반환하는 함수
- 입력 : 당첨번호(result,리스트), 여러장의 로또번호(이차원리스트)
- 결과 : 각 장수별 당첨결과(리스트)
'''
def lotto_result_all(result, lottos_lst):
    result_lst = []
    for i in range(len(lottos_lst)): 
        # 한장의 로또번호를 몇개 맞앗는지 카운트 세기 => lotto_result()
        result_lst.append(lotto_result(result, lotto_result[i]))
    


'''
auto_lotto() 함수
기능 : 장수를 입력받아서 *여러장의* 자동으로 로또를 뽑기 함수
입력 : 뽑을 횟수(숫자)
결과 : 여러장의 자동 로또 리스트(이차원리스트)
'''
def auto_lotto(count_num):
    auto_lotto_lst = [] # 로또번호 이차원리스트
    for i in range(count_num):
        auto_lotto_lst.append(lotto_num())
    return auto_lotto_lst


'''
passivity_lotto() 함수
기능 : *여러장의* 수동으로 찍은 로또를 정렬해주는 뽑아주는 함수
입력 : 입력하는 장의 개수
결과 : 여러장의 수동 로또 리스트

'''
# <발생한 문제사항>
    # - 45이상을 입력 받을 수 있네요. => 입력조건 다시 체크하기
    # - 장수랑 상관없이 1개만 입력받을 수 있다. => 장수 추가하기

def passivity_lotto(count_num):
    passivity_result_lst = []   # 각 장수별 로또 => 이차원리스트
    for i in range(count_num):
        print((i+1),"번째 장-------")
        ###### 수동 한장 뽑기
        passivity_lotto_lst = []    # 개별로또 번호 리스트
        while len(passivity_lotto_lst) < 6:
            lotto_num = int(input("1~45의 숫자 중에서 6개를 중복 없이 입력을 하나씩 입력을 해주세요(중복일 경우 다시 선택을 할 수 있습니다): "))
            if lotto_num <= 45 and lotto_num > 0:
                passivity_lotto_lst.append(lotto_num)
                passivity_lotto_lst = sorted(list(set(passivity_lotto_lst)))

        print((i+1),"번째 로또 => ", passivity_lotto_lst)
        ##### 
    return passivity_result_lst

# 메인 실행 -선택----------------------------------------------------------------------------------------------
def main1():
    result=[2,13,15,16,33,43]
    passivity_word=["수동","tnehd","ㅅㄷ"]
    auto_word = ["자동", "wkehd", "ㅈㄷ"]

    count_num = int(input("로또를 뽑을 장수를 적어주세요 => "))
    passivity_or_auto = input("수동 혹은 자동을 적어주세요: ")
    lottos = []
    if passivity_or_auto in auto_word:
        lottos += auto_lotto(count_num)
        # 결과 여러장 lotto_result_all() 사용하기

    elif passivity_or_auto in passivity_word:
        lottos += passivity_lotto(count_num)


    # 결과 확인
    print(lotto_result_all(result, lottos))



    # <로또 추출기 시나리오>
    # (1) 로또를 구매할지 ,당첨을 확인할지 물어보기
    # (1-1) 로또구매를 선택하면 로또 구매할 장수 입력하기
    # (1-2) 로또번호를 6개 입력해주세요.
    # (1-3) 이때, 안적고 넘어가면 => 자동으로 6개 로또 뽑기
    # (1-4)      6개 다 적으면 => 수동으로 6개 로또 뽑기
    # (1-5)      6개 미만으로 적으면 => 적은 갯수는 수동으로 모자란 갯수는 자동으로 채우기
    # (2) 당첨을 확인하기
    # (2-1) 구매한 로또가 있으면 당첨결과 출력
    # (2-2)          없으면 출력 할게 없음.



def lotto_check(check_num):
    result=[2,13,15,16,33,43]

    print(lotto_result(result, check_num))



def main2():
    lotto_lst = []
    count_num = int(input("로또를 뽑을 장수를 적어주세요 => "))
    for i in range(count_num):
        print((i+1),"번째 장-------")
        passivity_lotto_num = input("구매하실 로또의 번호 6개를 적어주세요(구분은 띄어쓰기/ 적지않은 번호는 자동으로 선정됩니다.): ").split(" ")
        lotto_num_lst = []
        
        # 입력값(passivity_lotto_num) 검증하기
        # 입력값이 항상 숫자인지도 체크필요.
        # - 빈문자열 : 자동
        # - 입력을 받으면 -> 일부만 입력했다 반자동
            #    -> 모두 입력했다 수동
        # 6개보다 많이 넣으면 다 들어간다.=> 다시 입력하도록 하세요.
        # 1~45까지의 숫자말고 다른 값이 들어가면 => 다시 입력하도록 하기

        for j in range(len(passivity_lotto_num)):
            try:
                if int(passivity_lotto_num[j]) < 46:
                    lotto_num_lst.append(int(passivity_lotto_num[j]))
                elif len(passivity_lotto_num) > 6:
                    raise Exception("LenError")
                else:
                    raise Exception("StrError")
            except 'StrError':
                passivity_lotto_num = input("번호를 제외한 다른 문자가 발견됐습니다. 다시 '번호' 6개를 적어주세요: ").split(" ")
            except 'LenError':
                passivity_lotto_num = input("선택하신 번호가 6개를 초과하였습니다. 다시 번호 '6개'를 적어주세요: ").split(" ")
                
        if len(lotto_num_lst) != 6:
            while len(lotto_num_lst) < 6:
                lotto_num_lst.append(random.randrange(1, 46))
                lotto_num_lst = list(set(lotto_num_lst))
        lotto_lst.append(lotto_num_lst)
        
    return sorted(lotto_lst)


# 반자동 로또 한개 뽑기 함수 만들기
def lotto_picker():
    while True:
        # 최종 6개 번호 : user_input 검증된것만 집어넣기
        passivity_lotto_num = []
        # input => 에러가 발생하는 상황 

        try: # 문자열.strip(): 아무것도 없으면 띄어쓰기. 맨앞과 맨뒤는 띄어쓰기를 허용 안하기
            user_input = input("구매하실 로또의 번호 6개를 적어주세요(구분은 띄어쓰기/ 적지않은 번호는 자동으로 선정됩니다.): ").strip()
            
            
            # 입력값이 비어있다면(len<=0) 자동뽑기함수(lotto_num)를 실행하기
            if len(user_input)<=0:
                passivity_lotto_num = lotto_num()
            else:# 수동, 반자동
                user_lotto_num = list(set(map(int, user_input.split(" "))))
                for i in range(len(user_lotto_num)):
                    if user_lotto_num[i] >= 1 and user_lotto_num[i] < 46:
                        passivity_lotto_num.append(user_lotto_num[i])
                
                # 만약에 갯수 6개보다 작으면가 맞지 않으면 자동뽑기함수lotto_num() 추가로 뒤에다가 붙이기
                if len(passivity_lotto_num) < 6:
                    passivity_lotto_num += lotto_num()


                # 자동으로 남은 로또번호를 뽑아주면 좋겠는데 어떻게 하면 좋을까?
                # 최대 5개부터 ~ 최소 1개 => 중복 안됨, 원래 뽑은 숫자랑도 중복은 되면 안됨
                # [2,3,4,5,6] + 3개 (자동뽑기함수lotto_num() 6개 [2,3,4,5,6,7])

                # # 자르기 0~6까지 자르기

            # 모든 번호가 다 잘 뽑힐경우, 함수 탈출하기 - break, return
            result = sorted(list(set(passivity_lotto_num))[:6])
            return result
        except :
            print("Error닷")
            
        # 정렬 맨마지막에
        





# print(lotto_picker())

def main():
    buy_or_check = input("로또 구매를 원하시면 구매, 로또 당첨 확인을 원하시면 확인이라 써주세요: ")
    buy_word = ["구매","rnao", "ㄱㅁ", "buy"]
    check_word = ["확인", "ㅎㅇ", "ghkrdls", "check"]

    if buy_or_check in buy_word:
        # 장수 추가하기!
        count_num = int(input("구매하실 장수를 입력해주세요."))
        result_lst = []
        
        for i in range(count_num):
            result_lst.append(lotto_picker())
        return result_lst
    elif buy_or_check in check_word:
        return lotto_check()

print(main())









