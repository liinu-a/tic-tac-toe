import tkinter as tk
from tkinter import Button
import functools


class Game:
    """Class, which manages the game.

    Attributes:
        turn: Indicates, whose turn it is. True -> X's and False -> O's.
        root: The root window of the game.
        spaces: List of spaces (represented as buttons) of the grid.
    """

    def __init__(self):
        self.turn = True


    def _build_gui(self):
        """Builds a Tkinter GUI for the game.
        """

        self.root = tk.Tk()
        self.root.title("Tic-tac-toe")

        self.spaces = [
            Button(self.root, text=" ", width=2, height=1, bg="white",
                   command=functools.partial(self._mark_space, i))
            for i in range(400)
        ]

        count = 0
        for r in range(20):
            for c in range(20):
                self.spaces[count + c].grid(row=r, column=c)
            count += 20


    def start(self):
        """Starts the game.
        """

        self._build_gui()
        self.root.mainloop()


    def _mark_space(self, i):
        """Marks the chosen space on the grid if free and switches whose turn it is.

        Args:
            i (int): The index of the space.
        """

        space = self.spaces[i]

        if space["text"] != " ":
            return

        space["text"] = "X" if self.turn else "O"
        self.turn = not self.turn


    def check_for_win(self):
        pass
