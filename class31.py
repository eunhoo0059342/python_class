# 색의 삼원색 RBY
# 빛의 삼원색 RGB => 클래스로 다루기


# pixel클래스
# - 속성(객체 내부 데이터) : r,g,b
class pixel:
    def __init__(self, r, g, b):
        self.red=r
        self.green=g
        self.blue=b


##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.
import random
import copy
random.seed(16)
paintingsample = [[0]*8 for i in range(8)]
for i in range(8):
  for j in range(8):
   paintingsample[i][j]=pixel(random.randint(0,255), random.randint(0,255), random.randint(0,255))
painting1=copy.deepcopy(paintingsample)
##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.
pic1 = copy.deepcopy(painting1[0])
pic1[0].red = 0
pic1[1].red = 1
pic1[2].red = 0
pic1[3].red = 0
pic1[4].red = 0
pic1[5].red = 0
pic1[6].red = 1
pic1[7].red = 1
pic2 = copy.deepcopy(painting1[1])
pic2[0].red = 0
pic2[1].red = 1
pic2[2].red = 1
pic2[3].red = 0
pic2[4].red = 1
pic2[5].red = 1
pic2[6].red = 1
pic2[7].red = 1
pic3 = copy.deepcopy(painting1[2])
pic3[0].red = 0
pic3[1].red = 1
pic3[2].red = 1
pic3[3].red = 0
pic3[4].red = 0
pic3[5].red = 1
pic3[6].red = 0
pic3[7].red = 0
pic4 = copy.deepcopy(painting1[3])
pic4[0].red = 0
pic4[1].red = 1
pic4[2].red = 1
pic4[3].red = 0
pic4[4].red = 0
pic4[5].red = 1
pic4[6].red = 0
pic4[7].red = 1
pic5 =copy.deepcopy(painting1[4])
pic5[0].red = 0
pic5[1].red = 0
pic5[2].red = 1
pic5[3].red = 0
pic5[4].red = 1
pic5[5].red = 1
pic5[6].red = 0
pic5[7].red = 1
pic6 =copy.deepcopy(painting1[5])
pic6[0].red = 0
pic6[1].red = 1
pic6[2].red = 0
pic6[3].red = 1
pic6[4].red = 1
pic6[5].red = 0
pic6[6].red = 0
pic6[7].red = 0

pic7 = copy.deepcopy(painting1[6])
pic7[0].red = 0
pic7[1].red = 1
pic7[2].red = 0
pic7[3].red = 0
pic7[4].red = 1
pic7[5].red = 1
pic7[6].red = 1
pic7[7].red = 1
pic8 = copy.deepcopy(painting1[7])
pic8[0].red = 0
pic8[1].red = 1
pic8[2].red = 0
pic8[3].red = 1
pic8[4].red = 0
pic8[5].red = 0
pic8[6].red = 1
pic8[7].red = 0
painting2=[]*8
painting2.append(pic1)
painting2.append(pic2)
painting2.append(pic3)
painting2.append(pic4)
painting2.append(pic5)
painting2.append(pic6)
painting2.append(pic7)
painting2.append(pic8)


##pixel 클래스 객체 painting1, painting1 생성부. 미션 수행 시 수정하지 않습니다.

# painting1 painting2 조작된 부분을 찾아라 => 2차원리스트
# 2차원리스트의 모든 값뽑기 이중for문을 사용해보기

# 빨,초,파 중에서 조작된 데이터가 있다고 한다.
# => 조작되었다, 빨,초,파중에서 p1,p2에서 서로 다른 값이 존재하면 해당 색상은 조작된것이다.
print(painting1, painting2)
for i in range(len(painting1)):
    for j in range(len(painting1[i])):
        # 객체 빨강(속성) 만출려해보기  => 인스턴이름.속성이름
        if painting1[i][j].red != painting2[i][j].red:
            print("빨간색이 조작되었습니다.")
        if painting1[i][j].blue != painting2[i][j].blue:
            print("파란색이 조작되었습니다.")
        if painting1[i][j].green != painting2[i][j].green:
            print("초록색이 조작되었습니다.")
        #   print(painting2[i][j])
    

print("=======mission 2 =================")
# https://namu.wiki/w/%EC%95%84%EC%8A%A4%ED%82%A4%20%EC%BD%94%EB%93%9C

# p1, p2 빨강색에서 다릅니다.
# p2에서 빨강색에 암호를 심어놨다. => 빨강색의 마지막 비트에 있는 데이터를 가져오기 

# 비트 : 가장 작은 데이터 단위
# - 1bit : 0또는 1 로 표현가능한 단위 <= 2진수로 변환한다음에 캐치
# - 1byte = 8bit    => 문자 1개 표현하는 크기, 알파벳 한글 2바이트

# 숫자를 2진수로 바꾸는 방법  bin(숫자) => 2진수 문자열
# (1)이차원리스트에서 빨강한 뽑아보고
# (2) 2진수로 바꿔보기
# (3) 2진수의 마지막 바트값 출력하기
# 0b1111011*0*

result_str = ''
# 이차원리스트
# (1)
for i in range(len(painting2)):
    # i는 존재가능 => 행값 painting2[i]
    # 비트를 행별로 모으기 => ASCII 코드로 변환
    # (2)
    num_lst = ['0b']
    # num_list = ''
    for j in range(len(painting2[i])):
        # i, j 존재가능^^ => 행안의 열값 painting2[i][j]
        bin_num = bin(painting1[i][j].red)
        #print(bin_num[-1])
        num_lst.append(bin_num[-1])
        
    # 행단위로 아스키코드로 변환 => "".oin(리스트)
    print(int("".join(num_lst),2))
    # ASCII 코드는 => 문자 => 숫자    / 숫자를 => 문자
    # chr(숫자) : ASCII 변환하기
    print(chr(int("".join(num_lst),2)))
    result_str += chr(int("".join(num_lst),2))
        
# 리스트
print(result_str)
result_str = ''
for i in range(len(painting2)):
    num_lst = ['0b']
    # num_list = ''
    for j in range(len(painting2[i])):
        # i, j 존재가능^^ => 행안의 열값 painting2[i][j]
        bin_num = bin(painting2[i][j].red)
        #print(bin_num[-1])
        num_lst.append(bin_num[-1])
    # 행단위로 아스키코드로 변환 => "".oin(리스트)
    print(int("".join(num_lst),2))
    # ASCII 코드는 => 문자 => 숫자    / 숫자를 => 문자
    # chr(숫자) : ASCII 변환하기
    print(chr(int("".join(num_lst),2)))
    result_str += chr(int("".join(num_lst),2))
     
print(result_str)
      
      










