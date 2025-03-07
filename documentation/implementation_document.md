# Implementation document

## Project structure

### Classes and functions

#### Game
The game class builds and handles the GUI and takes care of user interaction. The class's method make_move receives a move the user requests to make and gets a move from the AI. After each move, the status of the game is checked, i.e., does the game still continue or has it concluded.

#### AI
The AI class handles the decision making of the AI. The class tracks the value of the entire board, the values of the horizontal, vertical and diagonal rows and which of the rows may have changed. The board value and row values are not aligned with the actual game state, but rather with the game state that was last evaluated by the evaluation function during a search.  

#### decide_move
The decide_move method of the AI class calls minimax repeatedly, the search depth increasing with each iteration. Once the time limit expires and the depth to which minimax searches is at least five, the result from the previous depth is returned. Additionally, before returning, empties the table to which minimax saves data.

#### minimax
The minimax algorithm is a method of the AI class. The algorithm has been optimized with alpha-beta pruning and by limiting and ordering the moves that are explored at each step. Only the moves at most two spaces away from the preceding moves are evaluated, the ones being nearest to the previous move raised to be evaluated first. The move yielding the optimal result for the player whose turn it is, is saved in a table. When entering the same game state with the same or a later iteration, the move saved to the table is evaluated first. 
In the worst case scenario, the time complexity of the algorithm with is O(b^k), where b is the branching factor and k is the depth of the search tree. The branching factor b is not an exact number and varies depending on the amount moves to be evaluated.

#### update_moves_to_evaluate
A method of the AI class. Updates the list of moves to be evaluated in minimax with the moves the collect_moves_to_evaluate method returns. Moves, which are already present in the list are moved to the end and the nonpresent ones appended to the end of the list. The move that triggered the update is removed from the list. The worst case time complexity is O(17*n), where n is the length of the list. 

#### get_table_key



#### collect_moves_to_evaluate
A function that collects the free squares at most two squares away from a given move on the board. The time complexity is O(1), as the function checks which of the 16 squares are valid.

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