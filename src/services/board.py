def collect_moves_to_evaluate(board, move):
    """Creates a list of free squares at most two squares away from a move.

    Args:
        board ([[int]]): The board that shows which squares are free.
        move ((int, int)): The move around which the squares are collected.

    Returns:
        [(int, int)]: The list of squares, represented by their coordinates on the board (row, column).
    """

    r, c = move
    rp, rpp, rm, rmm = r + 1, r + 2, r - 1, r - 2
    cp, cpp, cm, cmm = c + 1, c + 2, c - 1, c - 2

    valid_moves = [
        (row, col) for row, col in [
            (rmm, cmm), (rmm, cpp), (rpp, cmm), (rpp, cpp), (rmm, c), (r, cmm), (r, cpp), (rpp, c),
            (rm, cm), (rm, cp), (rp, cm), (rp, cp), (rm, c), (r, cm), (r, cp), (rp, c)
        ]
        if (
            0 <= row < 20 > col >= 0
            and board[row][col] == 0
        )
    ]

    return valid_moves

def update_moves_to_evaluate(moves_to_evaluate, move_made, board):
    """Updates the list of moves that are evaluated in minimax.

    Args:
        moves_to_evaluate ([(int, int)]): The list containing the moves to be evaluated.
        made_move ((int, int)): The move that was made.
        board ([[int]]): The game board.
    """

    try:
        moves_to_evaluate.remove(move_made)
    except ValueError:
        pass

    moves = collect_moves_to_evaluate(board, move_made)

    for move in moves:
        try:
            moves_to_evaluate.append(
                moves_to_evaluate.pop(
                    moves_to_evaluate.index(move)
                )
            )
        except ValueError:
            moves_to_evaluate.append(move)

def row_of_five(board, includes_move):
    row, col = includes_move
    player = board[row][col]
    count = 1

    row += 1
    while row < 20 and board[row][col] == player:
        row += 1
        count += 1
        if count >= 5:
            return True
    row = includes_move[0] - 1
    while row >= 0 and board[row][col] == player:
        row -= 1
        count += 1
        if count >= 5:
            return True

    count = 1

    row = includes_move[0]
    col += 1
    while col < 20 and board[row][col] == player:
        col += 1
        count += 1
        if count >= 5:
            return True
    col = includes_move[1] - 1
    while col >= 0 and board[row][col] == player:
        col -= 1
        count += 1
        if count >= 5:
            return True

    count = 1

    row += 1
    col = includes_move[1] + 1
    while col < 20 > row and board[row][col] == player:
        row += 1
        col += 1
        count += 1
        if count >= 5:
            return True
    row = includes_move[0] - 1
    col = includes_move[1] - 1
    while col >= 0 <= row and board[row][col] == player:
        row -= 1
        col -= 1
        count += 1
        if count >= 5:
            return True

    count = 1

    row = includes_move[0] + 1
    col = includes_move[1] - 1
    while 0 <= col and 20 > row and board[row][col] == player:
        row += 1
        col -= 1
        count += 1
        if count >= 5:
            return True
    row = includes_move[0] - 1
    col = includes_move[1] + 1
    while col < 20 and 0 <= row and board[row][col] == player:
        row -= 1
        col += 1
        count += 1
        if count >= 5:
            return True

    return False


def evaluate(board):
    return 0
