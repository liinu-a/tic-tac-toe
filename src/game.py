from tkinter import Button, DISABLED, NORMAL, messagebox
import functools
from ai import AI
from board import Board


class Game:
    """Class that manages the gameplay.

    Attributes:
        root: The root window of the game.
        board_gui: The GUI board.
        count: A count of how many moves have been made thus far.
        player_o: The AI.
        board: The board used in calculations.
    """

    def __init__(self, root):
        self.root = root
        self.board_gui = []
        self.count = 0
        self.player_o = AI()
        self.board = Board()


    def start(self):
        """Builds the GUI of the game.
        """

        self.board_gui = [
            [
                Button(self.root, text=" ", width=2, height=1, bg="white",
                       command=functools.partial(self.make_move, row, col))
                for col in range(20)
            ]
            for row in range(20)
        ]

        for i, board_row in enumerate(self.board_gui):
            for j, square in enumerate(board_row):
                square.grid(row=i, column=j)

        reset = Button(self.root, text="RESET", command=self.reset)
        reset.grid(row=20, column=0, columnspan=2)


    def make_move(self, x_row, x_col):
        """Responds to the user making a move (player X).

        Args:
            x_row (int): The row of the user's move.
            x_col (int): The column of the user's move.
        """

        square = self.board_gui[x_row][x_col]

        if square["text"] != " ":
            return

        square["text"] = "X"
        self.root.update_idletasks()
        self.board.mark_board((x_row, x_col), -1)
        self.count += 1

        if self.board.row_of_five((x_row, x_col), -1):
            self.game_ended("Player X wins!")
            return
        
        if self.count == 400:
            self.game_ended("It's a tie!")
            return

        _, (o_row, o_col) = self.player_o.decide_move((x_row, x_col), self.board)

        self.board_gui[o_row][o_col]["text"] = "O"
        self.board.mark_board((o_row, o_col), 1)
        self.count += 1

        if self.board.row_of_five((o_row, o_col), 1):
            self.game_ended("Player O wins!")
            return
        
        if self.count == 400:
            self.game_ended("It's a tie!")


    def game_ended(self, message):
        """Prevents the user from making moves once the game ends. 
        
        Displays a message about how the game concluded.

        Args:
            message (str): Announces either the winner or a tie.
        """

        for row in self.board_gui:
            for square in row:
                square.config(state=DISABLED)

        messagebox.showinfo("The game has ended.", message)


    def reset(self):
        """Resets the game.
        """

        self.player_o = AI()
        self.board = Board()

        for row in self.board_gui:
            for square in row:
                square["text"] = " "
                square.config(state=NORMAL)
