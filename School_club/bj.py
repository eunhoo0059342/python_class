
import random
import math
import os
import sys
import time
import shutil
from collections import Counter

RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_clear(prompt):
    resp = input(prompt)
    if resp.strip().lower() in ('y', 'n'):
        clear()
    return resp

def slow_print(text, delay=0.1, end="\n"):
    for ch in str(text):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

RED = "\033[31m"
LIGHT_GREEN = "\033[92m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
NORM = "\033[22m"
BOLD = "\033[1m"

try:
    from terminaltexteffects.effects.effect_slide import Slide
    from terminaltexteffects.effects.effect_fireworks import Fireworks
    from terminaltexteffects.effects.effect_rain import Rain
    TTE_AVAILABLE = True
except Exception:
    Slide = None
    Fireworks = None
    Rain = None
    TTE_AVAILABLE = False

def tte_slide_print(text):
    if not TTE_AVAILABLE or Slide is None:
        slow_print(text)
        return
    effect = Slide(text)
    effect.effect_config.merge = True
    try:
        with effect.terminal_output() as term:
            for frame in effect:
                term.print(frame)
    except Exception:
        slow_print(text)

def tte_fireworks_reveal(text):
    if TTE_AVAILABLE and Fireworks is not None:
        effect = Fireworks(text)
        effect.effect_config.merge = True
        try:
            with effect.terminal_output() as term:
                for frame in effect:
                    term.print(frame)
            return
        except Exception:
            pass
    slow_print(text, delay=0.03)
    confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE]
    for _ in range(3):
        line = ""
        for _ in range(30):
            c = random.choice(confetti_colors)
            line += c + random.choice(["*", "✦", "✶", "✺"]) + RESET
        print(line)
        time.sleep(0.12)

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
    def counts(self):
        c = {r:0 for r in RANKS}
        for card in self.cards:
            c[card] += 1
        return c

def hand_score(hand):
    total = sum(rank_value(r) for r in hand)
    aces = hand.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def logistic(x, alpha, beta):
    return 1 / (1 + math.exp(-alpha * (x-beta)))

def reward_distribution(score, result):
    if result == "패배":
        return {"참가상": 1.0}

    logit_1 = 0.98 * logistic(score, alpha=0.4, beta=19)
    logit_2 = 1.20 * logistic(score, alpha=0.4, beta=19)
    logit_3 = 0.01 * (1 - logistic(score, alpha=0.4, beta=19))
    logit_4 = 0.58 * (1 - logistic(score, alpha=0.4, beta=19))

    logits = [logit_1, logit_2, logit_3, logit_4]
    exp_logits = [math.exp(x) for x in logits]
    total = sum(exp_logits)

    probs = [x / total for x in exp_logits]

    return {
        "1 등급": probs[0],
        "2 등급": probs[1],
        "3 등급": probs[2],
        "4 등급": probs[3],
    }

def choose_reward(score, result):
    dist = reward_distribution(score, result)
    rewards = list(dist.keys())
    probs = list(dist.values())
    return random.choices(rewards, weights=probs, k=1)[0]

def color_score(n):
    try:
        n_int = int(n)
    except:
        return str(n)
    if n_int > 21:
        return f"{RED}{n_int}{RESET}"
    if n_int == 21:
        return f"{LIGHT_GREEN}{n_int}{RESET}"
    return str(n_int)

