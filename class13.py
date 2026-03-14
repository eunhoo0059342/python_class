print("mission 1======")
account_details =[
    {'date':'0201','type':'withdraw','account':'211-854-6681','amount':132500,'memo':'-..'},
    {'date':'0205','type':'withdraw','account':'121-554-1820','amount':106000,'memo':'--'},
    {'date':'0205','type':'withdraw','account':'211-157-3580','amount':130000,'memo':'---'},
    {'date':'0207','type':'deposit','account':'202-3207-8819','amount':50000, 'memo':'Jovia'},
    {'date':'0201','type':'pay','account':'554-6280-7772','amount':100000,'memo':'Emily'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':123000,'memo':'-.'},
    {'date':'0201','type':'withdraw','account':'428-7190-5471','amount':167000,'memo':'.-'},
    {'date':'0204','type':'deposit','account':'260-415-2919','amount':16000,'memo':'John'},
    {'date':'0204','type':'withdraw','account':'211-854-6720','amount':180000,'memo':'..-.'},
    {'date':'0201','type':'withdraw','account':'115-854-1280','amount':230000,'memo':'..'},
    {'date':'0202','type':'withdraw','account':'131-555-6000','amount':251000,'memo':'-.'},
    {'date':'0203','type':'deposit','account':'243-31-5325','amount':15000,'memo':'Nugu'},
    {'date':'0204','type':'deposit','account':'463-433-0205','amount':7050,'memo':'Samuel'},
    {'date':'0201','type':'withdraw','account':'221-554-6880','amount':300000,'memo':'-..'},
    {'date':'0201','type':'withdraw','account':'428-7190-5471','amount':113700,'memo':'--'},
    {'date':'0204','type':'deposit','account':'206-415-2919','amount':16000,'memo':'Harry'},
    {'date':'0201','type':'withdraw','account':'628-7490-5471','amount':213700,'memo':'---'},
    {'date':'0201','type':'withdraw','account':'128-2196-5471','amount':113700,'memo':'-.'},
    {'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-'},
    {'date':'0204','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..-.'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..'},
    {'date':'0202','type':'withdraw','account':'131-554-6000','amount':221000,'memo':'-.'},
    {'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
    {'date':'0204','type':'deposit','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':300000,'memo':'-..'},
    {'date':'0201','type':'withdraw','account':'428-7190-5471','amount':313700,'memo':'--'},
    {'date':'0204','type':'deposit','account':'2060-415-2919','amount':16000,'memo':'Ann'},
    {'date':'0204','type':'withdraw','account':'111-554-6880','amount':320000,'memo':'---'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':24000,'memo':'Betty'},
    {'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Norman'},
    {'date':'0201','type':'withdraw','account':'428-7190-5471','amount':371200,'memo':'-.'},
    {'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-'},
    {'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Betty'},
    {'date':'0202','type':'withdraw','account':'131-554-6000','amount':1000,'memo':'DrFisher'},{'date':'0204','type':'withdraw','account':'2463-433-0205','amount':7050,'memo':'Samuel'},{'date':'0204','type':'withdraw','account':'111-554-6880','amount':530000,'memo':'..-.'},{'date':'0201','type':'withdraw','account':'111-554-6880','amount':130000,'memo':'..'},{'date':'0202','type':'withdraw','account':'131-554-6000','amount':109400,'memo':'-.'}]



# 알고리즘에 많이 쓰인다.
# "문자열".isalpha() : 문자열에 알파벳으로 구성되어 있는가 있으면 True 없으면 False
text = "abc12345"
print(text.isalpha())
# "문자열".isdigit() : 문자열에 숫자로만 구성되어 있는가? 
text = "a12345"
print(text.isdigit())

answer = []
for i in  range(len(account_details)):
    # print(account_details[i]["memo"])
    if account_details[i]["memo"].isalpha() == False:
        # print(account_details[i]["memo"])
        answer.append(account_details[i]["memo"])
print(answer)


print('mission 2 ============')
# 모스부호 사전(딕셔너리) 을 만들어라
# key
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
# value
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
morse_dic = {}
for i in range(len(morse_code)):
    morse_dic[morse_code[i]] = alphabet[i]
print(morse_dic)
    

# zip : 결합하다  => 합치면 튜플로 나온다.
# - 두개 갯수가 동일해야한다.
# zip(합칠데이터1, 합칠데이터2)
# print(list(zip(morse_code, alphabet)))

# 6. 튜플 Tuple ()
# - 리스트랑 동일한 성질: 순서, 인덱스 , 인덱싱
# - 변형이 불가능합니다. : 추가, 수정, 삭제 X append() X

# [('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'), ('.', 'E'), ('..-.', 'F'), ('--.', 'G'), ('....', 'H'), ('..', 'I'), ('.---', 'J'), ('-.-', 'K'), ('.', 'L'), ('--', 'M'), ('-.', 'N'), ('---', 'O'), ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'), ('...', 'S'), ('-', 'T'), ('..-', 'U'), ('...-', 'V'), ('.--', 'W')'-..-', 'X'), ('-.--', 'Y'), ('--..', 'Z')]


print("mission 3=========")
# answer와 morse_dic를 사용해서 해독하자.
# print(answer)
# print(morse_dic)


# {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', ': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
resert = ''
for i in range(len(answer)):
    # print(answer[i]) # mose_dic의 key로 활용하겠다.
    k = answer[i]
    # print(morse_dic[k])
    resert += morse_dic[k]
print(resert)

# DMONAFINDMONAFINDMONAFIN



# 과제 1)  메로나 : 1200, 탱그보이 : 1800, 빠삐코 : 800, 요맘때 1500 딕셔너리 로 만들어보자
icecream = {"메로나": 1200, "탱크보이": 1800, "빠삐코": 800, "요맘때": 1500}
# 1- 1. 메로나의 가격을 출력해라
print(icecream['메로나'])
# 1-2. 탱크보이와 요맘때 가격을 더해주세요.
print(icecream['탱크보이'] + icecream['요맘때'])
# 1-3 모든 가격의 합계를 구하시오 => 반복문 통해서 전체 접근하기
print(icecream['메로나'] + icecream['빠삐코'] + icecream['탱크보이'] + icecream['요맘때'])

a = 0
for k, v in icecream.items():
    # print(k, v)
    a += v
print(a)

    

    
print("==================================================================")

# 과제 2) 아이스크림 가격과 갯수가 같이 적혀 있는 딕셔너리가 있다.
icecream2 = {"미니 메로나":[1200,2],
             "탱크보이":[1800,3],
          "빠삐코": [800,12],
             "요맘때":[1500,10]}
# 2-1 미니누가바의 가격을 출력해라
print(icecream2['미니 메로나'][0])
# 2-2 탱크보이의 구매한 갯수를 출력해라
print(icecream2['탱크보이'][1])
# 2-3 빠비코의 총 구매 가격을 출력해라
print(icecream2['빠삐코'][0] * icecream2['빠삐코'][1])
# 2-4 모든 아이스크림의 총 구매 가격을 출력해라
print((icecream2['빠삐코'][0] * icecream2['빠삐코'][1]) + (icecream2['미니 메로나'][0] * icecream2['미니 메로나'][1]) + (icecream2["요맘때"][0] * icecream2['요맘때'][1]) + (icecream2['탱크보이'][0] * icecream2['탱크보이'][1]))
b = 0
for k, v in icecream2.items():
    # print(k, v)
    b += v[0] * v[1]
print(b)