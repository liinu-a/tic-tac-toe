from services.board import update_moves_to_evaluate, row_of_five
from services.evaluate import get_horizontal_val, get_vertical_val, get_downward_diag_val, get_upward_diag_val


class AI:
    """Class that manages the decition making of the AI.

    Attributes:
        moves_to_evaluate: The moves the AI evaluates and chooses the best one.
    """

    def __init__(self):
        self.moves_to_evaluate = []
        self.board_eval = 0

        self.updated_horizontals = set()
        self.horizontal_vals = [0] * 20

        self.updated_verticals = set()
        self.vertical_vals = [0] * 20

        self.updated_downward_diags = set()
        self.downward_diags_vals = {}

        self.updated_upward_diags = set()
        self.upward_diags_vals = {}

        for i in range(16):
            self.downward_diags_vals[(i, 0)] = 0
            self.downward_diags_vals[(0, i)] = 0
            self.upward_diags_vals[(i, 19)] = 0
            self.upward_diags_vals[(0, 19 - i)] = 0


    def decide_move(self, user_move, board):
        """Gets the move of the AI and reports the winner.

        Args:
            user_move ((int, int)): The row and column of the move to which the AI responds.
            board ([[int]]): The game board.

        Returns:
            (str, (int, int)): The winner and the square to be marked.
        """

        update_moves_to_evaluate(self.moves_to_evaluate, user_move, board)
        self.updated_rows(user_move)

        _, ai_move = self.minimax(
            board, self.moves_to_evaluate, 3, -100000000000, 100000000000, 1)

        update_moves_to_evaluate(self.moves_to_evaluate, ai_move, board)
        self.updated_rows(ai_move)

        return ai_move


    def minimax(self, board, moves_to_evaluate, depth, alpha, beta, turn):
        """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

        Returns:
            (int, (int, int)): The value of the optimal move and the move.
        """

        if depth == 0:
            return (self.evaluate(board, turn), None)

        if len(moves_to_evaluate) == 0:
            return (0, None)

        optimal = (100000000000 * turn * (-1), None)

        if turn == 1:
            for move in reversed(moves_to_evaluate):
                row, col = move
                board[row][col] = 1

                if row_of_five(board, move, 1):
                    board[row][col] = 0
                    return (1000000000, move)
                
                self.updated_rows(move)

                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, -1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    update_moves_to_evaluate(new_mvs_to_eval, move, board)

                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, -1)

                board[row][col] = 0
                self.updated_rows(move)

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
                    return (-1000000000, move)
                
                self.updated_rows(move)

                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, 1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    update_moves_to_evaluate(new_mvs_to_eval, move, board)

                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, 1)

                board[row][col] = 0
                self.updated_rows(move)

                if val < optimal[0]:
                    optimal = (val, move)
                beta = min(beta, val)

                if beta <= alpha:
                    break

        return optimal


    def updated_rows(self, move):
        row, col = move
        self.updated_horizontals.add(row)
        self.updated_verticals.add(col)

        x = min(row, col)
        start_of_diag = (row - x, col - x)
        if start_of_diag[0] <= 15 >= start_of_diag[1]:
            self.updated_downward_diags.add(start_of_diag)

        x = min(row, 19 - col)
        start_of_diag = (row - x, col + x)
        if start_of_diag[0] >= 4 and start_of_diag[1] <= 15:
            self.updated_upward_diags.add(start_of_diag)


    def evaluate(self, board, turn):
        value = 0
        for horiz_begin in self.updated_horizontals:
            value = get_horizontal_val(board, horiz_begin, turn)
            self.board_eval -= self.horizontal_vals[horiz_begin]
            self.board_eval += value
            self.horizontal_vals[horiz_begin] = value

        self.updated_horizontals = set()

        for vertc_begin in self.updated_verticals:
            value = get_vertical_val(board, vertc_begin, turn)
            self.board_eval -= self.vertical_vals[vertc_begin]
            self.board_eval += value
            self.vertical_vals[vertc_begin] = value

        self.updated_verticals = set()

        for diag_begin in self.updated_downward_diags:
            value = get_downward_diag_val(board, diag_begin, turn)
            self.board_eval -= self.downward_diags_vals[diag_begin]
            self.board_eval += value
            self.downward_diags_vals[diag_begin] = value

        self.updated_downward_diags = set()

        for diag_begin in self.updated_upward_diags:
            value = get_upward_diag_val(board, diag_begin, turn)
            self.board_eval -= self.upward_diags_vals[diag_begin]
            self.board_eval += value
            self.upward_diags_vals[diag_begin] = value

        self.updated_upward_diags = set()

        return self.board_eval

