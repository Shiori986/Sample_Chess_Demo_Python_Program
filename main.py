def print_banner():
    print(r"""
 ██████╗██╗  ██╗███████╗███████╗███████╗
██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝
██║     ███████║█████╗  ███████╗█████╗  
██║     ██╔══██║██╔══╝  ╚════██║██╔══╝  
╚██████╗██║  ██║███████╗███████║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
""")


from validation import (
    get_valid_name,
    get_valid_choice,
    get_valid_color,
    check_global_command
)

from board import create_starting_board, print_board

from move_input import get_player_move, parse_square
from move_logic import make_move
from music_picker import choose_music_file
from music_player import start_music, stop_music

# ============================
#   CHESS DEMO MAIN PROGRAM
# ============================

def main_menu():
    while True:
        print_banner()
        print("\n1. Start Game")
        print("2. Settings (future)")
        print("3. Quit Game\n")
       
 

        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
             settings = start_game_setup()
             if settings is None:
                 continue  # user cancelled or returned to menu

             # Start music if selected
    
             if settings["music_file"]:
                 start_music(settings["music_file"], settings["music_mode"])

             start_game(settings)

             # Stop music when game ends
             stop_music()
        
        elif choice == "2":
            print("\n[SETTINGS MENU — coming soon]")
        elif choice == "3":
            quit_game()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



def start_game(settings):
    print("\nStarting game with settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")

    print("\n[GAME WILL BEGIN HERE — board, turns, etc.]")

    board = create_starting_board()
    white_to_move = True

    while True:
        print_board(board)

        # Announce whose turn it is
    
        if white_to_move:
            print("\nWhite to move.")
        else:
            print("\nBlack to move.")

        move = get_player_move()
        if move == "quit":
            print("Exiting to main menu...")
            return  # <-- THIS returns to the menu cleanly

        if move is None:
            continue  # invalid input, ask again

        from_sq, to_sq = move

        success, white_to_move = make_move(board, from_sq, to_sq, white_to_move)
        if not success:
            continue  # illegal move, ask again


# ============================
#   GAME STARTER
# ============================

import random


PREFIXES = [
    "Astra", "Neo", "Cyber", "Echo", "Vanta", "Solar", "Nemesis", "Lucia", "Luna"
    "Iron", "Deep", "Quantum", "Omega", "Proto", "Hyper", "Rover", "Aemeath", "Shiori"
]

ROOTS = [
    "mind", "core", "flare", "knight", "pulse", "forge",
    "shade", "matrix", "circuit", "logic", "vector", "signal"
]

SUFFIXES = [
    "-X", "Zero", "Prime", "Unit", "Node", "One", "9000",
    "VX", "Sigma", "Protocol", "Engine"
]

def generate_ai_name():
    prefix = random.choice(PREFIXES)
    root = random.choice(ROOTS)
    suffix = random.choice(SUFFIXES)
    return prefix + root.capitalize() + suffix



def start_game_setup():
    print("\nWelcome to Chess Demo!\n")

    # 1. Player Name
    player_name = get_valid_name("Enter your name: ")
    if player_name in ("QUIT", "MENU"):
        handle_global_command(player_name)
        return None

    # 2. Game Mode
    print("\nChoose game mode:")
    print("1. Solo")
    print("2. Multiplayer")
    mode = get_valid_choice("Enter 1 or 2: ", ["1", "2"])
    if mode in ("QUIT", "MENU"):
        handle_global_command(mode)
        return None

    # 3. Color
    print("\nChoose your color:")
    color = get_valid_color("Enter W/White or B/Black: ")
    if color in ("QUIT", "MENU"):
        handle_global_command(color)
        return None

    # 4. Difficulty (solo only)
    difficulty = None
    if mode == "1":
        print("\nChoose difficulty:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        difficulty = get_valid_choice("Enter 1, 2, or 3: ", ["1", "2", "3"])
        if difficulty in ("QUIT", "MENU"):
            handle_global_command(difficulty)
            return None

    # AI name (solo only)
    ai_name = None
    if mode == "1":
        ai_name = generate_ai_name()

    # 5. Music
    print("\nWould you like to add music?")
    print("1. Yes")
    print("2. No")
    music_choice = get_valid_choice("Enter 1 or 2: ", ["1", "2"])
    if music_choice in ("QUIT", "MENU"):
        handle_global_command(music_choice)
        return None

    music_mode = None
    music_file = None

    if music_choice == "1":
        print("\nMusic options:")
        print("1. Loop")
        print("2. Shuffle")
        music_mode = get_valid_choice("Enter 1 or 2: ", ["1", "2"])
        if music_mode in ("QUIT", "MENU"):
            handle_global_command(music_mode)
            return None

        print("\nA file picker will open. Choose your music file.")
        music_file = choose_music_file()

        if not music_file:
          print("No file selected. Returning to menu.")
          return None

    return {
        "player_name": player_name,
        "mode": mode,
        "color": color,
        "difficulty": difficulty,
        "music_mode": music_mode,
        "music_file": music_file,
        "ai_name": ai_name
    }
	

# ============================
#   QUIT FUNCTION
# ============================

def quit_game():
    print("\nExiting game. Goodbye!")
    exit()


# ============================
#   PROGRAM ENTRY POINT
# ============================

if __name__ == "__main__":
    main_menu()