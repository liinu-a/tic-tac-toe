import tkinter as tk
from tkinter import Button
from ai import AI
import functools


class Game:
    """Class that manages the game.

    Attributes:
        turn: Indicates, whose turn it is. True -> X's and False -> O's.
        root: The root window of the game.
        grid: The grid, where the spaces are represented as buttons.
    """

    def __init__(self):
        self.turn = True
        self.player_O = AI()


    def _build_gui(self):
        """Builds a Tkinter GUI for the game.
        """

        self.root = tk.Tk()
        self.root.title("Tic-tac-toe")

        self.grid = [
            [
                Button(self.root, text=" ", width=2, height=1, bg="white",
                   command=functools.partial(self._mark_space, r, c))
                for c in range(20)
            ]
            for r in range(20)
        ]

        for i, grid_row in enumerate(self.grid):
            for j, space in enumerate(grid_row):
                space.grid(row=i, column=j)


    def start(self):
        """Starts the game.
        """

        self._build_gui()
        self.root.mainloop()


    def _mark_space(self, r, c):
        """Marks the chosen grid space if free and switches whose turn it is.

        Args:
            r (int): The grid row.
            c (int): The grid column.
        """

        space = self.grid[r][c]

        if space["text"] != " ":
            return

        space["text"] = "X" if self.turn else "O"
        self.turn = not self.turn

        """ 
        space["text"] = "X"

        player_O.decide_move((r, c))

        """
