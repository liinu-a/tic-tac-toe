class Board():
    """A class for the board that is used for calculations.

    Attributes:
        board: The main board/the horizontal rows of the board.
        board_vertical: The vertical rows of the board.
        board_downward_diag: The downward diagonal rows of the board.
        board_upward_diag: The upward diagonal rows of the board.
    """

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


    def mark_board(self, square, val):
        """Marks the board and its variations with a value.

        Args:
            square ((int, int)): The square to be marked.
            val (int): The value the square gets marked with, either -1, 0 or 1.
        """

        row, col = square
        self.board[row][col] = val
        self.board_vertical[col][row] = val

        row_diag = 19 + row - col
        self.board_downward_diag[row_diag][col if row_diag > 19 else row] = val

        row_diag = row + col
        self.board_upward_diag[row_diag][19 - col if row_diag > 19 else row] = val


    def row_of_five(self, contains_move, player):
        """Determines whether a player has gotten a row of five that includes a given move.

        Args:
            contains_move ((int, int)): The move included in the row.
            player (int): The player whose row it should be.

        Returns:
            Bool: True if row of five is found else False.
        """

        row, col = contains_move
        if self.check_row_of_five(col, self.board[row], player):
            return True
        if self.check_row_of_five(row, self.board_vertical[col], player):
            return True

        row_diag = 19 + row - col
        col_diag = col if row_diag > 19 else row
        if self.check_row_of_five(col_diag, self.board_downward_diag[row_diag], player):
            return True

        row_diag = row + col
        col_diag = 19 - col if row_diag > 19 else row
        if self.check_row_of_five(col_diag, self.board_upward_diag[row_diag], player):
            return True

        return False


    def check_row_of_five(self, col, row, player):
        """Checks a single row to determine if a player has gotten a row of five that contains 
        a move that occupies the given column.

        Args:
            row ([int]): The row to be checked of the board.
            col (int): The column of the square that must be included in the row of five.
            player (int): The player whose row of five it should be.

        Returns:
            Bool: True if found else False.
        """

        count = 1
        right = col + 1
        while right < len(row) and row[right] == player:
            right += 1
            count += 1
            if count >= 5:
                return True

        left = col - 1
        while left >= 0 and row[left] == player:
            left -= 1
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
            [(int, int)]: The list of squares, represented by their coordinates on the board.
        """

        r, c = move
        rp, rpp, rm, rmm = r + 1, r + 2, r - 1, r - 2
        cp, cpp, cm, cmm = c + 1, c + 2, c - 1, c - 2

        valid_moves = [
            (row, col) for row, col in [
                (rmm, cmm), (rmm, cpp), (rpp, cmm), (rpp, cpp), (rmm, c), (r, cmm), (r, cpp), (rpp, c),
                (rm, cm), (rm, cp), (rp, cm), (rp, cp), (rm, c), (r, cm), (r, cp), (rp, c)
            ]
            if 0 <= row < 20 > col >= 0 and self.board[row][col] == 0
        ]

        return valid_moves
