# 💪 수업 준비사항 💻
# 1. 하우코딩 수업 NIS 로그인
# ＊ID: agent@nis.com
# ＊PW: python
# 2.  VSCode LiveShare 링크 준비


# <데이터타입>
# 1. 숫자 Number
# - 정수 int() / 실수 float()
# 2. 문자열 String ""
# - 중요한 특징 : 인덱스(0번부터 시작하는 ~ 숫자)
# - 인덱싱 : 문자열변수[인덱스] => 인덱스 번호로 특정 문자 뽑기
# - 슬라이싱 : 문자열변수[시작 : 끝] => 인덱스 번호로 시작번호부터 끝-1 까지의 문자 자르기
# - 문자열 주요 메서드
#   - .upper()
#   - .lower()
#   - .strip()
#   - .replace("찾는문자","바꿀문자")
# - len() 함수 : 문자열의 크기, 길이 


text = "메리 크리스마스"
# 예제) 사람 4번째 글자를 뽑아서 출력해주세요.
print("인덱싱",text[3])
# print("안녕","나는","산타","이다")

# 예제) 사람기준 4번째부터 끝까지의 글자를 잘라서 출력해주세요.
print(text[3: ])

lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# 문자열변수.find("찾는 단어") 문자열에서 특정 문자의 위치를 찾아 인덱스 번호를 알려주는 함수 

# 예제) ""standard"" 몇번째에 있나요?
start_index = lorem.find("standard")
print(start_index)
# 예제 "1500s" 몇번째에 있나요?
last_index = lorem.find("1500s")
# lorem 문자열에서 "standard"~ "1500s" 까지를 잘라서 출력하게 해주세요!
# 151 = 마지막 인덱스 번호 + len("1500s")
print(lorem[start_index:last_index+ len("1500s")])


# 변수를 만드는 기준
# 1. 나중에 또 사용할것 같은가? => 무조건 변수
print("mission 1 ===================")
# start ~ end사이를 잘라서 출력해달라 
file_b ='djhfaheu___wehiehrhlsfhouhewwehr1238364892hrehwfwhelhewlehrlewhiorhhf3824863___883@hre93734084fdfhieelwhfhieistart#.redro lacitebahpla yb kcatta trats eW .yti@sr@@evinu,tna@lp rae@@lcun,llam@ gni@@ppoh@s,lla@h@ y@tic,tekr@am kcots,noi@tats eci@l@op,ret@aeht:secalp gniwollof fo eno si tegrat ehT#endhfdhsifohifeifhlk368537djs89hds83e____89fwgafg3dbsjhgdiutwfw823___t93g3%@iu3977e&egd37dheehdgsaioiowi'

first = file_b.find("start")
second = file_b.find("end")

answer = file_b[first+ len("start"): second]
# #.redro lacitebahpla yb kcatta trats eW .yti@sr@@evinu,tna@lp rae@@lcun,llam@ gni@@ppoh@s,lla@h@ y@tic,tekr@am kcots,noi@tats eci@l@op,ret@aeht:secalp gniwollof fo eno si tegrat ehT#

print("mission 2 ===================")
# 뒤집기 reverse => # 문자열변수[::-1]
answer = answer[::-1]
# #The target is one of following places:thea@ter,po@l@ice stat@ion,stock ma@rket,cit@y @h@all,s@hopp@@ing @mall,nucl@@ear pl@ant,unive@@rs@ity. We start attack by alphabetical order.#

# @ 불필요하다. 찾아서 없애주기 ''빈문자열 활용

print(answer.replace("@",""))

answer2 = "theater,police station,stock market,city hall,shopping mall,nuclear plant,university"
# 사람 : ,기준으로 여러개의 데이터를 인식
# 컴퓨터 : 문자열 1개


# 단일 데이터 타입 =====
# 1. 숫자 Number
# - 정수 int() / 실수 float()
# 2. 문자열 String ""
# 다중 데이터 타입 ===
# 리스트 : 여러개의 데이터(요소)를 저장하는 데이터타입 [요소, 요소, 요소]

# 8반 친구들로 리스트 만들기 4명정도
class8 = ["A", "B", "C", "D"]
print(class8)

# 문자열을 나눠서 리스트 변환
answer2 = "theater,police station,stock market,city hall,shopping mall,nuclear plant,university"
# 사람 : ,기준으로 여러개의 데이터를 인식
# 컴퓨터 : 문자열 1개

# 문자열변수.split("구분인자")
answer2 = "theater/police station/stock market/city hall/shopping mall/nuclear plant/university"
list1 = answer2.split("/")
print(list1)
# ['theater', 'police station', 'stock market', 'city hall', 'shopping mall', 'nuclear plant', 'university']
# 정렬 .sort()
list1.sort()
print(list1)
# ['city hall', 'nuclear plant', 'police station', 'shopping mall', 'stock market', 'theater', 'university']