def animate_prize_draw(dist):
    items = list(dist.items())
    names = [k for k,_ in items]
    weights = [v for _,v in items]
    n = len(names)
    if n == 0:
        return None

    if sum(weights) == 0:
        weights = [1.0] * n

    winner = random.choices(names, weights=weights, k=1)[0]
    winner_idx = names.index(winner)

    spinner = ['|','/','-','\\']
    term_w = shutil.get_terminal_size((80, 20)).columns
    if n <= 1:
        reveal = f"{winner}!"
        if TTE_AVAILABLE:
            tte_fireworks_reveal(reveal)
        else:
            slow_print(reveal, delay=0.1)
            confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE]
            for _ in range(3):
                line = "".join(random.choice(confetti_colors) + random.choice(["*", "✦", "✶", "✺"]) + RESET for _ in range(30))
                print(line)
                time.sleep(0.12)
        return winner

    cycles_needed = random.randint(4, 8)
    initial_delay = 0.06
    final_delay = 0.30
    ease_power = 2.0
    total_steps = cycles_needed * n + winner_idx

    i = 0
    while True:
        idx = i % n
        spin = spinner[i % len(spinner)]
        progress = i / total_steps if total_steps > 0 else 1.0
        delay = initial_delay + (final_delay - initial_delay) * (progress ** ease_power)
        line = f"{BOLD}뽑는중{RESET} {spin}  "
        for j, name in enumerate(names):
            if j == idx:
                line += f"{BLUE}[{name}]{RESET} "
            else:
                line += f"{name} "
        sys.stdout.write("\r" + line + " " * 10)
        sys.stdout.flush()
        time.sleep(delay)
        i += 1
        if i > total_steps:
            break
    sys.stdout.write("\r" + " " * term_w + "\r")
    sys.stdout.flush()
    reveal = f"{winner}!"
    if TTE_AVAILABLE:
        tte_fireworks_reveal(reveal)
    else:
        slow_print(reveal, delay=0.05)
        confetti_colors = [RED, LIGHT_GREEN, YELLOW, MAGENTA, BLUE]
        for _ in range(3):
            line = "".join(random.choice(confetti_colors) + random.choice(["*", "✦", "✶", "✺"]) + RESET for _ in range(30))
            print(line)
            time.sleep(0.12)
    return winner

def animate_final_prize(drawn_items):
    if not drawn_items:
        return None

    seen = {}
    label_to_original = {}
    dist = {}

    for item in drawn_items:
        seen[item] = seen.get(item, 0) + 1
        suffix = '\u200b' * seen[item]
        label = item + suffix
        dist[label] = dist.get(label, 0) + 1.0
        label_to_original[label] = item

    final_label = animate_prize_draw(dist)
    if final_label is None:
        return None
    return label_to_original.get(final_label, final_label)

