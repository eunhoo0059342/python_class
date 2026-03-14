# 💪 수업 준비사항 💻
# 1. 하우코딩 수업 NIS 로그인(미션풀때)
# ＊ID: agent@nis.com
# ＊PW: python
# 2.  VSCode LiveShare 링크 전달



#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# 리스트연산자 : in (포함여부), not in
alphabet = ['a','b','c','d','a','a','a']
print('e' not in alphabet)
# 리스트안에 몇개가 들어가 있느지 갯수를 원할때 함수 리스트변수.count(찾는데이터)
print(alphabet.count('a'))

print("mission 1======")
# 전선을 리스트로 만들어서 관리하기
# 파란색, 하얀색, 검정색
# 정답 : "cut the ___ wire"
answer = ["blue", "white", "black"]
if "red" not in answer:
    print("cut the "+ answer[1] +" wire")
# 마지막 전선이 하얀핵이면(같다),
# answer[2] : 2번째 != 마지막: 오른쪾엣 첫번째
elif answer[-1] == "white":
    print("cut the "+ answer[-1] +" wire")
# 파란색 전선의 "갯수"가 1개 이상이라면,
elif answer.count("blue") >= 1:
    print("cut the "+ answer[1] +" wire")
else:
    print("cut the "+ answer[-1] +" wire")
    
    
print("mission 2======")    
# 하얀색, 파란색, 빨간색
answer2 = ["white", "blue", "red"]
if "red" not in answer2:
    print("cut the "+ answer2[1] +" wire")
# 마지막 전선이 하얀핵이면(같다),
# answer[2] : 2번째 != 마지막: 오른쪾엣 첫번째
elif answer2[-1] == "white":
    print("cut the "+ answe2r[-1] +" wire")
# 파란색 전선의 "갯수"가 1개 이상이라면,
elif answer2.count("blue") >= 1:
    print("cut the "+ answer2[1] +" wire")
else:
    print("cut the "+ answer2[-1] +" wire")
    


print("mission 3======")
# <조건문>
# 비교연산자: == != > < >= <=
# 포함연산자: in , not in (문자열, 리스트)
# 논리연산자: 조건 and 조건(동시에), or(둘중에 하나라도) 
# <과제>
answer3 = ["yellow", "blue", "white", "black", "red"]

if answer3[3] != "black" :
    print("cut the "+answer3[1] +" wire")
elif answer3.count("red") == 1 and answer3.count("yellow") >= 1 :
    print("cut the "+answer3[0] +" wire")
elif "blue" not in answer3 :
    print("cut the "+answer3[3] +" wire")
else:
    print("cut the "+answer3[-1] +" wire")
