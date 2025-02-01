from services.minimax import minimax
from services.board import update_moves_to_evaluate


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
            board ([[int]]): Used to calculate which square the AI can and should mark.

        Returns:
            (str, (int, int)): The winner and the square to be marked.
        """

        update_moves_to_evaluate(self.moves_to_evaluate, user_move, board)

        optimal = _, ai_move = minimax(
            board, self.moves_to_evaluate, user_move, 4, -1000000, 1000000, 1)

        match optimal:
            case (4, _):
                return ("O", ai_move)
            case (-5, _):
                return ("X", (-1, -1))
            case (0, (-1, -1)):
                return ("tie", (-1, -1))

        update_moves_to_evaluate(self.moves_to_evaluate, ai_move, board)

        if len(self.moves_to_evaluate) == 0:
            return ("tie", ai_move)

        return ("none", ai_move)
