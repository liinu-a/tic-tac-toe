class Moves_list:
    """Class that manages the list of potential moves.

    Attributes:
        moves: List that contains the potential moves as tuples (row, column). 
        index_table: Table that contains the indexes of the grid spaces in moves. 
                     If a space is not in moves, the index is -1.
    """

    def __init__(self):
        self.moves = []
        self.index_table = [[-1 for _ in range(20)] for _ in range(20)]

    
    def remove(self, r, c):
        """Removes a space from moves.

        Does nothing if the space is not in moves.

        Args:
            r (int): The row of the space.
            c (int): The column of the space.
        """

        idx_in_moves = self.index_table[r][c]

        if idx_in_moves == -1: return

        last = row, col = self.moves.pop()
        self.index_table[r][c] = -1

        if last == (r, c): return

        self.moves[idx_in_moves] = last
        self.index_table[row][col] = idx_in_moves

    
    def add_moves(self, moves_to_add):
        """Adds moves to the list of potential moves.

        If a move is alrady in the list, it gets moved towards the end of the list.

        Else the move is appended to the end of the list.

        Args:
            moves_to_add ([(int, int)]): List of valid moves to be added to potential moves.
        """

        i = len(self.moves) - 1

        for move in moves_to_add:
            row, col = move
            idx_in_moves = self.index_table[row][col]

            if idx_in_moves == -1:
                self.moves.append(move)
                self.index_table[row][col] = len(self.moves) - 1
                continue

            swap_pos_with = r, c = self.moves[i]

            self.moves[i], self.moves[idx_in_moves] = move, swap_pos_with
            self.index_table[row][col], self.index_table[r][c] = i, idx_in_moves

            i -= 1
