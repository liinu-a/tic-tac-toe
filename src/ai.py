from services.board import update_moves_to_evaluate, row_of_five
from services.evaluate import evaluate


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

        _, ai_move = self.minimax(
            board, self.moves_to_evaluate, 3, -1000000000, 1000000000, 1)

        update_moves_to_evaluate(self.moves_to_evaluate, ai_move, board)

        return ai_move


    def minimax(self, board, moves_to_evaluate, depth, alpha, beta, turn):
        """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

        Returns:
            (int, (int, int)): The value of the optimal move and the move.
        """

        if depth == 0:
            return (evaluate(board, turn), None)

        if len(moves_to_evaluate) == 0:
            return (0, None)

        optimal = (1000000000 * turn * (-1), None)

        if turn == 1:
            for move in reversed(moves_to_evaluate):
                row, col = move
                board[row][col] = 1

                if row_of_five(board, move, 1):
                    board[row][col] = 0
                    return (10000000, move)
                
                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, -1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    update_moves_to_evaluate(new_mvs_to_eval, move, board)

                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, -1)

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

                if row_of_five(board, move, -1):
                    board[row][col] = 0
                    return (-10000000, move)

                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, 1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    update_moves_to_evaluate(new_mvs_to_eval, move, board)

                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, 1)

                board[row][col] = 0

                if val < optimal[0]:
                    optimal = (val, move)
                beta = min(beta, val)

                if beta <= alpha:
                    break

        return optimal
