#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?A45CC6E7BF09DCE96C547E163E737D4872E0
# https://solved.ac/profile/eunhoo345427

# 2진수로 표현하려면?
0b0001111000   
# 오른쪽 2진수 => 10진수로 바꾼 값이 될것120
# 보통은 2진수 문자열로 표현이 된다.
# 문자열로 된 2진수로 10진수로 바꾸려면 어떻게 해야할까? 
# int("2진수문자열",2)

# 2진수 0b
# 16진 Hex 0x7a   => int("16진수문자열",16)
print(int("0b0001111000", 2))
print(int("0b1001111001",2))

print("mission 2======================")

num_list = [0b1011110000001111, 
            0b1010010000001001, 
            0b1010010111101001, 
            0b1011110100101001, 
            0b1010010111101001, 
            0b1010010100001001, 
            0b1011110111101111]


# bin(숫자) : 2진수형태의 문자열을 만들어주는 함수


# "1" => "#" "0"=> " " 그외 => "" 빈문자열을 출력한다.
# 문자열을 반복돌리면 문자가 하나씩 나온다. 


# print() 옵션을 알아보자
# print("내용",end='')
for i in range(len(num_list)):
    #print(bin(num_list[i]), "문자열") # "0b1011110000001111"
    bin_text = bin(num_list[i])
    for j in range(len(bin_text)):
        #print(bin_text[j])
        if bin_text[j] == "1":
            print("#", end='')
        elif bin_text[j] == "0":
            print(" ",end='')
        else:
            print("",end='')
    #줄바꿈 하기 \n
    print("\n",end='')

print("mission 3 ==============")

paragraph = 'We are a form of warfare. We aim to achieve maximum consequential impact for where   asymmetric happens. We attack where finite input allocation of resources   exists. objectives should be clearly defined and work norms and means adopted by the organization are acceptable to the individual and groups. Each Person   is responsible for completing   the work. Organisation will appoint the job should be done. should be set up in such a way that every individual should be assigned a duty according to his skill and qualification. The person should   continue the same work so that he specialises in his work. This helps in increasing production in the concern. The scope of authority and responsibility   should be clearly defined.   Every person should know his work with definiteness. If the duties are not clearly assigned.  then it will not be possible to fix responsibility also. Everybody’s responsibility will become nobody’s responsibility. The principle states that top management should interfere only when something goes wrong.   If the things are done as per plans then there is no need for the interference of top management.   The management should leave routine things to be supervised by lower cadres.   It is only in exceptional situations when attention of   top easy management is drawn.  The principle   relieves top management of many botherations and routine things. Principle of exception allows top   management to concentrate on planning game and policy formulation.   Important time of management is not   wasted on avoidable supervision. The responsibility of the superior does not decrease once he has delegated authority. A person   can delegate authority and not responsibility. We will remain for the work even if it is de legated to the subordinate accountable work. So the responsibility of superior and subordinate remains absolute.'
missing   = 'We are a form of warfare. We aim to achieve maximum consequential impact for where   as-mmetric happens. We attack where finite input all-cation of reso-rces - exists. objectives s-ould be cle-rly defined and work norms and means adopted by the organization are acceptable to the indi-idual and groups. Each P-rson - is responsi-l- for compl-ti-g - the work. Organisation will appoint the job shoul- be d-ne. should be set up in such a way that every individual should be assigned a duty accord--- to his skill and qualification. The person should - continue the same -ork so that h- specialises in his work. This he-ps in increasing production in the concern. The scope of authority and responsibi-ity - -h-uld be clearly defined. - Every person should know his work with de-initeness. If the duties --e not clearly assigned-- then it will not -e possible to fix responsibility also. Everybody’s responsibility will become nobody’s responsibility. The principle states that top management sho-ld in-erfere only when something goes wrong. - If the things are done as per plans then there -s no need for -he interference of top management. - The management should leave routine things to be supervised by lo-er c-dre-. - It is only in excep-i-nal situations when attenti-n of - top ---- management is drawn- ---- principle - --lieves top man-gement of many botherations and routine things. Princip-e of exception allows top - management to concentrate on planning ---- and policy formulation. - Important time of management -- not - --sted on avo-dable supervision. The responsibility of -he super-or does -ot decrease once he has dele-ated authority- A person - can dele-ate authority and n-t resp-nsibility. We will remain for the work even if it is -e--egated to the s-bordinate a-countable wor-. So the responsibility of superior and subordinate remains absolute-'

# 두 변수의 길이를 비교해보자

print(len(paragraph))
print(len(missing))
answer = []
for i in range(len(paragraph)):
    #print(paragraph[i])
    #print(missing[i])
    if paragraph[i] != missing[i]:
        answer.append(paragraph[i])
print(''.join(answer))

# 문자열 => 리스트로 바꾸기 : 문자열변수.split('구분인자) 나눈다.
# 리스트 => 문자열로 바꾸고싶네 : '구분인자'.join(리스트변수)    합치다.
#- 보통은 "".join(리스트이름)




# 백준 연슴
# - 두 수 비교하기 - https://www.acmicpc.net/problem/1330
# - 별 찍기 - 1 https://www.acmicpc.net/problem/2438
# - 구구단 https://www.acmicpc.net/problem/2739