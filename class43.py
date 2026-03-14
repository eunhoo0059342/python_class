# 스택(Stack) - LIFO 
# 큐(Queue) - FIFO
# - 0번째부터 처리하는 방식은 성능이 좋지느 않습니다.
# - collection deque

#data
text = "1"
# text가 알파벳인가요? 맞으면 true 아니면 False
# text가 숫자인가요? isdigit
print(text.isalpha())
if text.isalpha() == True:
    print(True)
else:
    print(False)

if text.isdigit() == True:
    print(True)
else:
    print(False)

# 화학식
# C*3 H*5 (NO3)*3 -> N*3 O*9개
# 원자랑 갯수를 구분하는 방법 : 각 요소가 알파벳이면 원자 / 숫자이면 갯수
nitroglycerin = ['C', '3', 'H', '5', '(', 'N', 'O', '3', ')', '3']

# 각 원자당 질량
periodic_table = {'H': 1, 'C': 12, 'N': 14, 'O': 16, 'Na': 23, 'Mg': 24, 'S': 32, 'Cl': 35, 'Ca': 40, 'Fe': 56, 'Cu': 64, 'Ag': 108, 'I': 127, 'Pb': 207, 'He': 4}

# (1)nitroglycerin 요소를 하나씩 꺼내보자
# (2)영어 -> 원자 -> 각 원자당 질량
# (3)숫자 -> 앞에 원자가 있으면 -> 그 원자당 질량에 곱하기
# (4)'(' -> ')'나올때까지 기다려야한다. -> 괄호안의 화학식은 따로 데이터를 저장해줘야합니다.

# 총 원자의 질량

# mass: 원자의 질량 계산(
mass = 0
open_check = False
sum_mass = 0
mass_lst = 0

for i in range(len(nitroglycerin)):
    if nitroglycerin[i].isalpha() == True:
        # print(nitroglycerin[i])
        if open_check == False:
            sum_mass += mass
        else:
            mass_lst += mass
        mass = periodic_table[nitroglycerin[i]]
        # print(nitroglycerin[i])
    elif nitroglycerin[i].isdigit() == True:
        # print(nitroglycerin[i])
        mass = mass * int(nitroglycerin[i])
    else:
        if nitroglycerin[i] == '(':
            sum_mass += mass
            mass=0
            open_check=True
        elif nitroglycerin[i] == ")":
            # 괄호 안의 값 Mass_list 
            mass_lst += mass
            mass = mass_lst

sum_mass += mass
print(sum_mass)


