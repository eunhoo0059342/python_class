import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import os
from keras.models import load_model
import pickle
from sklearn.preprocessing import StandardScaler

# --- 모델 및 스케일러 경로 ---
MODEL_PATH = "blackjack_model.h5"
SCALER_PATH = "scaler.pkl"

# --- 모델 불러오기 ---
if not os.path.exists(MODEL_PATH):
    messagebox.showerror("파일 오류", f"{MODEL_PATH} 파일이 없습니다. 학습된 모델을 준비하세요.")
    raise FileNotFoundError(f"{MODEL_PATH} 없음")

model = load_model(MODEL_PATH, compile=False)

# --- 스케일러 불러오기 또는 생성 ---
if os.path.exists(SCALER_PATH):
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
else:
    # 스케일러 자동 생성 (간단 예시: 3차원 입력 기준)
    scaler = StandardScaler()
    dummy_data = np.zeros((1,3))  # 플레이어 3판 입력은 3개 특성
    scaler.fit(dummy_data)
    with open(SCALER_PATH, "wb") as f:
        pickle.dump(scaler, f)
    messagebox.showinfo("스케일러 생성", f"{SCALER_PATH} 파일을 새로 생성했습니다.")

# --- 전역 변수 ---
game_count = 0
MAX_GAMES = 3
player_history = []

# --- 창 전환 함수 ---
def switch_frame(current_frame, next_frame):
    current_frame.pack_forget()
    next_frame.pack(fill="both", expand=True)

# --- 1. 시작 창 ---
root = tk.Tk()
root.title("블랙잭 예측 게임")
root.geometry("800x600")

start_frame = ttk.Frame(root)
start_frame.pack(fill="both", expand=True)

ttk.Label(start_frame, text="블랙잭 예측 게임", font=("Arial", 24)).pack(pady=100)
start_btn = ttk.Button(start_frame, text="시작", command=lambda: switch_frame(start_frame, game_frame))
start_btn.pack()

# --- 2. 게임 창 ---
game_frame = ttk.Frame(root)
ttk.Label(game_frame, text="게임 진행 중", font=("Arial", 20)).pack(pady=20)

player_sum_var = tk.StringVar()
dealer_card_var = tk.StringVar()
has_ace_var = tk.StringVar()
result_var = tk.StringVar()

ttk.Label(game_frame, text="플레이어 카드 합:").pack()
ttk.Entry(game_frame, textvariable=player_sum_var).pack()

ttk.Label(game_frame, text="딜러 카드 합:").pack()
ttk.Entry(game_frame, textvariable=dealer_card_var).pack()

ttk.Label(game_frame, text="플레이어 에이스 유무 (0 or 1):").pack()
ttk.Entry(game_frame, textvariable=has_ace_var).pack()

ttk.Label(game_frame, textvariable=result_var, font=("Arial", 16)).pack(pady=20)

def submit_game():
    global game_count
    try:
        player_sum = float(player_sum_var.get())
        dealer_card = float(dealer_card_var.get())
        has_ace = float(has_ace_var.get())
    except ValueError:
        messagebox.showerror("입력 오류", "숫자를 정확히 입력하세요")
        return
    
    player_history.append([player_sum, dealer_card, has_ace])
    result_var.set(f"판 {game_count+1} 기록 완료")
    
    game_count += 1
    if game_count >= MAX_GAMES:
        switch_frame(game_frame, predict_frame)

ttk.Button(game_frame, text="입력 완료", command=submit_game).pack(pady=20)

# --- 3. 플레이어 예측 창 ---
predict_frame = ttk.Frame(root)
ttk.Label(predict_frame, text="다음 판 카드 합을 예측하세요", font=("Arial", 20)).pack(pady=50)
predict_var = tk.StringVar()
ttk.Entry(predict_frame, textvariable=predict_var).pack()

def submit_prediction():
    try:
        player_pred = float(predict_var.get())
    except ValueError:
        messagebox.showerror("입력 오류", "숫자를 정확히 입력하세요")
        return
    
    last_three = np.array(player_history[-3:])
    X_input = last_three[-1].reshape(1, -1)
    X_scaled = scaler.transform(X_input)
    ai_pred = model.predict(X_scaled)[0][0]
    
    ai_result_var.set(f"AI 예측 카드 합: {ai_pred:.1f}\n플레이어 입력: {player_pred}")
    switch_frame(predict_frame, compare_frame)

ttk.Button(predict_frame, text="확인", command=submit_prediction).pack(pady=20)

# --- 4. AI 예측 비교 창 ---
compare_frame = ttk.Frame(root)
ai_result_var = tk.StringVar()
ttk.Label(compare_frame, textvariable=ai_result_var, font=("Arial", 16)).pack(pady=50)

ttk.Button(compare_frame, text="다음", command=lambda: switch_frame(compare_frame, reward_frame)).pack()

# --- 5. 뽑기 창 ---
reward_frame = ttk.Frame(root)
ttk.Label(reward_frame, text="뽑기 결과", font=("Arial", 20)).pack(pady=50)

def draw_reward():
    import random
    rewards = ["1등급", "2등급", "3등급", "4등급"]
    probs = [0.1, 0.2, 0.3, 0.4]
    prize = random.choices(rewards, weights=probs, k=1)[0]
    messagebox.showinfo("당첨", f"당신이 받은 상품: {prize}")
    # 초기화 후 시작 창으로
    global game_count, player_history
    game_count = 0
    player_history = []
    switch_frame(reward_frame, start_frame)

ttk.Button(reward_frame, text="뽑기", command=draw_reward).pack(pady=20)

root.mainloop()
