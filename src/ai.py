import time


class AI:
    """Class that manages the decition making of the AI.

    Attributes:
        moves_to_evaluate: The moves the AI evaluates and chooses the best one.
    """

    def __init__(self):
        self.moves_to_evaluate = []
        self.board_eval = 0
        self.table = {}

        self.updated_horizontals = set()
        self.horizontal_vals = [0] * 20

        self.updated_verticals = set()
        self.vertical_vals = [0] * 20

        self.updated_downward_diags = set()
        self.downward_diags_vals = [0] * 39

        self.updated_upward_diags = set()
        self.upward_diags_vals = [0] * 39


    def decide_move(self, user_move, board):
        self.update_moves_to_evaluate(self.moves_to_evaluate, user_move, board)
        self.updated_rows(user_move)

        best_val, best_move = 0, None
        self.depth = 1
        self.time_expired = False
        self.time_start = time.time()

        while time.time() - self.time_start < 2 or self.depth < 4:
            val, move = self.minimax(
                board, self.moves_to_evaluate, self.depth, -1000000000000, 1000000000000, 1, "")
            
            if self.time_expired:
                break

            best_val, best_move = val, move
            self.moves_to_evaluate.append(
                self.moves_to_evaluate.pop(
                    self.moves_to_evaluate.index(move)
                )
            )
            self.depth += 1
        
        self.update_moves_to_evaluate(self.moves_to_evaluate, best_move, board)
        self.updated_rows(best_move)
        self.table = {}

        return best_val, best_move


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


    def minimax(self, board, moves_to_evaluate, depth, alpha, beta, turn, table_key):
        """Finds the optimal move. An implementation of the minimax algorithm with alpha-beta pruning.

        Returns:
            (int, (int, int)): The value of the optimal move and the move.

        """

        if self.table.get(table_key) is None:
            self.table[table_key] = None

        last_best_move = self.table[table_key]

        if last_best_move:
            moves_to_evaluate.append(
                moves_to_evaluate.pop(
                    moves_to_evaluate.index(last_best_move)
                )
            )

        optimal = (1000000000000 * turn * (-1), None)

        if turn == 1:
            for move in reversed(moves_to_evaluate):
                if time.time() - self.time_start >= 2 and self.depth > 4:
                    self.time_expired = True
                    return (0, None)

                board.mark_board(move, 1)

                if board.row_of_five(move, 1):
                    self.table[table_key] = move
                    board.mark_board(move, 0)
                    return (100000000000, move)

                val = 0
                if len(moves_to_evaluate) > 1:
                    self.updated_rows(move)
                    
                    if depth == 1:
                        val = self.evaluate(board, -1)
                    else:
                        new_moves_to_evaluate = moves_to_evaluate[:]
                        self.update_moves_to_evaluate(new_moves_to_evaluate, move, board)
                        new_table_key = self.get_table_key(table_key, "+", f"{move[0]:02d}", f"{move[1]:02d}")
                        val, _ = self.minimax(
                            board, new_moves_to_evaluate, depth - 1, alpha, beta, -1, new_table_key)
                    
                    self.updated_rows(move)

                board.mark_board(move, 0)

                if val > optimal[0]:
                    optimal = (val, move)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
        else:
            for move in reversed(moves_to_evaluate):
                if time.time() - self.time_start >= 2 and self.depth > 4:
                    self.time_expired = True
                    return (0, None)
                
                board.mark_board(move, -1)

                if board.row_of_five(move, -1):
                    self.table[table_key] = move
                    board.mark_board(move, 0)
                    return (-100000000000, move)

                val = 0
                if len(moves_to_evaluate) > 1:
                    self.updated_rows(move)
                    
                    if depth == 1:
                        val = self.evaluate(board, 1)
                    else:
                        new_moves_to_evaluate = moves_to_evaluate[:]
                        self.update_moves_to_evaluate(new_moves_to_evaluate, move, board)
                        new_table_key = self.get_table_key(table_key, "-", f"{move[0]:02d}", f"{move[1]:02d}")
                        val, _ = self.minimax(
                            board, new_moves_to_evaluate, depth - 1, alpha, beta, 1, new_table_key)
                    
                    self.updated_rows(move)

                board.mark_board(move, 0)

                if val < optimal[0]:
                    optimal = (val, move)
                beta = min(beta, val)
                if beta <= alpha:
                    break

        self.table[table_key] = optimal[1]
        return optimal


    def get_table_key(self, prev_key, player, row, col):
        tb_key = ""
        for i in range(1, len(prev_key), 5):
            if prev_key[i:i + 2] == row:
                for j in range(i + 2, len(prev_key), 5):
                    if prev_key[j:j + 2] > col or prev_key[j - 2:j] > row:
                        break
                    tb_key += prev_key[j - 3:j + 2]
                break

            if prev_key[i:i + 2] > row:
                break
            tb_key += prev_key[i - 1:i + 4]

        tb_key += player + row + col + prev_key[len(tb_key): ]
        return tb_key


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

