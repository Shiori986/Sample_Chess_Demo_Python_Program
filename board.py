from pieces import *
# ============================
#   CREATE STARTING BOARD
# ============================

from pieces import *

def create_starting_board():
    """Return an 8x8 list of lists representing the starting chess position."""

    board = [
        [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN,
         BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK],

        [BLACK_PAWN] * 8,

        [" "] * 8,
        [" "] * 8,
        [" "] * 8,
        [" "] * 8,

        [WHITE_PAWN] * 8,

        [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN,
         WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]
    ]

    return board


# ============================
#   ANSI COLOR DEFINITIONS
# ============================

# Light tan square
LIGHT = "\033[48;5;223m"

# Dark grey square
DARK = "\033[48;5;240m"

# Reset color
RESET = "\033[0m"


# ============================
#   SQUARE COLOR FUNCTION
# ============================

def get_square_color(row, col):
    """Return LIGHT or DARK depending on board position."""
    return LIGHT if (row + col) % 2 == 0 else DARK


# ============================
#   PRINT BOARD FUNCTION
# ============================

def print_board(board):
    TILE_WIDTH = 7
    TILE_HEIGHT = 4
    PIECE_LINE = TILE_HEIGHT // 2  # middle line (3 for 7×7)

    file_labels = ["A", "B", "C", "D", "E", "F", "G", "H"]

    print()  # top padding

    # Loop through each rank (row)
    for row in range(0, 8):  # 7 down to 0
        rank_label = str(8 - row)

        # Print each of the 7 lines that make up the tile height
        for line in range(TILE_HEIGHT):

            # Left rank label only on the center line
            if line == PIECE_LINE:
                print(f" {rank_label} ", end="")
            else:
                print("   ", end="")  # 3 spaces for alignment

            # Print each file (column)
            for col in range(8):
                piece = board[row][col]
                color = get_square_color(row, col)

                if line == PIECE_LINE:
                    # Center the piece horizontally in the 7‑wide tile
                    content = f"   {piece}   "
                else:
                    # Background-only line
                    content = " " * TILE_WIDTH

                print(f"{color}{content}{RESET}", end="")

            # Right rank label on the center line
            if line == PIECE_LINE:
                print(f" {rank_label}")
            else:
                print()

    # Print file labels centered under each tile
    print("\n   ", end="")  # left padding
    for f in file_labels:
        print(f.center(TILE_WIDTH), end="")
    print("\n")