def animate_prize_draw_cards(dist):
    names = list(dist.keys())
    weights = list(dist.values())
    term_w = shutil.get_terminal_size((80, 20)).columns

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
    slow_print(center(f"{LIGHT_GREEN}>> 축하합니다! {winner} <<{RESET}"), delay=0.02)
    confetti = [RED, LIGHT_GREEN, BLUE, YELLOW, MAGENTA]
    for _ in range(3):
        line = "".join(random.choice(confetti) + random.choice(["✦","✶","✺","*"]) + RESET for _ in range(term_w//3))
        print(center(line))
        time.sleep(0.06)
    print()
    return winner

def _color_count_str(n):
    num = int(n)
    if num == 0:
        return "  "
    num_str = f"{num:>2}"
    if num >= 3:
        return f"{NORM}{num_str}{RESET}"
    if num == 2:
        return f"{NORM}{YELLOW}{num_str}{RESET}"
    return f"{NORM}{RED}{num_str}{RESET}"

def display_counts_table(counts):
    print("─ 남은 카드 수 ─")
    sep = "   "
    row1 = sep.join(f"{r:<2} : {_color_count_str(counts[r])}" for r in ["A","2","3","4"])
    row2 = sep.join(f"{r:<2} : {_color_count_str(counts[r])}" for r in ["5","6","7","8"])
    row3 = sep.join(f"{r:<2} : {_color_count_str(counts[r])}" for r in ["9","10","J","Q"])
    row4 = f"{'K':<2} : {_color_count_str(counts['K'])}"
    print(row1)
    print(row2)
    print(row3)
    print(row4)

def perform_final_draw_prompt(drawn_items):
    clear()
    if not drawn_items:
        return False
    print("뽑기 항목: [" + ", ".join(drawn_items) + "]")
    print()
    while True:
        cmd = input(f"{BOLD}'뽑기'{RESET} 라고 입력해주세요: ").strip()
        if cmd == "뽑기":
            clear()
            final = animate_final_prize(drawn_items)
            drawn_items.clear()
            if final is not None:
                print(f"최종 당첨: {final}")
            sys.exit(0)
        else:
            print("입력이 정확하지 않습니다. '뽑기'를 정확히 입력해주세요.")

def ask_yes_no(prompt):
    while True:
        resp = input_clear(prompt)
        v = resp.strip().lower()
        if v in ('y','n'):
            return v
        print("잘못된 입력입니다. Y 또는 N을 입력해주세요.")

def play_turn_based(deck: Deck, prize_draws_remaining: int, auto_draw: bool, decline_count: int, drawn_items: list):
    player_hand = deck.draw(2)
    dealer_hand = deck.draw(2)
    player_done = False
    dealer_done = False
    p_score = hand_score(player_hand)
    p_disp = color_score(p_score)
    header = f"내 카드: {player_hand} {BOLD}(합: {p_disp}){RESET}"
    tte_slide_print(header)
    print()
    slow_print(f"딜러 카드 중 한 장: {dealer_hand[0]}", delay=0.05)

    while not (player_done and dealer_done):
        if not player_done:
            cmd = input(f"내 차례 {BOLD}[hit/stand]{RESET}: ").strip().lower()
            if cmd in ("hit", "h"):
                player_hand += deck.draw(1)
                p_score = hand_score(player_hand)
                p_disp = color_score(p_score)
                slow_print(f"플레이어 Hit → {player_hand} {BOLD}(합: {p_disp}){RESET}", delay=0.05)
                if p_score > 21:
                    slow_print(f"{RED}플레이어 {BOLD}버스트!{RESET}", delay=0.05)
                    player_done = True
                    if not dealer_done:
                        slow_print("딜러: Stand", delay=0.05)
                        time.sleep(1)
                    dealer_done = True
                    break

            elif cmd in ("stand", "s"):
                slow_print("플레이어가 Stand 합니다.", delay=0.05)
                player_done = True
            else:
                print("잘못 입력했습니다. 다시 입력하세요.")


        if not dealer_done:
            dealer_score_before = hand_score(dealer_hand)
            if dealer_score_before < 17:
                dealer_hand += deck.draw(1)
                dealer_score = hand_score(dealer_hand)
                slow_print("딜러: Hit", delay=0.05)
                time.sleep(1)
                if dealer_score > 21:
                    slow_print(f"{RED}딜러 {BOLD}버스트!{RESET}", delay=0.05)
                    dealer_done = True
            else:
                slow_print("딜러: Stand", delay=0.05)
                time.sleep(1)
                dealer_done = True

        if player_done and dealer_done:
            break

    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)

    if player_score > 21:
        result = "패배"
    elif dealer_score > 21:
        result = "승리"
    elif player_score > dealer_score:
        result = "승리"
    elif player_score < dealer_score:
        result = "패배"
    else:
        player_cards = len(player_hand)
        dealer_cards = len(dealer_hand)
        if player_cards < dealer_cards:
            result = "승리"
        elif player_cards > dealer_cards:
            result = "패배"
        else:
            result = "무승부"

    print()
    print(f"{BOLD}[Enter를 눌러 결과보기]{RESET}", end="", flush=True)
    input()
    clear()
    print("--- 게임 종료 ---")
    print()
    if result == "패배":
        result_display = f"{RED}{BOLD}{result}{RESET}"
    elif result == "승리":
        result_display = f"{BLUE}{BOLD}{result}{RESET}"
    else:
        result_display = f"{BOLD}{result}{RESET}"
    result_delay = 0.1 if (player_score > 21 or dealer_score > 21) else 0.2
    slow_print(f"결과: {result_display}", delay=result_delay)

    player_score_disp = color_score(player_score)
    dealer_score_disp = color_score(dealer_score)
    print()
    print(f"플레이어 최종: {player_hand} {BOLD}(합: {player_score_disp}){RESET}")
    print(f"딜러 최종:     {dealer_hand} {BOLD}(합: {dealer_score_disp}){RESET}")

    if result == "무승부":
        return False, prize_draws_remaining, auto_draw, decline_count, drawn_items

    print("\n--- 상품 확률표 ---")
    dist = reward_distribution(player_score, result)
    for k, v in dist.items():
        pct = v * 100 if isinstance(v, float) and v <= 1.0 else v
        print(f"{k}: {pct:.1f}%")
    print("-------------------")
    print()

    if prize_draws_remaining <= 0:
        print(f"{RED}남은 뽑기 회수가 없습니다. 건너뜁니다.{RESET}\n")
        if drawn_items:
            perform_final_draw_prompt(drawn_items)
        return True, prize_draws_remaining, auto_draw, decline_count, drawn_items

    if auto_draw:
        print(f"{YELLOW}상품 뽑기 자동진행{RESET} (남은 뽑기: {prize_draws_remaining})")
        interim = animate_prize_draw(dist)
        drawn_items.append(interim)
        prize_draws_remaining -= 1
        print(f"이번 뽑기 결과: {interim}")

        if len(drawn_items) >= 3:
            print("중간 뽑기 3회를 모았습니다. 최종 추첨을 진행합니다...")
            perform_final_draw_prompt(drawn_items)
        elif prize_draws_remaining <= 0 and drawn_items:
            print("남은 뽑기 회수가 0입니다. 모은 항목들로 최종 추첨을 진행합니다...")
            perform_final_draw_prompt(drawn_items)

        return True, prize_draws_remaining, auto_draw, decline_count, drawn_items

    prompt = f"상품을 {BOLD}뽑기{RESET} 하시겠습니까? (남은 뽑기: {prize_draws_remaining}) {BOLD}[Y/N]{RESET} "
    choice = input_clear(prompt)
    if choice.strip().lower() == "y":
        interim = animate_prize_draw(dist)
        drawn_items.append(interim)
        prize_draws_remaining -= 1
        print(f"이번 뽑기 결과: {interim}")
        print("뽑기 항목: [ " + ", ".join(drawn_items) + " ]" + f" (남은 뽑기: {prize_draws_remaining})\n")

        if len(drawn_items) >= 3:
            print("중간 뽑기 3회를 모았습니다. 최종 추첨을 진행합니다...")
            perform_final_draw_prompt(drawn_items)
        elif prize_draws_remaining <= 0 and drawn_items:
            print("남은 뽑기 회수가 0입니다. 모은 항목들로 최종 추첨을 진행합니다...")
            perform_final_draw_prompt(drawn_items)

    else:
        print(f"상품 {BOLD}뽑기{RESET}를 건너뜁니다.")
        decline_count += 1
        if decline_count >= 2:
            auto_draw = True
            print(f"{LIGHT_GREEN}다음부터는 질문 없이 자동으로 뽑기를 진행합니다.{RESET}")
    print()
    return True, prize_draws_remaining, auto_draw, decline_count, drawn_items

MAX_GAMES = 5
count = 0
prize_draws_remaining = 3
auto_draw = False
decline_count = 0
drawn_items = []

try:
    while count < MAX_GAMES:
        if count == 0:
            clear()
            prompt = f"게임을 시작하시겠습니까? (현재 {count}/{MAX_GAMES}) {BOLD}[Y/N]{RESET} "
        else:
            prompt = f"이어하기 (현재 {count}/{MAX_GAMES}) {BOLD}[Y/N]{RESET} "
        ans = ask_yes_no(prompt)
        if ans == "y":
            if count == 0:
                clear()
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
                    "- 트럼프 카드에서 A는 1, 11역활을 하고 J, Q, K는 각각 10 나머지 카드는 각각의 숫자입니다.",
                    "- 숫자를 총합하여 21에 가까울 수록 유리합니다.",
                    "- 시작시 딜러와 플레이어는 각각 2장씩 받게됩니다.",
                    "- 21을 넘기면 버스트(패배)입니다. 동점이면 카드 수로 우열을 판정합니다.",
                    "- 승리/패배에 따라 상품 뽑기 확률표가 제공됩니다.",
                    "- 상품 뽑기는 3회 진행되며, 3개로 최종 뽑기를 진행합니다.",
                    "", 
                    ascii_art,
                ]

                rules_text = "\n".join(rules)
                if TTE_AVAILABLE and Rain is not None:
                    try:
                        effect = Rain(rules_text)
                        effect.effect_config.merge = True
                        with effect.terminal_output() as terminal:
                            for frame in effect:
                                terminal.print(frame)
                    except Exception:
                        for line in rules:
                            slow_print(line, delay=0.02)
                else:
                    for line in rules:
                        slow_print(line, delay=0.02)
                print()
                input(f"{BOLD}[Enter를 눌러 시작하기]{RESET}")
                clear()
                deck = Deck(num_decks=1)
            counts = deck.counts()
            display_counts_table(counts)
            print(f"\n=== 게임 {count+1} 시작! (남은 카드: {deck.remaining()}) ===")
            print()
            (played, prize_draws_remaining, auto_draw, decline_count, drawn_items) = play_turn_based(
                deck, prize_draws_remaining, auto_draw, decline_count, drawn_items
            )
            if played:
                count += 1
        else:
            print("게임을 종료합니다.")
            break
except KeyboardInterrupt:
    print("\n사용자에 의해 중단되었습니다.")
    sys.exit(0)

print(f"{count}경기 플레이 후 종료합니다.")
# --- 예시 코드 ---
# # 0~21점 구간 확률 계산
# for i in range(21):
#     print(reward_distribution(i+1, '승리'), i+1)