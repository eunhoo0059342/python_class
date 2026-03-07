import random
import math
import os
import sys
import time
import shutil
import json
from collections import Counter
from unittest import result

RED = "\033[31m"
LIGHT_GREEN = "\033[92m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
NORM = "\033[22m"
BOLD = "\033[1m" 

try: #밑에 해당하는 사항(들)을 시도한다
    from terminaltexteffects.effects.effect_slide import Slide #slide(옆에서부터 나오는 연출) 모듈 가져오기
    from terminaltexteffects.effects.effect_fireworks import Fireworks #Fireworks(폭죽연출) 가져오기
    from terminaltexteffects.effects.effect_rain import Rain #Rain(글자가 비처럼 내리는 연출) 가져오기
    TTE_AVAILABLE = True
except Exception: #작동하지 않은 반례(예외)
    Slide = None #Slide의 연출을 없앰
    Fireworks = None #Fireworks의 연출을 없앰
    Rain = None #Rain의 연출을 없앰
    TTE_AVAILABLE = False #연출이 작동하지 않으면 연출이 없는 상태로 출력하게 하는 try:except문

RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # 카드 숫자 및 문자

MAX_GAMES = 5


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_yes_no(prompt):
    while True:
        resp = input_clear(prompt)
        v = resp.strip().lower()
        if v in ('y','n'):
            return v
        print("잘못된 입력입니다. Y 또는 N을 입력해주세요.")

def input_clear(prompt): #15~19 yes or no 응답 입력 함수
    resp = monitored_input(prompt)
    if resp.strip().lower() in ('y', 'n'):
        clear()
    return resp

def monitored_input(prompt=""):
    try:
        while True:
            resp = input(prompt)
            if resp.strip().lower() == "l":
                sb.show_ranking()
                continue
            if resp.strip().lower() == "b":
                clear()
                return "b"
            return resp
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단되었습니다.")
        sys.exit(0)

def rank_value(rank): #카드의 랭크를 분류하는 함수
    if rank == "A": #만약 카드의 랭크가 A라면
        return 11 #원래는 1과 11을 선택해야하지만 일단 큰 수인 11로 함수에서 내보냄
    if rank in ["J","Q","K"]: #만약 카드의 랭크가 J, Q, K라면
        return 10 # 10으로 내보냄
    return int(rank) #아무것도 아닌 경우는 이미 숫자이기 때문에 정수로 만든 후 내보냄.

def hand_score(hand): # 손에 있는 점수의 총 점수를 보여주는 함수
    total = sum(rank_value(r) for r in hand) #손에 있는 카드의 rank_value를 전부 곱함 / 축약형 for문
    aces = hand.count("A") #hand에서 A를 카운트함
    while total > 21 and aces > 0: #만약 total이 21을 초과하며 aces가 1 이상이라면
        total -= 10 #total을 10 줄임 / A는 11과 1 모두 가능한데 현재 A는 11로 저장되어 있기 때문에 10을 빼서 1을 만듦
        aces -= 1 #aces를 1 줄임 / total의 수도 조건이지만 aces가 있을 때 while문의 무한반복을 없애기 위하여 aces를 하나 없앰
    return total #total을 내보냄

def logistic(x, alpha, beta): #현재 주제인 로지스틱 회귀 함수의 공식 / 짧지만 여러번 쓰기 버겁기 때문에 미리 짧은 이름의 함수로 만듦
    return 1 / (1 + math.exp(-(alpha + beta * x)))

