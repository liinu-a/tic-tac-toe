# Implementation document

## Project structure

### Classes and helper functions

#### Game
The game class builds and handles the GUI and takes care of user interaction. It receives input from the user, to which it then gets a response from the AI. It additionally handles the state of the game, i.e., has the game ended, does the user request the game to be restarted.

#### AI
The AI class handles the decision making of the AI.

#### minimax
The minimax algorithm is a method of the AI class and used to calculate the next move of the AI. The minimax algorithm is optimized with alpha-beta pruning and explores only the moves at most two spaces away from the previous moves. The order of exploration is based on how recent the previous move is. In the worst case scenario, the time complexity of the minimax algorithm with alpha-beta pruning is O(b^k), where b is the branching factor and k is the depth of the search tree. The branching factor b is not an exact number and varies depending on the amount moves to be evaluated.

#### collect_moves_to_evaluate
A function that collects the free squares at most two squares away from a given move on the board. The time complexity is O(1), as the function checks which of the 16 squares are valid.

#### update_moves_to_evaluate
A function that updates the list of moves to be evaluated in the minimax algorithm with the moves it gets by calling the collect_moves_to_evaluate function. Moves, which are already present in the list are moved to the end and the nonpresent ones appended to the end of the list. Thus, minimax explores the list in reverse order. Also, removes the preceding move that triggered the update from the list. 

#### row_of_five
When given a move, the function checks for a vertical, horizontal or diagonal row of five that contains the move.

## Use of LLMs
No LLMs have been used in this project.

## Sources
Implementing the GUI with Tkinter
- https://www.youtube.com/watch?v=xx0qmpuA-vM
- https://ohjelmistotekniikka-hy.github.io/python/tkinter  

Minimax algorithm with alpha-beta pruning
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://www.youtube.com/watch?v=l-hh51ncgDI