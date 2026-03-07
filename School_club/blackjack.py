import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def rank_value(rank):
    if rank == "A":
        return 11
    if rank in ["J","Q","K"]:
        return 10
    return int(rank)

class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        for _ in range(num_decks):
            for r in RANKS:
                self.cards.extend([r]*4)
        random.shuffle(self.cards)
    def draw(self, n=1):
        drawn = []
        for _ in range(n):
            if not self.cards:
                raise RuntimeError("덱이 비었습니다.")
            drawn.append(self.cards.pop())
        return drawn
    def remaining(self):
        return len(self.cards)

def hand_score(hand):
    total = sum(rank_value(r) for r in hand)
    aces = hand.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def logistic(x, alpha, beta):
    return 1 / (1 + math.exp(-(alpha + beta * x)))

def reward_distribution(score):
    if score > 21:
        return {"참가상": 1.0}
    p_s = logistic(score, alpha=-15, beta=0.7)
    p_a = logistic(score, alpha=-12, beta=0.5) - p_s
    p_b = logistic(score, alpha=-9, beta=0.4) - p_a
    p_c = max(0.0, 1 - (p_s + p_a + p_b))
    return {
        "1등급": max(0.0, min(1.0, p_s)),
        "2등급": max(0.0, min(1.0, p_a)),
        "3등급": max(0.0, min(1.0, p_b)),
        "4등급": max(0.0, min(1.0, p_c)),
    }

def choose_reward(score):
    dist = reward_distribution(score)
    rewards = list(dist.keys())
    probs = list(dist.values())
    return random.choices(rewards, weights=probs, k=1)[0]

# ===== GUI 클래스 =====
class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        root.title("블랙잭 게임")
        root.geometry("600x400")
        
        self.max_games = 3
        self.count = 0
        
        self.deck = Deck(num_decks=1)
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        
        # 화면 구성
        self.info_label = ttk.Label(root, text="")
        self.info_label.pack(pady=10)
        
        self.player_label = ttk.Label(root, text="")
        self.player_label.pack()
        
        self.dealer_label = ttk.Label(root, text="")
        self.dealer_label.pack()
        
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.hit_button = ttk.Button(root, text="Hit", command=self.hit)
        self.stand_button = ttk.Button(root, text="Stand", command=self.stand)
        self.reward_button = ttk.Button(root, text="상품 뽑기", command=self.pick_reward)
        
        self.start_button = ttk.Button(root, text="게임 시작", command=self.start_game)
        self.start_button.pack(pady=20)
        
    def start_game(self):
        self.start_button.pack_forget()
        self.count += 1
        if self.count > self.max_games:
            messagebox.showinfo("게임 종료", f"총 {self.max_games}경기 플레이 후 종료합니다.")
            self.root.destroy()
            return
        
        if self.deck.remaining() < 10:
            self.deck = Deck(num_decks=1)  # 덱 부족하면 새 덱 생성
        
        self.info_label.config(text=f"게임 {self.count} 시작 (남은 카드: {self.deck.remaining()})")
        self.player_hand = self.deck.draw(2)
        self.dealer_hand = self.deck.draw(2)
        self.player_score = hand_score(self.player_hand)
        self.dealer_score = hand_score(self.dealer_hand)
        self.update_labels()
        
        self.hit_button.pack(side=tk.LEFT, padx=20, pady=10)
        self.stand_button.pack(side=tk.RIGHT, padx=20, pady=10)
    
    def update_labels(self):
        self.player_label.config(text=f"플레이어 카드: {self.player_hand} (합계: {self.player_score})")
        self.dealer_label.config(text=f"딜러 카드 중 한 장: {self.dealer_hand[0]}")
    
    def hit(self):
        self.player_hand += self.deck.draw(1)
        self.player_score = hand_score(self.player_hand)
        self.update_labels()
        if self.player_score > 21:
            messagebox.showinfo("버스트!", "버스트! 짐")
            self.end_round()
    
    def stand(self):
        while hand_score(self.dealer_hand) < 17:
            self.dealer_hand += self.deck.draw(1)
        self.dealer_score = hand_score(self.dealer_hand)
        self.end_round()
    
    def end_round(self):
        self.hit_button.pack_forget()
        self.stand_button.pack_forget()
        
        def winner(ms, ds):
            if ms > 21:
                return "짐"
            if ds > 21 or ms > ds:
                return "이김"
            if ms == ds:
                return "비김"
            return "짐"
        
        result = winner(self.player_score, self.dealer_score)
        self.result_label.config(text=f"결과: {result}\n딜러 최종 카드: {self.dealer_hand} 합계: {self.dealer_score}")
        
        # 상품 버튼 표시
        self.reward_button.pack(pady=10)
    
    def pick_reward(self):
        reward = choose_reward(self.player_score)
        dist = reward_distribution(self.player_score)
        dist_str = "\n".join([f"{k}: {v*100:.1f}%" for k,v in dist.items()])
        messagebox.showinfo("상품 결과", f"상품 확률:\n{dist_str}\n\n당신이 받은 상품: {reward}")
        self.reward_button.pack_forget()
        self.start_button.pack(pady=20)
        self.result_label.config(text="")
        self.player_label.config(text="")
        self.dealer_label.config(text="")
        self.info_label.config(text=f"게임 {self.count}/{self.max_games} 완료")

# ===== 실행 =====
if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
