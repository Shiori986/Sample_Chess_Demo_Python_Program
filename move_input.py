def parse_square(square_str):
    """Convert something like 'e2' into (row, col) indices."""
    if len(square_str) != 2:
        return None

    file_char = square_str[0].lower()   # a–h
    rank_char = square_str[1]           # 1–8

    if file_char < 'a' or file_char > 'h':
        return None
    if rank_char < '1' or rank_char > '8':
        return None

    col = ord(file_char) - ord('a')     # a→0, b→1, ..., h→7
    row = 8 - int(rank_char)            # rank 8→row 0, rank 1→row 7

    return (row, col)


def get_player_move():
    """Ask the user for a move like 'e2 e4' and return parsed coordinates."""
    move = input("Enter your move (e.g. 'e2 e4'): ").strip()

    # Allow quitting mid-match
    if move.lower() == "quit":
        return "quit"

    parts = move.split()
    if len(parts) != 2:
        print("Invalid format. Use: e2 e4")
        return None

    from_sq = parse_square(parts[0])
    to_sq = parse_square(parts[1])

    if from_sq is None or to_sq is None:
        print("Invalid square. Use something like 'e2'.")
        return None

    return from_sq, to_sq