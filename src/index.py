from tkinter import Tk
from game import Game

window = Tk()
window.title("Tic-tac-toe")
window.resizable(False, False)

tic_tac_toe = Game(window)
tic_tac_toe.start()

window.mainloop()
