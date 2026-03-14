# 경안고등학교
'''
집합(set) 고1-2학기
: 중복을 혀용하지 않습니다.
형태 : {원소,원소,원소} set([])
: 순서가 없다. => 리스트list()로 변환해서

(1) 집합의 연산자
- A&B 교집합 : 두집합사이의 공통된 것
- | 합집합 : 두집합 모두
- A-B 차집합 :A에서 B와 관련되 내용을 빼기
- subset 부분집합 : 부분집합이냐? issubset
- disjoint 서로소 : 공통된게 없는 집합 관계 => isdisjoint

'''
unknown = ['oak', 'guitar', 'butter','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee', 'ring', 'sun', 'bear','space','tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup']
print(set(unknown))


# a기관이 참여한 프로젝트
a_pj = {'Food Nutrition', 'Legal Services', 'pharmaceutics','Cement and steel', 'Agriculture industry', 'Mining','Artificial Intelligence', 'Psychology','Vocational Rehabilitation', 'Plant-Based food','Transport', 'Urbanisation', 'Postal and Delivery', 'Financial Services', 'Travel and Leisure'}
# c기관이 참여한 프로젝트
c_pj = {'Systems Engineering', 'Data Science', 'Drones and Robots','Information Technology', 'Neurocomputing', 'Aerospace', 'Cloud Systems', 'Materials','Artificial Intelligence', 'Food Nutrition', 'Digital Computing','Software Farm', 'Power Sectors', 'Networking', 'Database', 'Psychology'}
# # d기관이 참여한 프로젝트
d_pj = {'Data Researching','Government Services', 'Artificial Intelligence','Telecommunication','Construction', 'Urbanisation', 'Legal Services','Physical Assets', 'Banks and Cashes', 'Labour and Capital','Education', 'Financials', 'Drones and Robots'}

# a, c,d가 모두 참여한 공통 프로젝트 이름(교집합)
# - A&B 교집합 : 두집합사이의 공통된 것

print(a_pj&c_pj&d_pj)




################################
'''
반복문 for문 : 횟수반복

for 반복변수 in 반복조건: 
- 반복조건에 있는 데이터가 하나씩 나오면서 반복변수에 저장되면서 반복 

(1) 기본형 
for i in range(횟수):

(2) 리스트 반복
for v in 리스트 : 

(3) 딕셔너리의 반복:
for k, v in dict.items():
    print(k,v)

(4) 튜플 반복:
for t in tuple_data:


'''
unknown = ['oak', 'guitar', 'butter','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee', 'ring', 'sun', 'bear','space','tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup']
# (1) 기본형 range() - 인덱스 중요하게
# range(n) : 0~n-1까지의 연속된 정수
# range(10)
# for i in range(len(unknown)):
#     print(unknown[i])


# (2) 리스트반복 
# for v in unknown:
#     print(v)

# # (3) 딕셔너리의 반복:
# for k, v in dict.items():
#     print(k,v)




# 행렬 공통수학1- 맨마지막 행렬단
 #열 
[["a",'b','c','d'],  #행
 [],
 [],
 [],
 [],
 []]

# 2차원리스트는 반복을 이중for문



##############################3
# 반복 while문


# while 조건:
#     조건이 만족할때, 반복할 코드

# 반복카운트를 세기
# 문제 카운트가 10전까지만 반복
# - count<10작으면 반복


# while문사용시 주의사항
# - 조건이 무조건 적인 True가 되면 안됩니다.
# - 무한루프에 빠지게된다. - 다른 동작 불가능, 리소스 굉장히 많이 쓴다.
count = 0
while count < 10:
    print(count)
    # 반복문이 빠져나갈 코드를 반드시 적어야한다.
    count+=1


count = 0
while True:
    # 반복문이 빠져나갈 코드를 반드시 적어야한다.
    print(count)
    count+=1
    # 만약에 내가 count 500이상이라면 그만 반복하게하기
    # break : 중간에 반복문을 탈출하는 코드(for문도, while문)
    if count >= 500:
        break

unknown = ['oak', 'guitar', 'butter','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee', 'ring', 'sun', 'bear','space','tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup']
#반복 돌려보면서
#중간에 seed 나오면 반복문 멈춰주기

# 건너뛰기 continue : 컨티뉴 기준 아래에 있는 코드는 실행하지않고 다음 반복으로 넘어간다.
for i in range(len(unknown)):
    
    # if unknown[i] == "seed":
    #     break

    # i가 짝수이면 continue 하자
    print("---")
    if i % 2 == 0:
        continue     
    print(i, unknown[i])
    print("야호")
    


# 과제1) https://www.acmicpc.net/problem/2083
# 과제2) https://www.acmicpc.net/problem/2884