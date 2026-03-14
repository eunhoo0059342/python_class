'''
    2
    ↓(입력=매개변수,인수)
 _\   /______함수___
|                  |
|  ㅁ + 2 =         |
|___________    ___ 
           /    \
              ↓(결과)
              4

함수 : 코드 묶어 이름을 붙입니다. => 기능

(1) 함수의 정의
- 매개변수 : 인수의 데이터를 저장하는 변수
- 매개변수의 갯수와 인수의 갯수는 항상 같게 해줘야한다.
- return문 : 1. 결과값 반환 2. 함수가 종료

def 함수이름(매개변수):
  작성할 코드
  return 결과값 

(2) 함수 호출
# 인수: 함수를 호출할때 입력을 넣어줄수 있습니다.

함수이름(인수)

'''


# 안녕하세요라고 출력하는 hello함수를 만들어보자.
def hello():
    print("안녕하세요")


# 업그레이드) "환영합니다 OOO님" welcome함수로 만들어보기
# - 입력이 필요한가? Y 
# - 어떤 입력값이 들어나요? 이름 1개(문자열 타입)
def welcome(name):
    # name="강은후"
    print("환영합니다", name+"님"+str(17))
    # f-string: 문자열끼리 이어서 쓰고싶을때 조금더 편하게 쓰게하는 기능
    # print(f"환영합니다 {17}님")
#
print(welcome("강은후"))

# print() : 절대 결과랑 상관없습니다. 단순히 콘솔에 보여지는 역할을 할뿐
# 결과는 함수를 출력햇을때, 나오는 값.
# 결과를 쓰는방법 return 




print("=====")
# 입력을 두개 넣어서 함수
# 자기소개를 반환하는 함수 
# "내이름은 OOO이고, ㅁㅁ살이야."
def introduce(name, age):
    # print(f"내이름은 {name}이고 {age}살이야.")  # 내이름은 강은후이고 17살이야.
    return f"내이름은 {name}이고 {age}살이야."
    print('안녕하세요')


print(introduce("강은후", 17))
# introduce("강은후", 17)


# None : 존재하지않는다.
print("mission 1============")
# 모스부호가 있는 계좌 내역을 찾아보자. 

