from grid import Grid
from services.minimax import minimax

class AI:
    """Class that manages the gameplay of the AI.

    Attributes:
        
    """

    def __init__(self):
        self.grid = Grid()
        self.moves_to_evaluate = []


    def decide_move(self, user_move):
        self.grid.apply_move(user_move, -1)

        """
        minimax(self.grid, self.moves_to_evaluate, user_move, 0, -1, 1, 1)

        self.grid.apply_move(ai_move, 1)
        """
