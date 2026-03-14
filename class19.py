# <함수로 풀어보기>
# 기능 : 
# 입력 :
# 출력 : 


# 트랜스포지션 암호화
# abcdefg
# yzabcde

# apple
# ynnjc


# 원본 ---암호화---> 암호
#     <--복호화(해독)----
print("mission 1==========")
# 2칸씩 밀어서 암호화 한다.
# 복호화(해독) -2칸씩 움지여한다.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word1 = ['o','q','q','p','r','a']
# 답 : m o o n p y
# 2칸씩 밀수있도록 하는 함수
# 입력 : 몇칸 밀지, 바뀐 암호
def word(num, password):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a = ''
    for i in range(len(password)):
        # print(password[i])
        for j in range(len(alphabet)):
            if alphabet[j] == password[i]:
                a += alphabet[j - num]
    return a



print(word(2, word1))


print("mission 2==========") 
# 8칸 밀어보기 
word2 = ['q','u','q','b','i','b','q','w','v']
print(word(8, word2))




