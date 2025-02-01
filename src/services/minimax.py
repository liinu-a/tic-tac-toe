from .board import row_of_five, evaluate, update_moves_to_evaluate


def minimax(board, moves_to_evaluate, previous_move, depth, alpha, beta, turn):
    """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

    Returns:
        (int, (int, int)): The value of the optimal move and the move.
    """

    if row_of_five(board, previous_move):
        value = -1 - depth if turn == 1 else 1 + depth
        return (value, (-1, -1))

    if len(moves_to_evaluate) == 0:
        return (0, (-1, -1))

    if depth == 0:
        return (evaluate(board), (-1, -1))

    optimal = (1000000 * turn * (-1), (-1, -1))

    if turn == 1:
        for move in reversed(moves_to_evaluate):
            row, col = move
            board[row][col] = 1

            new_mvs_to_eval = moves_to_evaluate[:]
            update_moves_to_evaluate(new_mvs_to_eval, move, board)

            val, _ = minimax(board, new_mvs_to_eval, move, depth - 1, alpha, beta, -1)

            board[row][col] = 0

            if val > optimal[0]:
                optimal = (val, move)
            alpha = max(alpha, val)

            if beta <= alpha:
                break

    else:
        for move in reversed(moves_to_evaluate):
            row, col = move
            board[row][col] = -1

            new_mvs_to_eval = moves_to_evaluate[:]
            update_moves_to_evaluate(new_mvs_to_eval, move, board)

            val, _ = minimax(board, new_mvs_to_eval, move, depth - 1, alpha, beta, 1)

            board[row][col] = 0

            if val < optimal[0]:
                optimal = (val, move)
            beta = min(beta, val)

            if beta <= alpha:
                break

    return optimal
