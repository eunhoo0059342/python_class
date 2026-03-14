'''
함수 : 코드 묶음 => 하나의 기능 
- 코드 길어지면 어디에 무슨 코드 적었는지 모른다.
- 기능을 1번이상 사용하게 될때, 

# 독립적인 공간
# - 외부에서 어떤 값을 함수 전달하려면, 입력(인수,매개변수)을 사용해야한다.
# - 이때, 인수의 갯수와 매개변수의 갯수는 동일해야한다. 
def 함수이름(매개변수):
    코드
    return 결과값

함수이름(인수, 입력데이터 )

'''

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
print(morse(a))

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



print("mission 2============")
# 다음에 사용할 ATM 예측해라
for i in range(len(account_details)):
    # 인덱싱 : 무조건 있다는 가정하에 바로 뽑기 => 없으면 에러
    # 딕셔너리에서 key값으로 value를 뽑는방법 2가지 : key인덱싱, .get(key) 
    # print(account_details[i].get('atmSection'))
    if account_details[i].get('atmSection') != None:
        print(account_details[i]['atmSection'])

    # 해당값이 ~이냐 == is
    # account_details[100]

print("mission 3============")

# CCTV
criminal = [
[200,233,187,215,78,41,32,240,188,94],
[107,9,215,4,215,72,211,72,0,73],
[86,94,6,211,41,107,102,6,11,82],
[94,6,94,86,41,72,107,2,72,103],
[32,215,5,187,187,2,9,86,211,211],
[84,52,7,222,4,86,13,216,10,35],
[0,215,215,121,5,215,86,4,15,42],
[210,83,103,23,215,2,22,103,145,75],
[81,60,28,5,210,145,72,145,200,46],
[66,20,1,99,7,145,48,103,229,83],
]

#용의자
suspect1 = [
[32,15,225,17,187,12,9,86,90,20],
[200,233,87,215,78,41,32,20,1,5],
[10,6,14,8,111,723,109,12,72,103],
[12,25,115,217,107,72,66,86,4,198],
[107,9,215,4,215,72,211,72,0,75],
[107,9,215,4,215,72,211,72,0,75],
[0,90,215,121,5,130,86,4,130,42],
[147,248,90,24,86,130,98,55,12,2],
[81,60,28,25,210,145,72,145,130,46],
[66,20,1,99,7,145,48,103,229,52],
]

#용의자
suspect2 = [
[8,250,45,144,25,240,153,112,114,150],
[218,185,178,176,250,110,70,51,151,99],
[107,9,215,4,215,72,211,72,0,73],
[162,66,78,241,201,110,70,51,151,10],
[196,88,221,36,234,34,73,113,210,167],
[102,102,243,160,241,147,218,158,20,1],
[147,248,90,24,86,130,98,55,12,2],
[200,233,187,215,78,41,32,240,180,94],
[81,60,28,5,210,145,72,145,200,46],
[32,215,5,187,187,772,9,86,211,11],
]
#용의자
suspect3 = [
[200,233,87,215,78,41,32,240,180,94],
[166,220,1,99,7,145,8,13,29,80],
[32,15,225,17,187,12,9,86,90,20],
[10,6,14,8,111,723,109,12,72,103],
[107,9,215,4,215,72,211,72,0,75],
[84,52,7,222,4,86,13,216,10,35],
[147,248,90,24,86,130,98,55,12,2],
[200,233,187,215,78,41,132,20,40,94],
[81,60,28,25,210,145,72,145,200,46],
[12,25,115,217,107,72,66,86,4,198],
]

#용의자
suspect4 = [
[200,233,187,215,78,41,32,240,188,94],
[107,9,215,4,215,72,211,72,0,73],
[86,94,6,211,41,107,102,6,11,82],
[94,6,94,86,41,72,107,2,72,103],
[32,215,5,187,187,72,9,86,211,211],
[84,52,7,222,4,86,13,216,10,35],
[0,215,215,121,5,215,86,4,15,42],
[210,83,103,23,215,2,22,103,145,75],
[81,60,28,5,210,145,72,145,200,46],
[66,20,1,99,7,145,48,103,229,83],
]

#용의자
suspect5 = [
[34,35,242,202,149,214,221,3,90,20],
[200,233,87,215,78,41,32,20,1,5],
[10,6,14,8,111,723,109,12,72,69],
[12,25,115,217,137,72,66,198,4,12],
[107,9,215,4,215,72,198,94,0,47],
[107,9,215,204,232,72,93,72,0,75],
[3,90,215,121,5,130,86,4,130,42],
[147,248,90,24,86,130,98,55,12,2],
[81,60,28,25,210,145,72,145,202,6],
[147,248,17,47,62,65,8,55,12,52],
]

# cctv랑 용의자의 데이터를 비교하는 점수를 결과로 반환하는 함수를 만들어라
# 비교하면서 동일한부분이 많을수로 높은 점수를 줘서 높은 점수의 용의자가 범인이 된다.
def face(suspect_face, cctv_face):
    num = 0
    for i in range(len(suspect_face)):
        #print(suspect_face[i])
        for j in range(len(suspect_face[i])):
            #print(suspect_face[i][j])
            #print(cctv_face[i][j])
            if suspect_face[i][j] == cctv_face[i][j]:
                num += 1
    return num
print(face(suspect1, criminal))
print(face(suspect2, criminal))
print(face(suspect3, criminal))
print(face(suspect4, criminal))
print(face(suspect5, criminal))




# 나머지 https://www.acmicpc.net/problem/3052
# 문자열반복 https://www.acmicpc.net/problem/2675
# OX퀴즈 https://www.acmicpc.net/problem/8958


