# 객체(object) => 공장
# 현실세계 대상(데이터, 행동)동시에 존재

# class : 객체를 생성하는 틀
# - 속성(attribute): 데이터
# - 메서드(method): 행동, 함수 
    # - self : 맨앞에 넣어주기, 자기자신


# 회원 유저 객체를 생성하기 
# 데이터 : id, pw, name, phone
# 행동 : 로그인,비밀번호찾기
# id : agent@nis.com
# pw : python
# name : 이선
# phone : 010-1234-5678

# < 회원 유저 객 클래스 만들기>
class User1:
    # __init__(): 생성할때 생성자 메서드 사용 : 
    def __init__(self):
        # self.속성명(변수) : 나의 데이터 만들어주기
        self.id = "agent@nis.com"
        self.password = "python"
        self.name = "이선"
        self.phone = "010-1234-5678"
        

# 객체 틀로 찍어보기 => 인스턴스
# 인스턴스명 = 클래스이름()
id = User1()
# 인스턴스객체의 id를 알고싶어요.
# 인스턴스명.속성명
print(id.id, "id객체의 id속성이 나오기")


# <입력받은 데이터로 객체를 생성하기>
class User:
    # __init__(): 생성할때 생성자 메서드 사용 : 
    def __init__(self, myid, mypassword, myname, myphone):
        # self.속성명(변수) : 나의 데이터 만들어주기
        self.id = myid
        self.password = mypassword
        self.name = myname
        self.phone = myphone
        # 마케팅수신 무조건 동의할것 .
        self.marketing = True

    # 로그인검증메서드 : 함수 입력받은 id랑 비밀번호를, 내 id랑 pw랑 같으면 로그인, 다르면 계정을 확인해주세요.
    def login(self, input_id, input_pw):
        # 객체본인의 속성을 가져올때 : self.속섬명

        if self.id == input_id and self.password == input_pw:
            return "로그인 되었습니다."
        else:
            return "계정을 확인해주세요."

    # 비밀번호 찾기
    # - 아이디와 핸드폰번호를 받으면, 
    # - (동시에) 아이디와 핸드폰번호가 계정과 일치하면, 핸드폰번호로 비밀번호를 보내줍니다.
        #   {핸드폰번호}로 비밀번호 {pw}가 발송되었습니다. 라고 출력하기
    # - 계정을 확인해주세요.
    
    # f"{변수}문자열"

    def find_password(self, input_id2, input_phone2):
        if input_id2 == self.id and input_phone2 == self.phone:
                return f"{self.phone}으로 비밀번호 {self.password}가 발송되었습니다."
        else:
            return "계정을 확인해주세요."

# 은후 회원정보를 넣어서 객체를 만들어보기
# 인스턴스명 = 클래스이름(속성에 넣을 데이터)
eunhoo = User("agent@nis,com", "python", "은후", "010-3414-1181")

id = "agent@nis,com"
pw = "python"
phone = "010-3414-1181"
print(eunhoo.login(id, pw))
print(eunhoo.find_password(id, phone))

pi = User("agent2@nis.com","python","파이","010-1234-5678")
id2 = "agent2@nis.com"
phone2 = "010-1234-5678"
print(pi.login(id, pw))
print(pi.find_password(id2, phone2))