def reward_distribution(score, result): #보상 분배(뽑기)에 대한 함수 / score와 result를 받음
    if result == "패배": #만약 result가 '패배'라면
        return {"참가상": 1.0} #더이상 밑으로 내려가지 않고 참가상 100%로 마무리

    logit_1 = 6 * logistic(score, alpha=-15, beta=0.65)
    logit_2 = 11.5 * logistic(score, alpha=-12, beta=0.45)
    logit_3 = 1.0 * (1 - logistic(score, alpha=-10, beta=0.5)) #127 ~ 129 : x에 score를 넣고 alpha와 beta를 주고 로지스틱 회귀의 값을 얻어 확률을 만들어 냄
    logit_4 = 1.0 #하고 남은 나머지 값

    logits = [logit_1, logit_2, logit_3, logit_4] #나온 확률을 리스트로 만들어 정리함
    exp_logits = [math.exp(x) for x in logits] #자연 상수 e에 logits만큼의 제곱을 함
    total = sum(exp_logits) #exo_logits를 모두 합침

    probs = [x / total for x in exp_logits] #반복 변수 x를 exp_logits에 대입함 

    return {
        "1 등급": probs[0],
        "2 등급": probs[1],
        "3 등급": probs[3],
        "4 등급": probs[2],
    } #probs 리스트의 각 값을 등급으로 나눠 함수에서 내보냄

class Deck: #카드덱에 대한 클래스
    def __init__(self, num_decks=1): #함수에서 num_deck을 1로 받음
        self.cards = [] #스스로의 카드(들)를 리스트로 저장하기 위해 빈 리스트 변수 저장
        for _ in range(num_decks): #반복변수 _ / num deck
            for r in RANKS: #for 반복문
                self.cards.extend([r]*4) #card 리스트에 반복변수 r을 네번 추가
        random.shuffle(self.cards) #self_cards 리스트에 있는 수를 임의로 섞음
    def draw(self, n=1): #함수에서 n = 1로 받음 / 카드를 뽑는 함수
        drawn = [] #뽑힌 카드를 넣는 리스트
        for _ in range(n): #반복 변수 _ / n만큼 반복하는 for문
            if not self.cards: #만약에 self.cards에 아무것도 없다면
                raise RuntimeError("덱이 비었습니다.") #RuntimeError로 제기되며 '덱이 비었습니다로 출력'
            drawn.append(self.cards.pop()) #self.cards에서 지운 값을 drawn 리스트에 추가함
        return drawn #drawn 리스트를 함수에서 내보냄
    def remaining(self): #남은 카드 수를 보여주는 함수/ 길진 않지만 자주 사용하기에 함수로 만듦
        return len(self.cards) #self.cards의 길이(남아있는 카드의 수)를 내보냄
    def counts(self): # 각각의 카드의 수를 보여주는 함수
        c = {r:0 for r in RANKS} #RANKS 리스트의 모든 값은 r로 대입 되어 {1:0, 2:0, 3:0, ...}형식의 딕셔너리가 저장됨
        for card in self.cards: # self.cards에 대한 반복문
            c[card] += 1 #딕셔너리 c의 card부분에 1을 더함
        return c #딕셔너리 c를 내보냄

