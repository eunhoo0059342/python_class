'''
객체 : 속성(데이터)  & 메서드(기능)

<데이터>
8. 객체

'''

# 데이터의 한 종류써 객체를 다루기
# 누가 무엇을 할건지
# 누구(주체)의 데이터, 누구의 기능
# 객체.속성 / 객체.메서드
#Code


# 클래스 : 목소리에 대한 데이터
# 클래스 : 객체 틀(틀로 찍어서 인스턴스객체 생성)

class voice:
    def __init__(self, tone, pitch, frequency, speed, decibel):
      self.tone = tone #85~255
      self.pitch = pitch #60~300
      self.frequency = frequency #100~400Hz 
      self.speed = speed #0~500spm
      self.decibel = decibel # 50~2000


# 클래스 : 로봇
# - 속성 : 나이, 이름(숫자,문자, ... 데이터)
# - 메서드 : 출력하다, 나이를 더해주다. (행동, 함수)
class park_info_robot:
    def __init__(self, list, name=0):
      # 처음 생성될때, 
      self.mylist = list  # 들은 음성 리스트(list1,list2)
      self.name = name  # R1
  
    # 메서드 (기능& 추가적 데이터로 갖을수 있다.)
    def say_hi(self):
      print('Hi, ask me anything.')
    

    def time_voice(self, time):
        # print(self.mylist)
        
        for i in range(len(self.mylist)):
           index_mylst = self.mylist[i]
           if index_mylst['time'] == time:
              print(index_mylst['voice'])
        
         
       
    # 각 로봇이 들은 음성리스트 중에서 (나자신의 mylist에 들어가 있다.)
    # 내가 원하는 시간을 전달했을때(시간을 입력받기, 매개변수), 
    # 해당 시간의 음성을 출력하는 기능 만들어주기




#voice 객체 생성부. 미션 수행시 수정하지 않습니다.
# 리스트 타입 

# 리스트별로 시간과 목소리를 저장하고 있습니다.
# list1 리스트 타입 => 안에 딕셔너리 => voice 키 인스턴스객체가 들어가있을뿐
list1 = [
   {'time':2050,'voice':voice(183,70,389,196,19)},
   {'time':2306,'voice':voice(214,200,230,13,54)}
   ]
list2 = [{'time':1114,'voice':voice(205,82,270,227,68)},{'time':1744,'voice':voice(167,73,302,445,35)},{'time':2311,'voice':voice(177,230,266,446,51)}]
list3 = [{'time':2250,'voice':voice(98,191,229,208,52)},{'time':1402,'voice':voice(109,241,197,224,33)}]
list4 = [{'time':1835,'voice':voice(195,290,137,471,61)},{'time':1440,'voice':voice(178,299,332,22,58)},{'time':1849,'voice':voice(162,250,192,320,61)}]
list5 = [{'time':1728,'voice':voice(160,285,327,439,60)},{'time':2340,'voice':voice(156,88,212,25,52)},{'time':2340,'voice':voice(96,268,113,170,70)}]
list6 = [{'time':1940,'voice':voice(203,103,340,10,18)},{'time':2340,'voice':voice(152,278,120,357,66)},{'time':1356,'voice':voice(174,215,266,106,41)}]
list7 = [{'time':1300,'voice':voice(103,107,258,430,19)},{'time':1413,'voice':voice(85,80,279,30,11)},{'time':1527,'voice':voice(116,181,248,144,22)}]
list8 = [{'time':1740,'voice':voice(194,86,391,68,19)},{'time':1627,'voice':voice(107,248,171,351,35)},{'time':2217,'voice':voice(88,101,278,434,10)}]
list9 = [{'time':2340,'voice':voice(151,270,113,170,70)},{'time':2340,'voice':voice(152,278,120,356,66)},{'time':2405, 'voice':voice(150,200,300,460,10)},{'time':2416, 'voice':voice(230,152,258,200,65)}]
#voice 객체 생성부. 미션 수행시 수정하지 않습니다.
 
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.
# 로봇생성시 필요한 내용 : 리스트 & 이름
rb_1 = park_info_robot(list1, 'R1')
rb_2 = park_info_robot(list2, 'R2')
rb_3 = park_info_robot(list3, 'R3')
rb_4 = park_info_robot(list4, 'R4')
rb_5 = park_info_robot(list5, 'R5')
rb_6 = park_info_robot(list6, 'R6')
rb_7 = park_info_robot(list7, 'R7')
rb_8 = park_info_robot(list8, 'R8')
rb_9 = park_info_robot(list9, 'R9')

# 객체의 형태를 정의하는 구간 => class
# rb_1 첫번째 로봇을 출력해보기.
# 참고) 로봇은 list, name의 속성을 갖고 있고, say_hi 메서드(함수)를 갖고 있습니다.
print(rb_1.mylist)
print(rb_1.name)
rb_1.say_hi()


# 객체를 생성고 사용하는 구간 => 인스턴스객체


# def 함수이름() :


# 함수이름()
print("=====")
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.
rb_1.time_voice(2340)
rb_2.time_voice(2340)
rb_3.time_voice(2340)
rb_4.time_voice(2340)
rb_5.time_voice(2340)
rb_6.time_voice(2340)
rb_7.time_voice(2340)
rb_8.time_voice(2340)
rb_9.time_voice(2340)




# 로봇한테 목소리를 출력하는 함수
# 시간을 전달하면 해당 시간에 기록된 음성만 출력하는 메서드를 각 로봇마다 만들어줘야합니다.
# 로봇 9개
# 각 로봇이 들은 음성리스트 중에서 내가 원하는 시간을 전달했을때, 해당 시간의 음성을 출력하는 기능 만들어주기
# 로봇(객체) - 자동차 창문내리는 기능 => 만들때 갖고 있으면 좋겠다. 

# 클래스안이 아니다.
