# Project specification
Degree programme: Bachelor of Computer Science (BCS).

The main objective of this project is to implement an AI for tic-tac-toe. Two players, X and O, take turns marking the spaces in a twenty-by-twenty grid and the first to place at least five of their marks in a vertical, horizontal or diagonal row wins.

The AI will be implemented by using the minimax algorithm with alpha-beta pruning. When the AI decides on its next move, only the free spaces up to two spaces away from the previous moves will be considered as those will have more immediate impact on the game state. A list of these kinds of spaces will be maintained, which will get updated whenever a move is made. Also, as moves are being examined an updated versio of the list will be forwarded as an argument to minimax. This way there is no need to figure out every single move to be examined every time it is the AI's turn. 

The AI will follow a heuristic in which the spaces closest to the previous move made by the user will be evaluated first. Additionally, whenever the program checks for a winner, only the rows that include the previous move will be examined.

In the worst case scenario, the time complexity of the minimax algorithm with alpha-beta pruning is O(b^k), where b is the branching factor and k is the depth of the search tree. The branching factor b is not an exact number and varies depending on the amount moves to be examined.

## Interface
The user provides input to the program by interacting with a GUI implemented with Tkinter. The game grid is created by placing buttons in such a way, that they form the grid spaces / squares. These buttons or spaces are stored in a list. On their turn, the user can mark a free space (a button with no text) by clicking it. This action will trigger a function, which will recieve the index of the space as an argument. 

## Info for the course
The code and documentation are written in english. The programming language chosen for this project is Python. I should be able to understand Python and JavaScript to such an extent that I can peer review projects written in them.

## Sources
Implementing the GUI with Tkinter
- https://www.youtube.com/watch?v=xx0qmpuA-vM
- https://ohjelmistotekniikka-hy.github.io/python/tkinter

Minimax algorithm with alpha-beta pruning
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning