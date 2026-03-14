# 💪 수업 준비사항 💻
# 1. 하우코딩 수업 NIS 로그인(미션풀때)
# ＊ID: agent@nis.com
# ＊PW: python
# 2.  VSCode LiveShare 링크 전달

print("main파일")


# <데이터타입>
# 1. 숫자타입 Number
# - int() : 정수타입
# - +,-,*,/,//(몫),%(나머지),**(제곱)

# 2. 문자열타입 String : ""
# - +(문자열 이어붙이기), *(반복)
# 10 +"10" # 
# 10 + 10   => int()
# "10"+"10" => str()
# - len(데이터) : 길이 구하는 함수
# - 특징 : 순서(=인덱스, index, 0번부터 센다., 순서)
# - 인덱싱 문자열변수[index] : 해당 인덱스번호의 값이 뽑힌다.
# 정방향 인덱스 : 왼쪽부터 0,1,2,3
# 역방향 인덱스 : 오른쪽부터 ...,-3,-2,-1 => 마지막 값을 -1
# - 슬라이싱 : 문자열변수[시작인덱스: 끝 인덱스] : 시작부터 끝 전까지 잘라주는 것 


a = "apple"

# 예제) a변수의 길이를 구해서 출력해보기
print(len(a))
# 예제) 'a' 몇번째 일까요? 0번이다.  
print(a[0],"<= a변수의 0번째 값을 뽑기")
# 예제 a변수에서 3번째 값을 뽑아 출력해주세요.
print(a[3])
# 예제) a변수에서 마지막값을 뽑아서 출력해보기
print(a[-1])

ttt = 'hello world'
# 0번부터 5번까지를 잘라서 출력하기 => 슬라이싱
# 문자열변수[시작인덱스: 끝인덱스]
# - 맨앞에서 시작하고 싶다 : 변수[: 끝번호]
# - 맨 끝까지 자르고싶다. 변수[시작번호:]
print(ttt[:6])


print("mission 1 =======================")
# 글자가 512자인 정상적인 파일을 찾아라. 
file_a = 'ajkek__ihhfyfy7867gjk_,hi_bjfuky_gfu,hjkshfkyf_jgeu______,leieowry#ekh_iehkfejewjgdfe_48635ihf64___,guulhf_h,gdtj#gg#g65_ffy74764645v84djhf#uh8y__,h_jmehie##hejukjvd__,648fd7sgk4dl#k3_jhr82tej#223_______,___'
file_b = 'djhfaheu___wehiehrhlsfhouhewwehr1238364892hrehwfwhelhewlehrlewhiorhhf3824863___883@hre93734084fdfhieelwhfhiei#startmyg^efac^pohSkcans^tekram^ytisrevinu^erotStnemtraped^llaHytic^krap^tnaruatser^retaehTeivomend#hfdhsifohifeifhlk368537djs89hds83e____89fwgafg3dbsjhgdiutwfw823___t93g3%@iu3977e&egd37dheehdgsaioiowi'
file_c = 'asdfgwheu2963__jewjeyjkejeygey7627#36825h___,__d#ufigwfk,dfuigeuwke__,s324dfekd7he68___,jehkfk,fk73r#hkg743gjgu_,68fthk__#hfyu744ch_,ds##e_________####u#__,#j_#ab__,#nbu#_b_a_bb_b#bbbbrbby__##bb__bb##3#bb#1b_bb__,,bbbb#th_,64hdd##jdueh#hd72_,jey8___,37dek7dejebwjwkey1n_,ju,,_jeuwweejgeekeur_jege8363jfbdk'

print(len(file_a))
print(len(file_b))
print(len(file_c))


file_d = file_a + file_c
print(len(file_d))
print(file_d)


print("mission 2 =======================")
# 360번 ~ 429까지의 잘라달라
print(file_d[360: 430])

print("mission 3 =======================")
# len(데이터) : 
# 문자열의 내장메서드 : 문자열에서 할수 있는 기능 => 파이썬 자체적으로 만든 
# - 문자열변수.upper() : 대문자로 만들어주기
# - 문자열변수.lower() : 소문자로 만들어주기
# - 문자열변수.strip('없앨문자') : 양끝 문자를 없애기
# - 문자열변수.replace("찾는문자","바꿀문자")
# ...

ttt = "christmas"
print(ttt.upper())
ttt2 = "MerrY"
print(ttt2.lower())

ttt3 = "           안녕   하세요       "
print(ttt3.strip(" "))


file_e = file_d[360: 430]
# __,#j_#ab__,#nbu#_b_a_bb_b#bbbbrbby__##bb__bb##3#bb#1b_bb__,,bbbb#th_,
# (1)file_e에서 ","를 찾아서 "" 빈문자열로 바꾸기
# 문자열변수.replace("찾는문자","바꿀문자") => 찾아서 없애기로 응용이 가능
file_e = file_e.replace(",","")
# (2)file_e에서 "#"를 찾아서 "" 빈문자열로 바꾸기
file_e = file_e.replace("#","")
file_e = file_e.replace("_","")
file_e = file_e.replace("b  ","")
print(file_e)


