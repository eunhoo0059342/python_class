import os
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model
from keras.layers import Dense
import tkinter as tk
from tkinter import ttk, messagebox

# ===== 1. 학습용 CSV 준비 =====
csv_path = "blackjack_training_data.csv"

if not os.path.exists(csv_path):
    # Kaggle CSV를 이미 다운로드했다고 가정
    raw_csv = "blackjack.csv"  # 다운로드한 CSV
    if not os.path.exists(raw_csv):
        raise FileNotFoundError("원본 CSV 파일이 필요합니다: blackjack.csv")
    
    df = pd.read_csv(raw_csv)
    
    # 3판 기록 -> 4번째 판 예측용 데이터 생성
    records = []
    for i in range(len(df)-3):
        prev1 = df.iloc[i]['player_sum']
        prev2 = df.iloc[i+1]['player_sum']
        prev3 = df.iloc[i+2]['player_sum']
        next_sum = df.iloc[i+3]['player_sum']
        dealer_card = df.iloc[i+2]['dealer_card']
        has_ace = df.iloc[i+2]['has_ace']
        style_id = df.iloc[i+2].get('style_id',0)
        records.append([style_id, prev1, prev2, prev3, dealer_card, has_ace, next_sum])
    
    df_train = pd.DataFrame(records, columns=['style_id','prev1','prev2','prev3','dealer_card','has_ace','next_sum'])
    df_train.to_csv(csv_path, index=False)
else:
    df_train = pd.read_csv(csv_path)

# ===== 2. 모델 학습 =====
model_path_h5 = "blackjack_model.h5"

if not os.path.exists(model_path_h5):
    X = df_train[['style_id','prev1','prev2','prev3','dealer_card','has_ace']].values
    y = df_train['next_sum'].values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    model = Sequential([
        Dense(64, activation='relu', input_dim=X_train.shape[1]),
        Dense(64, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)
    
    model.save(model_path_h5)
else:
    model = load_model(model_path_h5)
    scaler = StandardScaler()
    X = df_train[['style_id','prev1','prev2','prev3','dealer_card','has_ace']].values
    scaler.fit(X)

# ===== 3. 카드 관련 함수 =====
def create_deck():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    random.shuffle(cards)
    return cards

def calculate_hand(hand):
    total = sum(hand)
    if 1 in hand and total + 10 <= 21:
        total += 10
    return total

# ===== 4. GUI =====
class BlackjackApp:
    def __init__(self, root):
        self.root = root
        root.title("블랙잭 3판 + 4번째 판 예측 게임")
        root.geometry("500x400")
        self.show_start_screen()
    
    def show_start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        start_label = ttk.Label(self.root, text="블랙잭 예측 게임", font=("Arial", 16))
        start_label.pack(pady=50)
        start_button = ttk.Button(self.root, text="게임 시작", command=self.start_game)
        start_button.pack()
    
    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.deck = create_deck()
        self.round_num = 1
        self.player_hand = []
        self.dealer_hand = []
        self.player_history = []
        self.style_id = 0
        self.dealer_card = 10
        self.has_ace = 0
        
        self.info_label = ttk.Label(self.root, text=f"=== {self.round_num}판 ===")
        self.info_label.pack(pady=10)
        
        self.hand_label = ttk.Label(self.root, text="카드: [] 합계: 0")
        self.hand_label.pack()
        
        self.dealer_label = ttk.Label(self.root, text="딜러 오픈 카드: ?")
        self.dealer_label.pack()
        
        self.hit_button = ttk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.stand_button = ttk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)
        
        self.next_guess_label = ttk.Label(self.root, text="")
        self.next_guess_entry = ttk.Entry(self.root, width=10)
        self.guess_button = ttk.Button(self.root, text="맞추기", command=self.check_guess)
        
        self.start_round()
    
    def start_round(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.update_labels()
    
    def update_labels(self):
        self.hand_label.config(text=f"플레이어 카드: {self.player_hand}, 합계: {calculate_hand(self.player_hand)}")
        self.dealer_label.config(text=f"딜러 오픈 카드: {self.dealer_hand[0]}")
    
    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.update_labels()
        if calculate_hand(self.player_hand) > 21:
            self.end_round()
    
    def stand(self):
        self.end_round()
    
    def end_round(self):
        player_sum = calculate_hand(self.player_hand)
        self.player_history.append(player_sum)
        
        while calculate_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        dealer_sum = calculate_hand(self.dealer_hand)
        
        if player_sum > 21:
            result = "Lose"
        elif dealer_sum > 21 or player_sum > dealer_sum:
            result = "Win"
        elif player_sum < dealer_sum:
            result = "Lose"
        else:
            result = "Draw"
        
        self.result_label.config(text=f"{self.round_num}판 종료! 플레이어 합계: {player_sum}, 딜러 합계: {dealer_sum}, 결과: {result}")
        
        if self.round_num < 3:
            self.round_num += 1
            self.info_label.config(text=f"=== {self.round_num}판 ===")
            self.start_round()
        else:
            self.info_label.config(text="3판 완료! 4번째 판 점수를 맞춰보세요.")
            self.hit_button.pack_forget()
            self.stand_button.pack_forget()
            self.next_guess_label.config(text="4번째 판 점수 예측:")
            self.next_guess_label.pack()
            self.next_guess_entry.pack()
            self.guess_button.pack(pady=10)
    
    def check_guess(self):
        try:
            guess = int(self.next_guess_entry.get())
        except:
            messagebox.showerror("오류", "정수를 입력하세요.")
            return
        
        input_features = np.array([[self.style_id] + self.player_history + [self.dealer_card, self.has_ace]])
        input_scaled = scaler.transform(input_features)
        predicted_sum = model.predict(input_scaled)[0][0]
        predicted_sum_rounded = round(predicted_sum)
        
        correct = guess == predicted_sum_rounded
        messagebox.showinfo("결과", f"모델 예측값: {predicted_sum_rounded}\n맞췄나요? {correct}")
        
        self.show_start_screen()

# ===== 5. 실행 =====
root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()
