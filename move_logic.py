# ==========================
#   PIECE IDENTIFICATION
# ==========================

from pieces import (
    WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING,
    BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING
)

    

WHITE_SET = {
    WHITE_PAWN,
    WHITE_ROOK,
    WHITE_KNIGHT,
    WHITE_BISHOP,
    WHITE_QUEEN,
    WHITE_KING
}

BLACK_SET = {
    BLACK_PAWN,
    BLACK_ROOK,
    BLACK_KNIGHT,
    BLACK_BISHOP,
    BLACK_QUEEN,
    BLACK_KING
}

def is_white_piece(piece):
    return piece in WHITE_SET

def is_black_piece(piece):
    return piece in BLACK_SET


# ==========================
#   PAWN MOVEMENT
# ==========================

def is_pawn_move_legal(board, from_sq, to_sq, piece):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    # White moves UP (toward row 0)
    if is_white_piece(piece):
        direction = -1
        start_rank = 6
    else:
        # Black moves DOWN (toward row 7)
        direction = 1
        start_rank = 1

    # Single forward
    if ff == tf and tr - fr == direction:
        if board[tr][tf] == " ":
            return True

    # Double forward
    if ff == tf and fr == start_rank and tr - fr == 2 * direction:
        mid = fr + direction
        if board[mid][tf] == " " and board[tr][tf] == " ":
            return True

    # Diagonal capture
    if abs(tf - ff) == 1 and tr - fr == direction:
        target = board[tr][tf]
        if target != " " and (is_white_piece(piece) != is_white_piece(target)):
            return True

    return False


# ==========================
#   ROOK MOVEMENT
# ==========================

def is_rook_move_legal(board, from_sq, to_sq, piece):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    if fr != tr and ff != tf:
        return False

    step_r = 0 if fr == tr else (1 if tr > fr else -1)
    step_f = 0 if ff == tf else (1 if tf > ff else -1)

    r, f = fr + step_r, ff + step_f

    while (r, f) != (tr, tf):
        if board[r][f] != " ":
            return False
        r += step_r
        f += step_f

    target = board[tr][tf]
    return target == " " or (is_white_piece(piece) != is_white_piece(target))


# ==========================
#   KNIGHT MOVEMENT
# ==========================

def is_knight_move_legal(board, from_sq, to_sq, piece):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    dr = abs(tr - fr)
    df = abs(tf - ff)

    if not ((dr == 2 and df == 1) or (dr == 1 and df == 2)):
        return False

    target = board[tr][tf]
    return target == " " or (is_white_piece(piece) != is_white_piece(target))


# ==========================
#   BISHOP MOVEMENT
# ==========================

def is_bishop_move_legal(board, from_sq, to_sq, piece):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    dr = tr - fr
    df = tf - ff

    if abs(dr) != abs(df):
        return False

    step_r = 1 if dr > 0 else -1
    step_f = 1 if df > 0 else -1

    r, f = fr + step_r, ff + step_f

    while (r, f) != (tr, tf):
        if board[r][f] != " ":
            return False
        r += step_r
        f += step_f

    target = board[tr][tf]
    return target == " " or (is_white_piece(piece) != is_white_piece(target))


# ==========================
#   QUEEN MOVEMENT
# ==========================

def is_queen_move_legal(board, from_sq, to_sq, piece):
    return (
        is_rook_move_legal(board, from_sq, to_sq, piece) or
        is_bishop_move_legal(board, from_sq, to_sq, piece)
    )


# ==========================
#   KING MOVEMENT
# ==========================

def find_king(board, white):
    king = WHITE_KING if white else BLACK_KING
    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return (r, c)
    return None


def is_king_move_legal(board, from_sq, to_sq, piece):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    dr = abs(tr - fr)
    df = abs(tf - ff)

    if dr > 1 or df > 1 or (dr == 0 and df == 0):
        return False

    target = board[tr][tf]
    return target == " " or (is_white_piece(piece) != is_white_piece(target))



# ==========================
#   ATTACK DETECTION
# ==========================

def is_square_attacked(board, row, col, by_white):
    # TEMPORARY placeholder so the program runs
    return False

def would_cause_self_check(board, from_sq, to_sq, white_to_move):
    # 1. Copy the board
    temp = [row[:] for row in board]

    (fr, ff) = from_sq
    (tr, tf) = to_sq
    piece = temp[fr][ff]

    # 2. Make the move on the temp board
    temp[tr][tf] = piece
    temp[fr][ff] = " "

    # 3. Find your king on the temp board
    king_pos = find_king(temp, white_to_move)
    if king_pos is None:
        return True  # Something is wrong; treat as illegal

    (kr, kc) = king_pos

    # 4. Check if your king is attacked
    return is_square_attacked(temp, kr, kc, not white_to_move)




# ==========================
#   MAIN MOVE FUNCTION
# ==========================

def make_move(board, from_sq, to_sq, white_to_move):
    (fr, ff) = from_sq
    (tr, tf) = to_sq

    piece = board[fr][ff]

    if piece == " ":
        print("There is no piece on that square.")
        return False, white_to_move

    # Turn enforcement
    if white_to_move and not is_white_piece(piece):
        print("It's White's turn. You must move a White piece.")
        return False, white_to_move

    if not white_to_move and not is_black_piece(piece):
        print("It's Black's turn. You must move a Black piece.")
        return False, white_to_move

    # Piece-specific rules
    if piece in WHITE_SET or piece in BLACK_SET:

        if piece in {"🨸","🨲"}:  # Pawn
            if not is_pawn_move_legal(board, from_sq, to_sq, piece):
                print("Illegal pawn move.")
                return False, white_to_move

        elif piece in {"🨳","🨭"}:  # Rook
            if not is_rook_move_legal(board, from_sq, to_sq, piece):
                print("Illegal rook move.")
                return False, white_to_move

        elif piece in {"🨴","🨮"}:  # Knight
            if not is_knight_move_legal(board, from_sq, to_sq, piece):
                print("Illegal knight move.")
                return False, white_to_move

        elif piece in {"🨵","🨯"}:  # Bishop
            if not is_bishop_move_legal(board, from_sq, to_sq, piece):
                print("Illegal bishop move.")
                return False, white_to_move

        elif piece in {"🨶","🨰"}:  # Queen
            if not is_queen_move_legal(board, from_sq, to_sq, piece):
                print("Illegal queen move.")
                return False, white_to_move

        elif piece in {"🨷","🨱"}:  # King
            if not is_king_move_legal(board, from_sq, to_sq, piece):
                print("Illegal king move.")
                return False, white_to_move

    #===========================#
    #       Self Check          #
    #===========================#

    if would_cause_self_check(board, from_sq, to_sq, white_to_move):
        print("Illegal move: your king would be in check.")
        return False, white_to_move
    
    #===========================#

    # Apply move
    board[tr][tf] = piece
    board[fr][ff] = " "

    return True, not white_to_move