# 딕셔너리타입 key-value
# key기준으로  딕셔너리를 정렬하기

# => 리스트에 대한 정렬
# 리스트.sort() : 원본자체를 바꾸기 => 리스트에서만 사용이 가능하다.
# ** sorted(리스트, 튜플, 딕셔너리) : 원본을 정렬한 새로운 데이터를 반환
# - 내림차순정렬 sorted(데이터,reverse=True )
arr = [10,5,3,7,9,1]
print(sorted(arr,reverse=True))




slides = {7:'catch criminals,',
          1:'Dear',
          14:'is best',
          3:'I made',
          4:'project MONA',
          6:'our country,',8:'and find the',10:'other countries',11:'— so please',13:'Think about what',15:'for this country.',18:'Idle.',16:'Sincerely,',17:'Dr.',2:'President:',9:'spies from',12:'let me continue.',5:'to protect'}

# 기본적으로 key 정렬이된다.
print(sorted(slides.items()))
# 딕셔너리는 리스트로 사용하게될때 key값만 나오게된다.
# 딕셔너리.keys()
# 딕셔너리.value()
# 딕셔너리.items() => key-value가 튜플형태가 된다. => 정렬이 가능하다.

# 정렬한 딕셔너리를 쭉 이어서 value값 이어주세요!
sorted_slides = sorted(slides.items())
answer = []
answer2 = ''
for i in range(len(sorted_slides)):
    # print(sorted_slides[i][1])
    answer.append(sorted_slides[i][1])
    answer2 += sorted_slides[i][1]+" "
print(' '.join(answer))
print(answer2)


# 이차원리스트의 탐색
alpha = [
    ['a','b','c'], #행
    ['d','e','f'],
    ['g','h','i'],
]

i = 0
j = 1
# i행 j열 => b
# b를 기준으로 양옆에 위아래
# (1) 왼쪽 j-1 이동
# (2) 오른쪽 j+1 이동
# (3) 위 i-1 이동
# (3) 아래 i+1 이동







# 과제)
# 수 정렬하기 https://www.acmicpc.net/problem/2750
# 세수 https://www.acmicpc.net/problem/10817 
# 중복빼고 정렬하기 https://www.acmicpc.net/problem/10867