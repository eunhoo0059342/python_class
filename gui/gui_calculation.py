# UI(User Interface)
# 

# 파이썬 응용소프트웨어로 빼는방법
# pip install pyinstaller
'''
과제) 버튼 배치 다 하고 올것!
------------------
              숫자       <-Entry
------------------
[7][8][9][/]            <-Button
[4][5][6][*]
[1][2][3][-]
[AC][0][=][+]

'''
import tkinter as t

# tk를 사용해서 윈도우 창을 만들기

w= t.Tk()
# w.resizable(false,false)
w.geometry('163x235')
w.resizable(False, False)


fontstyle = ('Footlight MT', 13, 'bold')
# jusify="left/center/right" : 정렬
e = t.Entry(w, justify='right')
# 제일 윗줄에 맨앞에서 4칸 차지 하기
# 위젯이름.grid(row=행번호, column=열번호, columnspan=차지할칸수)
e.grid(row = 0, column = 0, columnspan = 4,ipady=10, ipadx=10)

# 함수연결 내용 => print("click")

# 그리드시스템(Grid System)


# def button2():
#     x = lambda: 1+2  # 매개변수 없을때
#     y = lambda x: x+2 #매개변수 있을때,
#     print(x())
#     print(y(3),5)
#     print('click')

# 행과 열은 0번부터 시작
# 위젯이름.grid(row=행번호, column=열번호, columnspan=차지할칸수)
# 스타일 옵션, 폰트 : 시작메뉴 글꼴 검색
# 1. font = ('폰트이름',사이즈,bold/italic/underline)
# => 변수

# 2. 사이즈 
# - width=가로 길이 , height=세로길이
# - padx=내부가로여백, pady= 내부세로여백


# lambda 함수 : 

# lambda : 표현식

# def 함수이름():
#     return 


def button(num):
    # print(num)
    e.insert(t.END, num)

def clear():
    # 삭제 : delete(시작순서,끝순서)
    print('clear')
    e.delete(0, t.END)

def calculate():
    # print("계산함수")
    # eval("문자열수식") : 문자열로 된 수식을 계산해주느 함수
    # 엔트리에서 가져오기 : 엔트리이름.get() : 한줄 전체를 다 가져옵니다. / Text위젯 : 여러줄이여서 .get(순서)
    cal_num = e.get()
    # TODO : 전체 내용 삭제 후 추가
    clear()
    e.insert(t.END,str(eval(cal_num)))



# command lambda : button함수에 (1)를 넣어서 실행시켜주기
# button 함수 : 엔트리 넣어주는 역할
seven_b = t.Button(w, text='7', command=lambda: button(7), font=fontstyle, padx=9, pady=9)
seven_b.grid(row=1, column=0)

eight_b = t.Button(w, text='8', command=lambda: button(8), font=fontstyle,padx=9, pady=9)
eight_b.grid(row=1, column=1)

nine_b = t.Button(w, text='9', command=lambda:button(9), font=fontstyle,padx=9, pady=9)
nine_b.grid(row=1, column=2)

slash_b = t.Button(w, text='/', command=lambda: button('/'), font=fontstyle,padx=10, pady=9)
slash_b.grid(row=1, column=3)

four_b = t.Button(w, text='4', command=lambda: button(4), font=fontstyle, padx=9, pady=9)
four_b.grid(row=2, column=0)

five_b = t.Button(w, text='5', command=lambda: button(5), font=fontstyle,padx=9, pady=9)
five_b.grid(row=2, column=1)

six_b = t.Button(w, text='6', command=lambda:button(6), font=fontstyle,padx=9, pady=9)
six_b.grid(row=2, column=2)

star_b = t.Button(w, text='*', command=lambda: button('*'), font=fontstyle,padx=9, pady=9)
star_b.grid(row=2, column=3)

one_b = t.Button(w, text='1', command=lambda: button(1), font=fontstyle, padx=9, pady=9)
one_b.grid(row=3, column=0)

two_b = t.Button(w, text='2', command=lambda: button(2), font=fontstyle,padx=9, pady=9)
two_b.grid(row=3, column=1)

three_b = t.Button(w, text='3', command=lambda:button(3), font=fontstyle,padx=9, pady=9)
three_b.grid(row=3, column=2)

minus_b = t.Button(w, text='-', command=lambda: button('-'), font=fontstyle,padx=10, pady=9)
minus_b.grid(row=3, column=3)

clear_b = t.Button(w, text='AC', command=lambda: clear(), font=fontstyle, padx=2, pady=9)
clear_b.grid(row=4, column=0)

zero_b = t.Button(w, text='0', command=lambda: button(0), font=fontstyle,padx=9, pady=9)
zero_b.grid(row=4, column=1)

# 계산하는 함수연결해주세요.
equal_b = t.Button(w, text='=', command=lambda:calculate(), font=fontstyle,padx=9, pady=9)
equal_b.grid(row=4, column=2)

plus_b = t.Button(w, text='+', command=lambda: button('+'), font=fontstyle,padx=8, pady=9)
plus_b.grid(row=4, column=3)

w.mainloop()