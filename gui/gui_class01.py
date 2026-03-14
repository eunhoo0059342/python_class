'''
tkinter 모듈로 GUI 만들기
'''

# (1) tkinter 모듈 삽입 
# 모듈에 별칭정하기
# import 모듈이름 as 별칭 tk

import tkinter as tk

import random
# (2)tk를 사용해서 윈도우 창을 만들기
# - 윈도우이름(w,window, root)= tk.Tk()
# - 윈도우 크기 설정 : 윈도우이름.geometry("가로사이즈x세로사이트+x위치+y위치")
w = tk.Tk()
w.geometry('300x600')


# ——————————— 2. 위젯(UI) ———————————
# (1) Label 문자를 나오게하는 위젯
# 라벨이름 = tk.Label(윈도우이름, text="내용")
# 라벨이름.pack()
l = tk.Label(w, text='hello World')
l.pack()

# (2) Button 위젯
# 버튼이름 = tk.Button(윈도우이름, text="내용",command=함수이름)
def click():
    print("click")
    # 라벨 수정
    # 라벨이름.config(text="수정할 내용")
    l.config(text='hi')


b = tk.Button(w, text='button', command=click)
b.pack()

# 로또를 뽑아주는 새로운 버튼을 만들어보고 로또함수랑 연결해보세요~!
def lotto_num():
    num_lst = []
    while len(num_lst) < 6:
        num_lst.append(random.randrange(1, 46))
        num_lst = list(set(num_lst))
    l.config(text=sorted(num_lst))
    # 리스트박스에 내용추가 : 리스트박스.insert(삽입위치,추가할내용)
    # - 순서 : 맨위, 맨앞 0 / 맨뒤: tk.END
    box.insert(tk.END, sorted(num_lst))


lotto_b = tk.Button(w, text='lotto', command=lotto_num)
lotto_b.pack()

# (3) Listbox 위젯
# 박스이름 = tk.Listbox(윈도우이름)
box = tk.Listbox(w)
box.pack()

# (4) Entry위젯 : 한줄입력
# 엔트리이름 = tk.Entry(윈도우이름)
e = tk.Entry(w)
e.pack()
# - 위젯의 내용을 가져오기 버튼 만들기
def entry():
    # - 위젯의 내용을 가져오기 get / 설정 set
    # get(위치)
    # L 라벨에다가 가져온 내용으로 수정하기
    get_e = e.get()
    l.config(text=get_e)
bring_b = tk.Button(w, text='bring', command=entry)
bring_b.pack()


# (5) Text위젯
# 텍스트위젯이름 = tk.Text(윈도우이름,옵션)
# 옵션 : 사이즈 정하기 : width= 가로 길이(폰트사이즈), height=세로길이
t = tk.Text(w, width=20, height=20)
t.pack()

# 계산기





# * 윈도우를 계속해서 반복하면서 실행하도로 하기
# 윈도우이름.mainloop()
w.mainloop()