class Display:
    def slow_print(self, text, delay=0.1, end="\n"):  # 21~27 천천히 연출에 맞춰 출력하게 하는 함수
        for ch in str(text):
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(end)
        sys.stdout.flush()
    
    def tte_slide_print(self, text): #왼쪽에서부터 하나씩 출력되는 연출을 작동하는 함수
        if not TTE_AVAILABLE or Slide is None: #아무것도 가지고 있지 않다면 그냥 돌려 보내기
            self.slow_print(text)
            return
        effect = Slide(text) #우선사항 확인 후 남은 문자열를 Slide 함수를 사용하여 연출하기
        effect.effect_config.merge = True 
        try:
            with effect.terminal_output() as term: #연출을 터미널에 출력하고 이름을 term으로 저장함
                for frame in effect:
                    term.print(frame)
        except Exception:
            self.slow_print(text) #작동하지 않는다면 slow_print함수로 보내기
    
    def tte_fireworks_reveal(self, text): #폭죽 연출을 만드는 함수
        if TTE_AVAILABLE and Fireworks is not None: 
            effect = Fireworks(text)
            effect.effect_config.merge = True #아무것도 가지고 있지 않으면 slow_print 함수로 보내기
            try: #밑에는 사항(들)을 시도함
                with effect.terminal_output() as term: #폭죽 연출을 터미널에 출력하고 이름을 term으로 저장함
                    for frame in effect: #for 반복문
                        term.print(frame) #반복하여 term의 연출을 출력함
                return #이미 출력을 했기 때문에 return을 굳이 사용하지 않음 
            except Exception: #시도했지만 실패한 반례(예외)(들)
                pass #그다지 중요하지 않으니 넘겨도 상관없기 때문에 넘김
        self.slow_print(text, delay=0.03) #slow_print 함수 사용
        confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE] #연출에 사용할 색 리스트
        for _ in range(3): # _ = 반복 변수 / 3번 반복함
            line = "" #line이란 변수 생성
            for _ in range(30): #반복 변수 _ / 30번 반복
                c = random.choice(confetti_colors) #c는 choice의 약자 / 색깔을 임의로 선택하여 저장함
                line += c + random.choice(["*", "✦", "✶", "✺"]) + RESET #line에 리스트 안에 있는 그림을 임의로 선택하여 추가 + 리셋
            print(line) #그렇게 만들어진 line을 하나씩 출력
            time.sleep(0.12) #0.12초를 멈춤
            
    def color_score(self, n): #score에 따라 달라지는 컬러값을 조정하는 함수 / n을 받음
        try: 
            n_int = int(n) #n을 정수로 만들기를 시도함
        except:
            return str(n) #되지 않는다면 문자열로 다시 변경 후 진행
        if n_int > 21: #만약에 정수 n이 21보다 크다면
            return f"{RED}{n_int}{RESET}" #컬러값을 빨간색으로 만든다
        if n_int == 21: #만약에 정수 n이 21과 같다면
            return f"{LIGHT_GREEN}{n_int}{RESET}" #컬러값을 초록색으로 변경한다
        return str(n_int) #변경한 정수 n을 문자열로 변경하고 내보낸다
        
    def _color_count_str(self, n):
        num = int(n)
        if num == 0:
            return "  "
        num_str = f"{num:>2}"
        if num >= 3:
            return f"{NORM}{num_str}{RESET}"
        if num == 2:
            return f"{NORM}{YELLOW}{num_str}{RESET}"
        return f"{NORM}{RED}{num_str}{RESET}"

    def display_counts_table(self, counts):
        print("─ 남은 카드 수 ─")
        sep = "   "
        row1 = sep.join(f"{r:<2} : {self._color_count_str(counts[r])}" for r in ["A","2","3","4"])
        row2 = sep.join(f"{r:<2} : {self._color_count_str(counts[r])}" for r in ["5","6","7","8"])
        row3 = sep.join(f"{r:<2} : {self._color_count_str(counts[r])}" for r in ["9","10","J","Q"])
        row4 = f"{'K':<2} : {self._color_count_str(counts['K'])}"
        print(row1)
        print(row2)
        print(row3)
        print(row4)

    def animate_prize_draw(self, dist): #보상을 뽑는 연출을 만드는 함수 / dist값을 받음
        items = list(dist.items()) 
        names = [k for k,_ in items]
        weights = [v for _,v in items]
        n = len(names) #163 ~ 166:자주 쓸 내용은 미리 짧은 변수로 만들어 놓기
        if n == 0: #만약에 n이 0이라면
            return None #None을 내보냄
        if sum(weights) == 0: #만약에 weights의 총 합이 0이라면
            weights = [1.0] * n #weights는 1.0만 가진 리스트를 n번동안 반복
        winner = random.choices(names, weights=weights, k=1)[0] #임의로 선택한 값을 저장 / 뽑힌 값
        winner_idx = names.index(winner) #winner(뽑힌 값)을 index로 내보냄
        spinner = ['|','/','-','\\'] #돌리 때 나올 연출을 리스트로 정리
        term_w = shutil.get_terminal_size((80, 20)).columns #터미널사이즈를 저장함
        if n <= 1: #만약에 n이 1보다 작거나 같다면
            reveal = f"{winner}!" #뽑힌 값을 뒤에 !와 함께 저장
            if TTE_AVAILABLE: #만약에 TTE_AVAILABLE이라면
                self.tte_fireworks_reveal(reveal) #reveal에 폭주효과를 넣음
            else: #아니라면
                self.slow_print(reveal, delay=0.1) #slow_print함수를 작동함
                confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE] #색깔 리스트
                for _ in range(3): # _: 반복 변수 / 총 3번 반복하는 for문
                    line = "".join(random.choice(confetti_colors) + random.choice(["*", "✦", "✶", "✺"]) + RESET for _ in range(30)) #임의의 색과 모양을 30번 넣은 줄을 저장
                    print(line) #저장한 줄을 출력
                    time.sleep(0.12) #0.12초 동안 잠시 멈춤
            return winner #winner를 내보냄
        cycles_needed = random.randint(4, 8) #4에서 8중에서 임의로 숫자를 정함
        initial_delay = 0.06 #초기 지연을 0.06으로 저장함
        final_delay = 0.30 #최종 지연을 0.30으로 저장함
        ease_power = 2.0 #2.0으로 저장함
        total_steps = cycles_needed * n + winner_idx #cycle_needed와 n을 곱하고 winner_idx를 더한 값을 저장함
        i = 0 #i를 0으로 저장함
        while True: #무한 반복 while문
            idx = i % n #i를 n으로 나누었을 때 나머지를 index로 저장함
            spin = spinner[i % len(spinner)] #i를 spinner의 길이로 나누고 남은 값을 spinner의 index값으로 나온 값을 저장함  
            progress = i / total_steps if total_steps > 0 else 1.0 #만약 total_step이 0보다 크다면 i를 total_step으로 나눈 값으로 저장하고 아니라면 1.0으로 저장
            delay = initial_delay + (final_delay - initial_delay) * (progress ** ease_power) #딜레이 값을 계산하여 저장
            line = f"{BOLD}뽑는중{RESET} {spin}  " #안내 라인 저장
            for j, name in enumerate(names): #리스트 names를 반복하여 반복변수 j와 name를 가져옴
                if j == idx: #만약 반복변수 j가 idx와 같다면
                    line += f"{BLUE}[{name}]{RESET} " #line에 name을 파란색으로 추가
                else: #아니라면
                    line += f"{name} " #line에 name을 추가
            sys.stdout.write("\r" + line + " " * 10) #버퍼링 없이 출력하기
            sys.stdout.flush() #임시 저장 되어있는 데이터를 지움
            time.sleep(delay) #delay 값만큼 멈추기
            i += 1 #i에 1을 추가함
            if i > total_steps: #만약에 i가 total_steps보다 크다면
                break #멈추기
        sys.stdout.write("\r" + " " * term_w + "\r") #버퍼링 없이 출력하기
        sys.stdout.flush() #임시 저장 되어 있는 데이터를 지움
        reveal = f"{winner}!" #뽑힌 값을 reveal에 저장함
        if TTE_AVAILABLE: #만약 True라면
            self.tte_fireworks_reveal(reveal) #reveal에 폭죽 연출을 추가함
        else: #아니라면
            self.slow_print(reveal, delay=0.05) #함수 slow_print에 reveal과 delay를 넣어 실행
            confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE] #색 리스트
            for _ in range(3): #반복변수 _ / 3번을 반복하는 for 반복문
                line = "".join(random.choice(confetti_colors) + random.choice(["*", "✦", "✶", "✺"]) + RESET for _ in range(30)) #색과 그림을 임의로 선택해 연출한 줄을 30번 만들어 나온 값을 저장함
                print(line) #line을 출력함
                time.sleep(0.12) #0.12초를 멈춤
        return winner #winner를 내보냄

    def animate_final_prize(self, drawn_items): #drawn_items를 넣고 최종 당첨 항목을 연출과 함께 출력하는 함수
        if not drawn_items: #만약 drawn_items가 없다면
            return None #None 출력
        seen = {} #몇번 등장했는지 나타내는 딕셔너리
        label_to_original = {} #빈 딕셔너리
        dist = {} #빈 딕셔너리
        for item in drawn_items: #drawn_items의 반복 변수 항목인 item을 반복함
            seen[item] = seen.get(item, 0) + 1 #딕셔너리 seen에서 현재변수항목인 item에 1을 추가함
            suffix = '\u200b' * seen[item] #/u200b을 seen[item]의 값만큼 반복한 값을 저장
            label = item + suffix #item값과 sufflix을 합쳐 저장함
            dist[label] = dist.get(label, 0) + 1.0 #dist의 label 값을 1로 추가함
            label_to_original[label] = item #label_to_original의 label 값을 item 항목
        final_label = self.animate_prize_draw(dist) #animate_prize_draw에 dist를 넣고 나온 값을 저장
        if final_label is None: #만약 final_label이 없다면
            return None #None 내보내기
        return label_to_original.get(final_label, final_label) #label_to_original의 값 중에 final_label 값을 내보냄

    def animate_prize_draw_cards(self, dist): #보상을 뽑는 함수
        names = list(dist.keys()) #이름 리스트
        weights = list(dist.values()) #확률 리스트
        term_w = shutil.get_terminal_size((80, 20)).columns #터미널 사이즈를 조절하여 저장함.
        def center(s): 
            pad = max(0, (term_w - len(s)) // 2)
            return " " * pad + s
        cards_front = ["┌─────┐", "│  ?  │", "│     │", "└─────┘"]
        for _ in range(3):
            line = "   ".join(cards_front)
            print(center(line))
        time.sleep(0.25)
        revealed = [None, None, None]
        for i in range(3):
            revealed[i] = random.choices(names, weights=weights, k=1)[0]
            sys.stdout.write("\033[F" * 3)
            sys.stdout.flush()
            box_lines = []
            for j in range(3):
                label = revealed[j] if revealed[j] is not None else "  ?  "
                box = [
                    "┌─────┐",
                    f"│ {label:^3} │",
                    "│     │",
                    "└─────┘",
                ]
                box_lines.append(box)
            for line_idx in range(4):
                row = "   ".join(box_lines[j][line_idx] for j in range(3))
                print(center(row))
            time.sleep(0.18)
        winner = random.choices(names, weights=weights, k=1)[0]
        box = f"  🎉 당첨: {winner} 🎉  "
        pad = max(0, (term_w - len(box)) // 2)
        top = " " * pad + "+" + "-" * len(box) + "+"
        mid = " " * pad + "|" + box + "|"
        print(top)
        print(mid)
        print(top)
        self.slow_print(center(f"{LIGHT_GREEN}>> 축하합니다! {winner} <<{RESET}"), delay=0.02)
        confetti = [RED, LIGHT_GREEN, BLUE, YELLOW, MAGENTA]
        for _ in range(3):
            line = "".join(random.choice(confetti) + random.choice(["✦","✶","✺","*"]) + RESET for _ in range(term_w//3))
            print(center(line))
            time.sleep(0.06)
        print()
        return winner

class Scoreboard:

    def __init__(self, path='ranking json'):
        self.path = path
        self.scoreboard = self.load_scoreboard(path)

    def normalize_grade(self, s):
        if s is None:
            return "참가상"
        t = s.replace(" ", "").replace("　", "")
        if t in ("1 등급","1 등"):
            return "1 등급"
        if t in ("2 등급","2 등"):
            return "2 등급"
        if t in ("3 등급","3 등"):
            return "3 등급"
        if t in ("4 등급","4 등"):
            return "4 등급"
        if "참가" in t:
            return "참가상"
        return s

    def grade_to_num(self,g):
        gm = {"1 등급":1, "2 등급":2, "3 등급":3,"4 등급":4, "참가상":5}
        return gm.get(g, 4)

    def compute_draws_sum(self, draws):
        return sum(self.grade_to_num(self.normalize_grade(d)) for d in draws)
    
    def load_scoreboard(self, path):
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except Exception:
            pass
        return []

    def save_scoreboard(self, path, scoreboard):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(scoreboard, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("랭킹 파일 저장 중 오류:", e)

    def merge_scoreboard(self, scoreboard, new_entry):
        sid = new_entry.get("id")
        for i, e in enumerate(scoreboard):
            if e.get("id") == sid:
                scoreboard[i] = new_entry
                return scoreboard
        scoreboard.append(new_entry)
        return scoreboard

    def print_final_ranking(self, scoreboard):
        grade_map = {"1 등급":1, "2 등급":2, "3 등급":3, "4 등급":4, "참가상":5}
        def sort_key(x):
            final = self.normalize_grade(x.get("final"))
            draws = x.get("draws", [])
            return (grade_map.get(final, 4), sum(grade_map.get(self.normalize_grade(d), 4) for d in draws), x.get("id",""))
        scoreboard_sorted = sorted(scoreboard, key=sort_key)
        print("\n=== 최종 랭킹 ===")
        if not scoreboard_sorted:
            print("랭킹 데이터가 없습니다.")
            return
        for idx, entry in enumerate(scoreboard_sorted, start=1):
            sid = entry.get("id","")
            final = self.normalize_grade(entry.get("final"))
            draws = [self.normalize_grade(d) for d in entry.get("draws",[])]
            print(f"{idx}등 {sid}: {final} {draws}")

    def show_ranking(self):
        while True:
            clear()
            self.print_final_ranking(self.scoreboard)
            print()
            resp = input("입력: ").strip().lower()
            if resp == "b":
                clear()
                return
            if resp == "r":
                confirm = input("정말 초기화하겠습니까? (Y/N): ").strip().lower()
                if confirm == "y":
                    self.scoreboard.clear()
                    self.save_scoreboard("ranking.json", self.scoreboard)
                    clear()
                    print("랭킹보드를 초기화했습니다.")
                    time.sleep(1.0)
                continue

class playing_game:
    def __init__(self, deck: Deck, prize_draws_remaining: int, auto_draw: bool, decline_count: int, drawn_items: list):
        self.deck = deck
        self.prize_draws_remaining = prize_draws_remaining
        self.auto_draw = auto_draw
        self.decline_count = decline_count
        self.drawn_items = drawn_items
        self.player_hand = []
        self.dealer_hand = []
        self.dp = Display()

    def deal_initial_cards(self):
        self.player_hand = self.deck.draw(2)
        self.dealer_hand = self.deck.draw(2)
        p_score = hand_score(self.player_hand)
        p_disp = self.dp.color_score(p_score)
        header = f"내 카드: {self.player_hand} {BOLD}(합: {p_disp}){RESET}"
        self.dp.tte_slide_print(header)
        print()
        self.dp.slow_print(f"딜러 카드 중 한 장: {self.dealer_hand[0]}", delay=0.05)
    
    def _player_turn(self):
        while True:
            cmd = monitored_input(f"내 차례 {BOLD}[hit/stand]{RESET}: ").strip().lower()
            if cmd in ("l",):
                continue
            if cmd in ("hit", "h"):
                self.player_hand += self.deck.draw(1)
                p_score = hand_score(self.player_hand)
                p_disp = self.dp.color_score(p_score)
                self.dp.slow_print(f"플레이어 Hit → {self.player_hand} {BOLD}(합: {p_disp}){RESET}", delay=0.05)
                if p_score > 21:
                    self.dp.slow_print(f"{RED}플레이어 {BOLD}버스트!{RESET}", delay=0.05)
                    return True
                return False
            elif cmd in ("stand", "s"):
                self.dp.slow_print("플레이어가 Stand 합니다.", delay=0.05)
                return True
            else:
                print("잘못 입력했습니다. 다시 입력하세요.")
    def _dealer_turn(self):
        if hand_score(self.dealer_hand) < 17:
            self.dealer_hand += self.deck.draw(1)
            self.dp.slow_print("딜러: Hit", delay=0.05)
            time.sleep(1)
            if hand_score(self.dealer_hand) > 21:
                self.dp.slow_print(f"{RED}딜러 {BOLD}버스트!{RESET}", delay=0.05)
                return True
            return False
        else:
            self.dp.slow_print("딜러: Stand", delay=0.05)
            time.sleep(1)
            return True
        
    def play_turns(self):
        player_done = False
        dealer_done = False
        while not (player_done and dealer_done):
            if not player_done:
                player_done = self._player_turn()
                if player_done and hand_score(self.player_hand) > 21:
                    if not dealer_done:
                        self.dp.slow_print("딜러:Stand", delay=0.05)
                        time.sleep(1)
                    dealer_done = True
                    break
            if not dealer_done:
                dealer_done = self._dealer_turn()
            if player_done and dealer_done:
                break

    def determine_result(self):
        p = hand_score(self.player_hand)
        d = hand_score(self.dealer_hand)
        if p > 21:
            return "패배"
        elif d > 21:
            return "승리"
        elif p > d:
            return "승리"
        elif p < d:
            return "패배"
        else:
            self.player_cards = len(self.player_hand)
            self.dealer_cards = len(self.dealer_hand)
            if self.player_cards < self.dealer_cards:
                return "승리"
            elif self.player_cards > self.dealer_cards:
                return "패배"
            else:
                return "무승부"
    def show_result(self, result: str):
        print()
        print(f"{BOLD}[Enter를 눌러 결과보기]{RESET}", end="", flush=True)
        monitored_input("") 
        clear()
        print("--- 게임 종료 ---")
        if result == "패배":
            result_display = f"{RED}{BOLD}{result}{RESET}"
        elif result == "승리":
            result_display = f"{BLUE}{BOLD}{result}{RESET}"
        else:
            result_display = f"{BOLD}{result}{RESET}"
        player_score_disp = hand_score(self.player_hand)
        dealer_score_disp = hand_score(self.dealer_hand)
        result_delay = 0.1 if (player_score_disp > 21 or dealer_score_disp > 21) else 0.2
        self.dp.slow_print(f"결과: {result_display} ", delay=result_delay)
        print()
        print(f"플레이어 최종: {self.player_hand} {BOLD}(합: {self.dp.color_score(player_score_disp)}){RESET}")
        print(f"딜러 최종:     {self.dealer_hand} {BOLD}(합: {self.dp.color_score(dealer_score_disp)}){RESET}")

    def do_draw(self, dist,silent=False):
        if silent:
            print(f"{YELLOW}상품 뽑기 자동진행{RESET} (남은 뽑기: {self.prize_draws_remaining})")
            interim = self.dp.animate_prize_draw(dist)
            self.drawn_items.append(interim)
            self.prize_draws_remaining -= 1
            print(f"이번 뽑기 결과: {interim}")
        if not silent:
            interim = self.dp.animate_prize_draw(dist)
            self.drawn_items.append(interim)
            self.prize_draws_remaining -= 1
            print(f"이번 뽑기 결과: {interim}")
            print("뽑기 항목: [ " + ", ".join(self.drawn_items) + " ]" + f" (남은 뽑기: {self.prize_draws_remaining})\n")
    
    def hand_prize(self, result: str):
        p_score = hand_score(self.player_hand)
        dist = reward_distribution(p_score, result)
        print("\n--- 상품 확률표 ---")
        for k, v in dist.items():
            pct = v * 100 if isinstance(v, float) and v <= 1.0 else v
            try:
                print(f"{k}: {pct:.1f}%")
            except:
                print(f"{k}: {pct}")
        print("-------------------")
        if self.prize_draws_remaining <= 0:
            print(f"{RED}남은 뽑기 회수가 없습니다. 건너뜁니다.{RESET}\n")
            return
        if self.auto_draw:
            self.do_draw(dist, silent=True)
            return
        prompt = f"상품을 {BOLD}뽑기{RESET} 하시겠습니까? (남은 뽑기: {self.prize_draws_remaining}) {BOLD}[Y/N]{RESET} "
        if input_clear(prompt).strip().lower() == "y":
            self.do_draw(dist)
        else:
            print(f"상품 {BOLD}뽑기{RESET}를 건너뜁니다.")
            self.decline_count += 1
            if self.decline_count >= 2:
                self.auto_draw = True
                print(f"{LIGHT_GREEN}다음부터는 질문 없이 자동으로 뽑기를 진행합니다.{RESET}")
        print()

    def run(self):
        self.deal_initial_cards()
        self.play_turns()
        result = self.determine_result()
        self.show_result(result)
        if result == "무승부":
            return False, self.prize_draws_remaining, self.auto_draw, self.decline_count, self.drawn_items
        self.hand_prize(result)
        return True, self.prize_draws_remaining, self.auto_draw, self.decline_count, self.drawn_items   
    
dp = Display()
sb = Scoreboard()

def main():
    clear()
    print()
    ascii_art = r"""
 ******   **           **       ******  **   **      **     **       ******  **   **
/*////** /**          ****     **////**/**  **      /**    ****     **////**/**  **
/*   /** /**         **//**   **    // /** **       /**   **//**   **    // /** **
/******  /**        **  //** /**       /****        /**  **  //** /**       /****
/*//// **/**       **********/**       /**/**       /** **********/**       /**/**
/*    /**/**      /**//////**//**    **/**//**  **  /**/**//////**//**    **/**//**
/******* /********/**     /** //****** /** //**//***** /**     /** //****** /** //**
///////  //////// //      //   //////  //   //  /////  //      //   //////  //   //
"""
    rules = [
        "",
        "",
        "- 트럼프 카드에서 A는 1, 11 역할을 하고 J, Q, K는 각각 10 나머지 카드는 각각의 숫자입니다.",
        "- 숫자를 총합하여 21에 가까울 수록 유리합니다.",
        "- 시작시 딜러와 플레이어는 각각 2장씩 받게됩니다.",
        "- 21을 넘기면 버스트(패배)입니다. 동점이면 카드 수로 우열을 판정합니다.",
        "- 승리/패배에 따라 상품 뽑기 확률표가 제공됩니다.",
        "- 상품 뽑기는 3회 진행되며, 3개로 최종 뽑기를 진행합니다.",
        "",
        ascii_art,
    ]
    if TTE_AVAILABLE and Rain is not None:
        try:
            effect = Rain("\n".join(rules))
            effect.effect_config.merge = True
            with effect.terminal_output() as terminal:
                for frame in effect:
                    terminal.print(frame)
        except Exception:
            for line in rules:
                dp.slow_print(line, delay=0.02)
    else:
        for line in rules:
            dp.slow_print(line, delay=0.02)
    print()
    monitored_input(f"{BOLD}[Enter를 눌러 시작하기]{RESET}")
    clear()
    while True:
        clear()
        sid = monitored_input("학번을 입력하세요.: ").strip()
        if sid.lower() == "exit":
            break
        clear()
        print(f"플레이어 시작: {sid}\n")
        deck = Deck(num_decks=1)
        dp.display_counts_table(deck.counts())
        print()
        prize_draws_remaining = 3
        auto_draw = False
        decline_count = 0
        drawn_items = []
        count = 0
        while count < MAX_GAMES:
            prompt = f"게임을 시작하시겠습니까? (현재 {count}/{MAX_GAMES}) {BOLD}[Y/N]{RESET} "
            ans = ask_yes_no(prompt)
            if ans == "y":
                clear()
                dp.display_counts_table(deck.counts())
                print(f"\n=== 게임 {count+1} 시작! (남은 카드: {deck.remaining()}) ===")
                play_game = playing_game(deck, prize_draws_remaining, auto_draw, decline_count, drawn_items)
                played, prize_draws_remaining, auto_draw, decline_count, drawn_items = play_game.run()
                if played:
                    count += 1
                if prize_draws_remaining <= 0 or len(drawn_items) >= 3:
                    break
            else:
                print("게임을 종료합니다.")
                break
        if drawn_items:
            print("\n--- 최종 추첨을 진행합니다 ---")
            final = dp.animate_final_prize(drawn_items)
            if final is None:
                final = drawn_items[-1] if drawn_items else "참가상"
            print(f"학번 {sid} 최종 상품: {final}")
            print(f"획득 상품 목록: {drawn_items}")
            entry = {"id": sid, "final": sb.normalize_grade(final), "draws": [sb.normalize_grade(d) for d in drawn_items]}
            sb.merge_scoreboard(sb.scoreboard, entry)
            sb.save_scoreboard(sb.path, sb.scoreboard)
        else:
            print(f"학번 {sid} 뽑기 결과가 없어 기록에 추가하지 않습니다.")
    sb.print_final_ranking(sb.scoreboard)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단되었습니다.")
        sys.exit(0)

