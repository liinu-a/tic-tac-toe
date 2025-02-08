from services.board import row_of_five, evaluate, update_moves_to_evaluate


class AI:
    """Class that manages the decition making of the AI.

    Attributes:
        moves_to_evaluate: The moves the AI evaluates and chooses the best one.
    """

    def __init__(self):
        self.moves_to_evaluate = []

    def decide_move(self, user_move, board):
        """Gets the move of the AI and reports the winner.

        Args:
            user_move ((int, int)): The row and column of the move to which the AI responds.
            board ([[int]]): The game board.

        Returns:
            (str, (int, int)): The winner and the square to be marked.
        """

        update_moves_to_evaluate(self.moves_to_evaluate, user_move, board)

        optimal = _, ai_move = self.minimax(
            board, self.moves_to_evaluate, user_move, 4, -1000000, 1000000, 1)

        match optimal:
            case (4, _):
                return ("O", ai_move)
            case (-5, _):
                return ("X", (-1, -1))
            case (0, (-1, -1)):
                return ("tie", (-1, -1))

        update_moves_to_evaluate(self.moves_to_evaluate, ai_move, board)

        if len(self.moves_to_evaluate) == 0:
            return ("tie", ai_move)

        return ("none", ai_move)

    def minimax(self, board, moves_to_evaluate, previous_move, depth, alpha, beta, turn):
        """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

        Returns:
            (int, (int, int)): The value of the optimal move and the move.
        """

        if row_of_five(board, previous_move, (-1) * turn):
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

                val, _ = self.minimax(board, new_mvs_to_eval, move, depth - 1, alpha, beta, -1)

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

                val, _ = self.minimax(board, new_mvs_to_eval, move, depth - 1, alpha, beta, 1)

                board[row][col] = 0

                if val < optimal[0]:
                    optimal = (val, move)
                beta = min(beta, val)

                if beta <= alpha:
                    break

        return optimal
