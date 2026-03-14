# 이선 19004
# 블루웨일 60817
# 주파수 15


# 통신 서버(서비스를 제공하는 컴퓨터) 를 만들기
class Server:
    def __init__(self):
        # NIS server를 이용해 통신 할 수 있는 transmitter 리스트
        # 사용할수 있는 유저 리스트
        self.trm_list = []
        #각 주파수 별로 현재 전파되고 있는 메시지
        self.msg_list = [None,'Hi there','>>#=@.......$#^','2_8_...M..{{{#','243','today\'s news broadcasting.','this is NIS server','%$#&^#^','Input secret code.','@*DW)R_#IO-','#$$$@__&*$%','+)@!((^@',';nNiIssssss023;','16837','\sdkf','...Hel*^%-!Pp....','call with a secret code','wewrh','service location','add user','not now','commercial zone','438759234','/32.1/2/','&*)','q3284023','.....','add transmitter','....008800888','fire','438759234','baseball','&*)','q3284023','.....','........','no excuses','hey','...bal','/32.1/2/','2375','000','.....']
    
    # 정상적인 사용자를 등록하는 메서드
    # 입력 : 유저(id, 주파수)
    def addUser(self, user):
        self.trm_list.append(user)
        print('New user', user.id ,'added.')
        


    def delUser(self, id):
       for i in range(len(self.trm_list)):
        if self.trm_list[i].id == id:
            del self.trm_list[i]
            print('delete completed.')

    def emitMsg(self, msg):
        for freq in self.msg_list:
            freq = msg

    # 유저의 주파수에 해당되는 메세지를 출력한는 메서드 만들기
    # - 입력 : 유저 객체를 데이터
    # - 결과 : 유저의 주파수에 해당되는 메세지르 출력하기
    # (1)메세지 받고자하는 유저가 서버에 등록되어있는지를 확인해야한다.
    # (2)등록되어 있다면, msg_list에서 해당 주파수위치의 메시지를 출력하기
    def massege(self, user):
        if user in self.trm_list:
           print("등록된 유저이다.")
           return self.msg_list[user.freq]
        else:
           print("등록되지 않은 유저이다")
          



# 수신자(서버를 이용한 클라리언트)
class Transmitter:
    def __init__(self, id):
        # id, 주파수
        self.id=id
        self.freq = 5
        print('Transmitter', id,'enrolled.')

    # 주파수를 변경하는 메서드
    # - 입력값 server(서버객체), newFreq(주파수, 숫자)
    def changeFreq(self, server, newFreq):
      if newFreq <= len(server.msg_list):
        self.freq=newFreq
        print('Frequency set to', newFreq, 'completed.')
      else:
        print('Invalid Frequency.')
    
    def send(self, server, msg):
        server.msg_list[self.freq] = msg
    # 서버와 연결을 시도
    def connect(self, server):
        return server.massege(self)


# 블루웨일 <-> 이선 2명이 통신유저 인스턴스를 생성하기 하기
# 이선 19004
# 블루웨일 60817
# 주파수 15
print("======")
# (1) 블루웨일 <-> 이선 2명이 통신유저 인스턴스를 생성하기 하기
leesun = Transmitter(19004)
bluewhale = Transmitter(60817)
# 이선의 주파수를 출력해보자.
print(leesun.freq)

# (2) 통신 서버를 생성하기
server = Server()
# (3)이선의 주파수를 변경하기 => 서버객체, 새로운주파수 입력을 필요해
# (4)블루웨일의 주파수로 변경하기
leesun.changeFreq(server, 15)
bluewhale.changeFreq(server, 15)


# (5)이선이가 서버랑 연결하기
# 
server.addUser(leesun)
print(leesun.connect(server))
