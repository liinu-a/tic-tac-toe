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
        self.downward_diags_vals = [0] * 39

        self.updated_upward_diags = set()
        self.upward_diags_vals = [0] * 39


    def decide_move(self, user_move, board):
        """Gets the move of the AI and reports the winner.

        Args:
            user_move ((int, int)): The row and column of the move to which the AI responds.
            board ([[int]]): The game board.

        Returns:
            (int, (int, int)): 
        """

        self.update_moves_to_evaluate(self.moves_to_evaluate, user_move, board)
        self.updated_rows(user_move)

        _, ai_move = self.minimax(
            board, self.moves_to_evaluate, 4, -100000000000, 100000000000, 1)

        self.update_moves_to_evaluate(self.moves_to_evaluate, ai_move, board)
        self.updated_rows(ai_move)

        return ai_move


    def update_moves_to_evaluate(self, moves_to_evaluate, move_made, board):
        """Updates the list of moves that are evaluated in minimax.

        Args:
            made_move ((int, int)): The move that was made.
            board ([[int]]): The game board.
        """

        try:
            moves_to_evaluate.remove(move_made)
        except ValueError:
            pass

        moves = board.collect_moves_to_evaluate(move_made)

        for move in moves:
            try:
                moves_to_evaluate.append(
                    moves_to_evaluate.pop(
                        moves_to_evaluate.index(move)
                    )
                )
            except ValueError:
                moves_to_evaluate.append(move)


    def minimax(self, board, moves_to_evaluate, depth, alpha, beta, turn):
        """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

        Returns:
            (int, (int, int)): The value of the optimal move and the move.
        """

        if len(moves_to_evaluate) == 0:
            return (0, None)

        if depth == 0:
            return (self.evaluate(board, turn), None)

        optimal = (100000000000 * turn * (-1), None)

        if turn == 1:
            for move in reversed(moves_to_evaluate):
                board.mark_board(move, 1)

                if board.row_of_five(move, 1):
                    board.mark_board(move, 0)
                    return (1000000000, move)

                self.updated_rows(move)

                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, -1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    self.update_moves_to_evaluate(new_mvs_to_eval, move, board)
                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, -1)

                board.mark_board(move, 0)
                self.updated_rows(move)

                if val > optimal[0]:
                    optimal = (val, move)
                alpha = max(alpha, val)

                if beta <= alpha:
                    break
        else:
            for move in reversed(moves_to_evaluate):
                board.mark_board(move, -1)

                if board.row_of_five(move, -1):
                    board.mark_board(move, 0)
                    return (-1000000000, move)
                
                self.updated_rows(move)

                val = None
                if depth == 1:
                    val, _ = self.minimax(board, moves_to_evaluate, depth - 1, alpha, beta, 1)
                else:
                    new_mvs_to_eval = moves_to_evaluate[:]
                    self.update_moves_to_evaluate(new_mvs_to_eval, move, board)
                    val, _ = self.minimax(board, new_mvs_to_eval, depth - 1, alpha, beta, 1)

                board.mark_board(move, 0)
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

        row_diag = 19 + row - col
        if 4 <= row_diag <= 34:
            self.updated_downward_diags.add(row_diag)

        row_diag = row + col
        if 4 <= row_diag <= 34:
            self.updated_upward_diags.add(row_diag)


    def evaluate(self, board, turn):
        value = 0
        for row in self.updated_horizontals:
            value = self.get_row_val(board.board[row], turn)
            self.board_eval -= self.horizontal_vals[row]
            self.board_eval += value
            self.horizontal_vals[row] = value

        self.updated_horizontals = set()

        for row in self.updated_verticals:
            value = self.get_row_val(board.board_vertical[row], turn)
            self.board_eval -= self.vertical_vals[row]
            self.board_eval += value
            self.vertical_vals[row] = value

        self.updated_verticals = set()

        for row in self.updated_downward_diags:
            value = self.get_row_val(board.board_downward_diag[row], turn)
            self.board_eval -= self.downward_diags_vals[row]
            self.board_eval += value
            self.downward_diags_vals[row] = value

        self.updated_downward_diags = set()

        for row in self.updated_upward_diags:
            value = self.get_row_val(board.board_upward_diag[row], turn)
            self.board_eval -= self.upward_diags_vals[row]
            self.board_eval += value
            self.upward_diags_vals[row] = value

        self.updated_upward_diags = set()

        return self.board_eval


    def get_row_val(self, row, cur_turn):
        start_col = end_col = 0
        count = value = 0
        last = -1
        player = None
        values = {
            2: 1,
            3: 20,
            4: 10000
        }

        while end_col < len(row) and row[end_col] == 0:
            end_col += 1

        if end_col == len(row):
            return 0

        player = row[end_col]
        start_col = 0 if end_col <= 4 else end_col - 4

        while end_col < len(row):
            if row[end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last >= start_col:
                    start_col = last + 1

            if row[end_col] == player:
                count += 1
                last = end_col

            if end_col - start_col == 4:
                if count == 4:
                    if player == cur_turn:
                        return 100000000 * cur_turn

                if count > 1:
                    value += values[count] * player

                count -= abs(row[start_col])
                start_col += 1
            end_col += 1

        return value

