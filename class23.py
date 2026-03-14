route = {
    'a':{'b':1772,'c':5805,'f':5546,'h':730},
    'b':{'a':1772,'d':3010,'g':2562},
    'c':{'a':5805,'d':4111,'e':1081,'f':1621},
    'd':{'b':2010,'c':4111,'e':2892,'g':2908,'h':3092,'j':517},
    'e':{'c':1081,'d':2892,'f':4082,'i':506,'j':290},
    'f':{'a':5546,'c':1621,'e':4082,'i':627},
    'g':{'b':2562,'d':2908,'h':903},
    'h':{'a':730,'d':3092,'g':903,'j':3900},
    'i':{'f':627,'e':506},
    'j':{'d':517,'h':3900,'e':290}
}
# a 출발 - e까지 가고싶습니다.
# 실선 : 갈 수 있는 도로
# 점선 : 공사중이여서 갈수 없는 도로

print("mission 1 ============")
# rounte에서 점선에 해당되는 도록 제거
# [리스트 추가,수정,삭제]
# .append
# 변수[인덱스]= 새로운데이터: 새로운데이터로 수정
# .pop() : 맨뒤의 값을 뽑아서 삭제 / .pop(인덱스) : 해당 인덱스를 뽑아서 삭제

# [딕셔너리 추가,수정,삭제]
# 추가,수정 : = 활용 
# => 변수[key]=새로운데이터
# 삭제 .pop('key')  : 해당 key를 뽑아서 삭제

# 예제) route 'k' 값으로 "안녕하세요" 추가해보자 
route["k"] = "안녕하세요"
# print(route)
# 예제) route 'k' 값으로 "hello" 수정해보자 
route["k"] = "hello"
# print(route)
# 예제) route 'k' 값을 삭제하기
del_data = route.pop("k")
# print(route)
print(del_data)
# 힌트 : 빼고싶은값이 안쪽에 있는 딕셔너리이다.

route["f"].pop("e")
route["e"].pop("f")
route["f"].pop("c")
route["c"].pop("f")
route["c"].pop("d")
route["d"].pop("c")
route["h"].pop("j")
route["j"].pop("h")
route["d"].pop("h")
route["h"].pop("d")
print(route)
# route에서 점섬의 데이터를 삭제
# f-e, f-c, c-d, h-d, h-j

print("mission 2 =============")
# a부터 -e까지 가는 경로(문자열) => 리스트 
# 각 경로에 대해서 몇시간이 걸리는가


# a-f-i-e : 지점 4개인데 도로3 소요시간 3개
    # - a(도로의 시작점)-f(도로의 끝점)도로
    # - f-i도로
    # - i-e도로
    # a-c-e : 지점 3개 도로 2



# 경로 리스트
#pass_route_list=['afie',"ace","abde","abgde","ahgde","ahgbde","abdje","abgdje","ahgdje","ahgbdje"]
pass_route_list = ['afie', 'ace', 'abde', 'abdje', 'abgde', 'abgdje', 'ahgde', 'ahgdje']

route_time_list = []
# 모든 경로의 시간 (전체)
route_time_all = 0 # 아닙니다.
# 각각의 경로에대한 반복문
# - 경로 별로 개별 소요시간을 구하고싶어요.()
# - 경로 안에는 여러개의 도로 존재합니다.
for i in range(len(pass_route_list)):
    pass_route = pass_route_list[i] 
    route_time = 0

    # 구하야하는 값:각 도로별 소요시간의 합계 
    #print("도로의갯수", len(index_pass_route)-1)
    # 각각의 도로에대한 반복문#############################
    for j in range(len(pass_route) - 1):
        start = pass_route[j]
        end = pass_route[j+1]
        road_time = route[start][end]
        
        # 경로의 소요시간 : 모든 도로 소요시간의 합
        route_time += road_time
        print("--",start+"-"+end+"도로", "/ 도로별소요시간",road_time)
    ################################################

    route_time_list.append(route_time)
    print("경로",pass_route, "| 소요시간",route_time,end='\n\n')


print(route_time_list)
# <탐색 : 현재값 다음값>
# alpha = ['abc','def','hijk']
# # 인덱스
# for i in range(len(alpha)-1):
#     print(i,alpha[i],i+1, alpha[i+1])


print("mission 3 =============")
print(min(route_time_list))


# <변수이름>
# - 분류_구체적인용도_타입 (권장)
# month_text = "12월"
# n = 12 



# (과제)
# 1. 과제 안 내신분...? https://www.acmicpc.net/problem/5597 => 토요일 날 풀이
# 2. 열개씩 끊어서 출력하기 https://www.acmicpc.net/problem/11721
# 3. 윤년 https://www.acmicpc.net/problem/2753 => 문제만 잘보시고 이해안되면 카톡
