# Implementation document

## Project structure

### Classes and functions

#### Game
The game class builds and handles the GUI and takes care of user interaction. The class receives a move the user requests to make and then may get a move from the AI. After each move, the class checks the status of the game, i.e., is the game still ongoing or has it concluded.

#### AI
The AI class handles the decision making of the AI. The class tracks the value of the board, the values of the horizontal, vertical and diagonal rows and which of the rows may have changed. The board value and row values are not aligned with the actual game state, but rather with a game state that was last evaluated by the evaluation function during minimax.  


#### decide_move


#### minimax
The minimax algorithm is a method of the AI class and used to calculate the next move of the AI. The minimax algorithm is optimized with alpha-beta pruning and explores only the moves at most two spaces away from the previous moves. The order of exploration is based on how recent the previous move is. In the worst case scenario, the time complexity of the minimax algorithm with alpha-beta pruning is O(b^k), where b is the branching factor and k is the depth of the search tree. The branching factor b is not an exact number and varies depending on the amount moves to be evaluated.

#### collect_moves_to_evaluate
A function that collects the free squares at most two squares away from a given move on the board. The time complexity is O(1), as the function checks which of the 16 squares are valid.

#### update_moves_to_evaluate
A function that updates the list of moves to be evaluated in the minimax algorithm with the moves it gets by calling the collect_moves_to_evaluate function. Moves, which are already present in the list are moved to the end and the nonpresent ones appended to the end of the list. Thus, minimax explores the list in reverse order. Also, removes the preceding move that triggered the update from the list. 

#### row_of_five
When given a move, the function checks for a vertical, horizontal or diagonal row of five that contains the move.

## Possible flaws and improvements

## Use of LLMs
No LLMs have been used in this project.

## Sources
Implementing the GUI with Tkinter
- https://www.youtube.com/watch?v=xx0qmpuA-vM
- https://ohjelmistotekniikka-hy.github.io/python/tkinter  

Minimax algorithm with alpha-beta pruning
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://www.youtube.com/watch?v=l-hh51ncgDI