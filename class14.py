'''
<데이터타입>
1. 숫자타입
2. 문자열타입
3. bool타입 T/F => 조건문 
4. 리스트타입 [요소,요소,요소]
5. 딕셔너리타입 {key:value}
6. 튜플타입 (요소,요소,요소)
7. 집합 {원소,원소,원소}  => set([원소,원소,원소])
'''

# 집합 (수학적으로) 1. 명확하게 기준을 갖은 
#       2. 서로 다른 원소들의 데이터의 모음
# (코딩) : 서로 다른 원소들 만 처리 중복데이터는 허용하지않는 데이터 모음
# - 집합에는 순서가 없습니다.

# 과목이름으로 집합을 만들어보기
subject = {"수학","과학","영어","국어","사회"}
print(subject)
subject2 = set(["수학","과학","영어","국어","사회"])
print(subject2)

print("mission 1 ============")
# a,b,c,d 모든 명단을 구하시오. 

# a와 b가 동시에 참여한 명단
a_b = ['oak', 'guitar', 'butter', 'clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','ring', 'sun', 'bear','space']
# b와 d가 동시에 참여한 명단
b_d = ['clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
# c와 d가 동시에 참여한 명단
c_d = ['boat', 'piano', 'seed', 'tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
d = ['boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
d = set(d)
b = set(b_d)-d
c = set(c_d)-d
a = set(a_b)-b

print(b)
print(c)
print(a)
print(d)
# 차집합 A-B
# A.difference(B) 
# A-B

print("mission 2===========")
# a가 b의 부분집합이냐?
a < b
a.issubset(b)
# unknown 명단에, a,b,c,d집중 어느 집합이 속해있는가?(=부분집합 관계)
unknown = ['oak', 'guitar', 'butter','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee', 'ring', 'sun', 'bear','space','tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup']
print(a.issubset(unknown))
print(b.issubset(unknown))
print(c.issubset(unknown))
print(d.issubset(unknown))

# a,c,d를 합집합 하면 unknown 같은가?
print((a|c|d) == set(unknown))
print(a|c|d)