class Board():
    def __init__(self):
        self.board = [[0 for _ in range(20)] for _ in range(20)]
        self.board_vertical = [[0 for _ in range(20)] for _ in range(20)]
        self.board_downward_diag = []
        self.board_upward_diag = []

        for i in range(1, 21):
            self.board_downward_diag.append([0] * i)
            self.board_upward_diag.append([0] * i)
        for i in range(19, 0, -1):
            self.board_downward_diag.append([0] * i)
            self.board_upward_diag.append([0] * i)


    def mark_board(self, move, player):
        row, col = move
        self.board[row][col] = player
        self.board_vertical[col][row] = player

        row_diag = 19 + row - col
        self.board_downward_diag[row_diag][col if row_diag > 19 else row] = player

        row_diag = row + col
        self.board_upward_diag[row_diag][19 - col if row_diag > 19 else row] = player


    def row_of_five(self, contains_move, player):
        """Determines if there is a row of five containing the given move.

        Args:
            contains_move ((int, int)): The move included in the row.
            player (int): Which player's row.

        Returns:
            Bool: True if row of five is found else False.
        """

        row, col = contains_move

        if self.check_row_of_five(row, col, self.board, player):
            return True
        if self.check_row_of_five(col, row, self.board_vertical, player):
            return True

        row_diag = 19 + row - col
        col_diag = col if row_diag > 19 else row

        if self.check_row_of_five(row_diag, col_diag, self.board_downward_diag, player):
            return True

        row_diag = row + col
        col_diag = 19 - col if row_diag > 19 else row

        if self.check_row_of_five(row_diag, col_diag, self.board_upward_diag, player):
            return True

        return False


    def check_row_of_five(self, row, col, board, player):
        count = 1
        right_col = col + 1
        while right_col < len(board[row]) and board[row][right_col] == player:
            right_col += 1
            count += 1
            if count >= 5:
                return True

        left_col = col - 1
        while left_col >= 0 and board[row][left_col] == player:
            left_col -= 1
            count += 1
            if count >= 5:
                return True

        return False


    def collect_moves_to_evaluate(self, move):
        """Creates a list of free squares at most two squares away from a move.

        Args:
            board ([[int]]): The game board.
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
                and self.board[row][col] == 0
            )
        ]

        return valid_moves
