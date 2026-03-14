# gui 깔끔한 버전의 tikinter사용
# https://customtkinter.tomschimansky.com/documentation/

# Installation
# pip install customtkinter
# import customtkinter as ctk
import customtkinter as ctk
from datetime import datetime
# (1) 윈도우 = ctk.CTk()
# 윈도우.geometry("가로x세로")
# 윈도우.title("프로그램제목")
# 윈도우.mainloop()  # 맨아래

window = ctk.CTk()
window.title("d-day program")
window.geometry("600x600")

# Ui참고사이트 https://superkts.com/cal/d_day/
'''
오늘 날짜 표시
게산할 날짜를 입력받게하기
[ ]년 []월 []일 
계산버튼
-------
계산한 내용들로 리스트 기록

'''
# https://customtkinter.tomschimansky.com/documentation/widgets/label
# 날짜 포
today_date = datetime.today()
# today_date.strftime("Y%년m%월d%일")

# font적용팁 - 튜플-변수화 ("폰트이름",사이즈,bold/itelic/underline)
# -font이름 Arial
window_font = ("Arial", 40)
label = ctk.CTkLabel(window, text=today_date.strftime("%Y년%m월%d일"), font=window_font, fg_color="transparent")
# 오늘의 날짜는 행6개를 합쳐보기 columnspan=합칠갯수
label.grid(row=0, column=0, columnspan=6)

# grid로 배치하기
# 위젯이름.grid(row="행번호(세로위치,0부터 시작)",column="열번호(가로위치,0부터시작)")
# 디데이 계산할 entry
# https://customtkinter.tomschimansky.com/documentation/widgets/entry
# 엔트리이름 = ctk.CTkEntry(윈도우명)

year = ctk.CTkLabel(window, text="년도", font=window_font, fg_color="transparent")
year.grid(row=1, column=0)
year_entry = ctk.CTkEntry(window)
year_entry.grid(row=1, column=1)

month = ctk.CTkLabel(window, text="월", font=window_font, fg_color="transparent")
month.grid(row=1, column=2)
month_entry = ctk.CTkEntry(window)
month_entry.grid(row=1, column=3)

day = ctk.CTkLabel(window, text="일", font=window_font, fg_color="transparent")
day.grid(row=1, column=4)
day_entry = ctk.CTkEntry(window)
day_entry.grid(row=1, column=5)


# 오늘날짜보다 미래이면 D-_남은일자__
# 오늘날짜보다 과거면 D+남은일짜--
# 오늘날짜랑 같으면 D-Day
def calculate(today_date):
    # 오늘날짜랑 엔트리에 넣은 값을 가져와서 비교하기
    # 엔트리이름.get()
    # if today_date:
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())

    # today_date : datetime객체
    # 비교해줄 날짜도 : datetime객체 만들어줘야한다.
    #=> datetime(년도,월,일)
    entry_date = datetime(year, month, day)
    
    # label 내용수정하기
    # label위젯이름.configure(text="변경할 내용")
    print(today_date.date(), entry_date.date())
    if today_date.date() > entry_date.date():
        result_label.configure(text=f"D+{(today_date- entry_date).days}")
    elif today_date.date() == entry_date.date():
        result_label.configure(text="D-DAY")
    else:
        result_label.configure(text=f"D-{(entry_date- today_date).days}")
    
# 버튼위젯 CTKButton
# https://customtkinter.tomschimansky.com/documentation/widgets/button
# 위젯이름 = ctk.CTkButton(윈도우명, text="버튼 글자",command=함수이름)
# lambda : 함수이름(매개변수)
button = ctk.CTkButton(window, text="계산하기", command=lambda : calculate(today_date))
button.grid(row=2, column=0, columnspan=6)
# ntry = ctk.CTkEntry(window)


# label 결과를 출력하기
result_label = ctk.CTkLabel(window, text="", font=window_font, fg_color="transparent")
result_label.grid(row=3, column=0, columnspan=6)

window.mainloop()