account_details =[{'date':'0201','type':'withdraw','account':'211-854-6681','amount':132500,'memo':'-..', 'atmSection':'PA1101'},
{'date':'0205','type':'withdraw','account':'121-554-1820','amount':106000,'memo':'--', 'atmSection':'FG1001'},
{'date':'0205','type':'withdraw','account':'211-157-3580','amount':130000,'memo':'---', 'atmSection':'HT1010'},
{'date':'0207','type':'deposit','account':'202-3207-8819','amount':50000, 'memo':'Jovia'},
{'date':'0201','type':'pay','account':'554-6280-7772','amount':100000,'memo':'Emily'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':123000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':167000,'memo':'.-', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'260-415-2919','amount':16000,'memo':'John'},
{'date':'0204','type':'withdraw','account':'211-854-6720','amount':180000,'memo':'..-.', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'115-854-1280','amount':230000,'memo':'..', 'atmSection':'PA1101'},
{'date':'0202','type':'withdraw','account':'131-555-6000','amount':251000,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0203','type':'deposit','account':'243-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'221-554-6880','amount':300000,'memo':'-..', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':113700,'memo':'--', 'atmSection':'PA1101'},
{'date':'0204','type':'deposit','account':'206-415-2919','amount':16000,'memo':'Harry'},
{'date':'0201','type':'withdraw','account':'628-7490-5471','amount':213700,'memo':'---', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'128-2196-5471','amount':113700,'memo':'-.', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'PA1101'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..-.', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':310000,'memo':'..', 'atmSection':'HT1010'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':221000,'memo':'-.', 'atmSection':'PA1101'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0204','type':'deposit','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':300000,'memo':'-..', 'atmSection':'FG1001'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':313700,'memo':'--', 'atmSection':'HT1010'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':16000,'memo':'Ann'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':320000,'memo':'---', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':24000,'memo':'Betty'},
{'date':'0203','type':'deposit','account':'2463-31-5325','amount':15000,'memo':'Nugu'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Norman'},
{'date':'0201','type':'withdraw','account':'428-7190-5471','amount':371200,'memo':'-.', 'atmSection':'FG1001'},
{'date':'0204','type':'deposit','account':'2060-415-2919','amount':106000,'memo':'.-', 'atmSection':'HT1010'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':30000,'memo':'Betty'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':1000,'memo':'DrFisher'},
{'date':'0204','type':'withdraw','account':'2463-433-0205','amount':7050,'memo':'Samuel'},
{'date':'0204','type':'withdraw','account':'111-554-6880','amount':530000,'memo':'..-.', 'atmSection':'PA1101'},
{'date':'0201','type':'withdraw','account':'111-554-6880','amount':130000,'memo':'..', 'atmSection':'FG1001'},
{'date':'0202','type':'withdraw','account':'131-554-6000','amount':109400,'memo':'-.', 'atmSection':'HT1010'}]
morse_dict = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'}

# 미션 : 모스부호가 있는 좌 내역을 모두 찾아보자. 
# - memo에서 알파벳이 아닌거 => 숫자, 특수문자 =>모스무호

# 문자열변수.isalpha() => 알파벳으로만 있어야 True, 섞여있거나 없으면 False
# 문자열변수.isdigit() => 숫자로만 있어야 True,   섞여있거나 없으면 False
a = []
for i in range(len(account_details)):
    # print(account_details[i]["memo"])
    if account_details[i]["memo"].isalpha() == False:
        a.append(account_details[i]['memo'])
print(a)

# 모스부호를 해석 하기


# 해석하는 함수를 만들어보기
# - 입력 : 해석할 모스부호(리스트)
# - 결과 : 해석된 문자열(리스트)

def morse(answer):
    # morse부호 사전으로 통해서 해석을 해볼겁니다.
    morse_dict = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'}
    b = []
    for i in range(len(a)):
        # if a[i] == morse_dict:
        # 번역 : morse_dict에서 해당 key모스부호랑 연결되 value를 뽑으면된다.
        k=a[i]
        # print(morse_dict[k])
        b.append(morse_dict[k])
    #print(b)
    return b


# id = "ididididid"
# pw = "12345"

# login(id,pw)



print(morse(a))




# input() : 콘솔(터미널)에서 키보드로 문자열을 입력받는 함수
# 함수의 입력 : 기능에서 사용하는 필요한 데이터

# 과제1)월과 일을 입력 받아서 오늘 날짜 출력하는 함수 만들기
# 오늘날짜는 ___(입력값)__ 입니다.
def date(month_num, date_num):
    return f"오늘 날짜는 {month_num}월 {date_num}일 입니다"
print(date(1, 12))



# 과제2)가격을 입력받아서 1000원 할인된 금액을 결과로 반환하는 sale_price() 함수 만들기
# 예제데이터를 모두 사용하기 ----
def sale(price):
    return price - 1000
price1 = 1000
price2 = 2400
price3 = 12000
print(sale(price1))
print(sale(price2))
print(sale(price3))

# 과제3)반지름 r을 입력받고, 입력받은 반지름에 대한 원주(둘레)를 결과로 반환하는 함수를 만들어주세요. 
r1=5
r2=3
r3=10
def circle(r):
    return 2 * 3.14 * r
print(circle(r1))
print(circle(r2))
print(circle(r3))

# 과제4)리스트를 입력받아 모든 값를 더한 숫자를 결과로 반환하는 sum_num() 함수를 만들어봐라.
# 예제데이터를 모두 사용하기 ----
num_list1=[1, 3, 2, 10, 12, 11, 15]
num_list2=[1,3,5]
def sum_num(sum_list):
    num = 0
    for i in range(len(sum_list)):
        num += sum_list[i]
    return num
print(sum_num(num_list1))
print(sum_num(num_list2))








