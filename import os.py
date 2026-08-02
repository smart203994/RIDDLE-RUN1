import os
import json
import random
import time
import sys
import select
from datetime import date

# --- Cyberpunk Terminal Color Palettes ---
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
DING = '\a'

os.system('')  # Native Windows terminal color profile activation wrapper

# --- Persistent JSON Data Management Systems ---
JSON_FILE = "riddles.json"

def initialize_riddle_database():
    """Validates or seeds the structural external JSON riddle matrix storage file."""
    default_riddles = [
        {"question": "What has to be broken before you can use it?", "answer": "egg", "hint": "It's found in the kitchen."},
        {"question": "I am tall when young and short when old. What am I?", "answer": "candle", "hint": "It gives off light."},
        {"question": "I am an object, I have a head, a tail, but no body. What am I?", "answer": "coin", "hint": "It's worth money."},
        {"question": "I have three brothers but we do not meet each other. What am I?", "answer": "fan", "hint": "It keeps you cool."},
        {"question": "What has many keys but can’t open a single lock?", "answer": "keyboard", "hint": "You are typing on one right now."},
        {"question": "What gets wetter the more it dries?", "answer": "towel", "hint": "You use it after a shower."},
        {"question": "The more of me you take, the more you leave behind. What am I?", "answer": "footsteps", "hint": "Look down when you walk."},
        {"question": "What has hands but cannot clap?", "answer": "clock", "hint": "It tells the time."},
        {"question": "What has one eye but cannot see?", "answer": "needle", "hint": "Used for sewing clothes."},
        {"question": "What can travel around the world while staying in a corner?", "answer": "stamp", "hint": "Look at the corner of an envelope."}
    ]
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump(default_riddles, f, indent=4)

def load_riddle_matrix():
    """Extracts raw question arrays directly from the structured external file asset."""
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_leaderboard():
    """Parses local leaderboard text array stack, sorting for elite score limits."""
    scores = []
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                if ":" in line:
                    name, score_str = line.strip().split(":", 1)
                    try:
                        scores.append((name, int(score_str)))
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]

def save_score_to_leaderboard(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}:{score}\n")

def get_daily_status():
    """Compares calendar records to ensure true daily synchronization parameters."""
    try:
        with open("daily_status.txt", "r") as file:
            return file.read().strip() == str(date.today())
    except:
        return False

def set_daily_status_claimed():
    with open("daily_status.txt", "w") as file:
        file.write(str(date.today()))

def reset_all_databases():
    for f in ["leaderboard.txt", "daily_status.txt"]:
        if os.path.exists(f):
            os.remove(f)

