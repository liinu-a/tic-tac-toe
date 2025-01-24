from moves_list import Moves_list

class AI:
    """Class that manages the gameplay of the AI.

    Attributes:
        potential_moves: Contains potential next moves based on previously made moves by either player.
        grid: 20x20 grid, where -1 indicates space marked by the user, 1 by the AI and 0 is free.
    """

    def __init__(self):
        self.potential_moves = Moves_list()
        self.grid = [[0 for _ in range(20)] for _ in range(20)]

    
    def mark_space(self, player, r, c):
        """Marks a space in the grid.

        Args:
            player (int): Is either 1 or -1.
            r (int): The row of the space.
            c (int): The column of the space.
        """

        self.grid[r][c] = player


    def get_free_valid_spaces(self, r, c):
        """Generates a list of free spaces that are at most two spaces away from the given space and within the grid.

        Args:
            r (int): The row of the given space.
            c (int): The column of the given space.

        Returns:
            [(int, int)]: A list of tuples (row, column) representing the spaces.
        """

        spaces = [(row, col) for row, col in [
            (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1),
            (r-2, c-2), (r-2, c), (r-2, c+2), (r, c-2), (r, c+2), (r+2, c-2), (r+2, c), (r+2, c+2)
            ] if row >= 0 and row < 20 and col >= 0 and col < 20 and self.grid[row][col] == 0]

        return spaces
    

    def choose_move(self, r, c):
        """The AI chooses its next move in response to the user having made a move.

        Args:
            r (int): The row of the move made by the user.
            c (int): The column of the move made by the user.
        """

        self.mark_space(-1, r, c)
