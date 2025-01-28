class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(20)] for _ in range(20)]


    def apply_move(self, move, player):
        row, col = move
        self.grid[row][col] = player


    def remove_move(self, move):
        row, col = move
        self.grid[row][col] = 0

    
    def get_valid_moves(self, move):
        r, c = move

        valid_moves = [
            (row, col) for row, col in [
                (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1),
                (r-2, c-2), (r-2, c), (r-2, c+2), (r, c-2), (r, c+2), (r+2, c-2), (r+2, c), (r+2, c+2)
            ] 
            if (
                row >= 0 
                and row < 20 
                and col >= 0 
                and col < 20 
                and self.grid[row][col] == 0
            )
        ]

        return valid_moves
    
    
    def row_of_five(self, move):
        pass