# --- Thread-Safe Cross-Platform Input Countdown Engine ---
def terminal_countdown_input(prompt, timeout):
    """Monitors terminal interfaces using strict variable time decay tracking loops."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    
    if os.name == 'nt':
        import msvcrt
        start = time.time()
        input_str = ""
        while True:
            if time.time() - start > timeout:
                print(RED + "\n⏱️ TIME EXPIRATION DECOUPLING!" + RESET)
                return "time_out_event"
            if msvcrt.kbhit():
                char = msvcrt.getwche()
                if char == '\r' or char == '\n':
                    print()
                    return input_str
                elif char == '\b':
                    if len(input_str) > 0:
                        input_str = input_str[:-1]
                        sys.stdout.write(' \b')
                        sys.stdout.flush()
                else:
                    input_str += char
            time.sleep(0.02)
    else:
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip()
        else:
            print(RED + "\n⏱️ TIME EXPIRATION DECOUPLING!" + RESET)
            return "time_out_event"

# --- SYSTEM INITIALIZATION BOOTSTRAP ---
initialize_riddle_database()
keep_playing = "yes"

while keep_playing == "yes":
    leaderboard = get_leaderboard()
    high_score = leaderboard[0][1] if leaderboard else 0
    record_holder = leaderboard[0][0] if leaderboard else "None"
    daily_claimed = get_daily_status()
    clear()
    
    # Render Dashboard Grid System UI
    print(YELLOW + "==========================================================" + RESET)
    print(YELLOW + "                ⚔️  RIDDLE RUN: ARCHADEX ⚔️              " + RESET)
    print(YELLOW + "==========================================================" + RESET)
    print(f" 🏆 Overlord: {CYAN}{record_holder} ({high_score} PTS){RESET} | 🎁 Daily Cargo: " + (f"{RED}[LOCKED]{RESET}" if daily_claimed else f"{GREEN}[READY]{RESET}"))
    print(YELLOW + "----------------------------------------------------------" + RESET)
    print(f"  FEATURED MATRIX MATRIX BRAIN TEASER:")
    print(f"  {MAGENTA}\"I move fast but have no legs. I devour all but create nothing.\"{RESET}")
    print(f"  {MAGENTA}Answer Core Indicator: [ FIRE ]{RESET}")
    print(YELLOW + "==========================================================" + RESET)
    print("\n   SYSTEM OPERATIONS MENU:")
    print("   1. 🚀 Breach Active Riddle Labyrinth")
    print("   2. 🎁 Open Daily Present Cargo Box (+50 Score Modifier)")
    print("   3. 📊 View Top 5 Elite Agents Grid")
    print("   4. 🔄 Purge System Storage Database")
    print("   5. 🚪 Terminate Terminal Connection")
    
    menu_choice = input("\nSelect operational profile profile (1-5): ").strip()
    
    if menu_choice == "5":
        break

    if menu_choice == "4":
        reset_all_databases()
        print(GREEN + "\nData structural frameworks purged successfully!" + RESET)
        time.sleep(1.5)
        continue

    if menu_choice == "3":
        clear()
        print(YELLOW + "==========================================================" + RESET)
        print(YELLOW + "              🏆 TOP 5 RUN LEADERBOARD ARCHIVE            " + RESET)
        print(YELLOW + "==========================================================" + RESET)
        if not leaderboard:
            print("                 No active logs discovered.")
        for rank, (user, pts) in enumerate(leaderboard, 1):
            print(f"   [0{rank}] Agent: {CYAN}{user:<22}{RESET} -> {GREEN}{pts} PTS{RESET}")
        print(YELLOW + "==========================================================" + RESET)
        input("\nPress Enter to escape view profile...")
        continue

    if menu_choice == "2":
        if get_daily_status():
            print(RED + "\n❌ Present cargo already purged! Resets at midnight cycle." + RESET)
        else:
            set_daily_status_claimed()
            print(GREEN + "\n🎁 DECRYPTING CARGO CONTAINER STORAGE..." + RESET)
            time.sleep(1.2)
            print(YELLOW + "   [+] Injection Engine Loaded! +50 XP will sync to your next run." + RESET)
        input("\nPress Enter to return to main operations...")
        continue

    if menu_choice != "1":
        continue

    # --- Game Parameter Ingestion Loop ---
    name = input("\nIdentify Agent Alias Identity: ").strip()
    if not name:
        name = "Agent_Anonymous"
    
    print("\nSelect Operational Vitality Capacity (Difficulty):")
    print("1. Easy Simulation   (5 Lives | 15s Standard Decay)")
    print("2. Normal Labyrinth   (3 Lives | 12s Adaptive Decay)")
    print("3. Hardcore Matrix   (1 Life  | 8s Hyper-Speed Decay)")
    diff_choice = input("Select profile (1-3): ").strip()

    # Dynamic baseline values
    if diff_choice == "1":
        lives = 5
        base_timer = 15
    elif diff_choice == "3":
        lives = 1
        base_timer = 8
    else:
        lives = 3
        base_timer = 12

    # Dynamic Daily Cargo Point Modifier Injection Check
    score = 0
    if daily_claimed:
        score = 50
        print(GREEN + "\n⚡ Daily Cargo Modifier Detected! +50 XP appended to run database." + RESET)
        time.sleep(1.5)

    quiz_pool = load_riddle_matrix()
    if not quiz_pool:
        print(RED + "Critical Failure loading external riddles. Rebooting loop." + RESET)
        time.sleep(2)
        continue

    random.shuffle(quiz_pool)
    clear()

    # --- Core Runtime Logic Loop ---
    for index, item in enumerate(quiz_pool, 1):
        if lives <= 0:
            break

        # Adaptive Speed Mechanism Calculation
        # Timer decreases by 1 second for every riddle cleared, matching your query request
        current_adaptive_timer = max(4, base_timer - (index - 1))

        print(YELLOW + "----------------------------------------------------------" + RESET)
        print(f" {CYAN}Labyrinth Node Matrix: {index} of {len(quiz_pool)}{RESET}")
        print(f" Cumulative Balance: {GREEN}{score} PTS{RESET} | Vital Capacities: {RED}{'❤️' * lives}{RESET}")
        print(f" {YELLOW}⏱️ Adaptive Time Horizon Window: {current_adaptive_timer}s remaining!{RESET}")
        print(YELLOW + "----------------------------------------------------------" + RESET)
