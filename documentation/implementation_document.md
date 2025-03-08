# Implementation document

## Project structure
The program consists of three classes, which are Game, AI and Board.

### Classes and methods

#### Game
The game class builds and handles the GUI and takes care of user interaction. The class's method make_move receives a move the user requests to make and gets a move from the AI. After each move, the status of the game is checked, i.e., does the game still continue or has it concluded.

#### AI
The AI class handles the decision making of the AI. The class tracks the value of the entire board, the values of the horizontal, vertical and diagonal rows of the board, as well as which rows may have changed. The board value and row values are not aligned with the actual game state, but rather with the game state that was last evaluated by the evaluation function during a search.  

 **decide_move**
The decide_move method calls minimax repeatedly, the search depth increasing with each iteration. Once the time limit expires and the depth to which minimax searches is at least five, the result from the previous depth is returned.

 **minimax**
The minimax algorithm calculates the move of the AI. The algorithm has been optimized with alpha-beta pruning and by limiting and ordering the moves that are explored at each step of the search. Only the moves at most two spaces away from the preceding moves are evaluated, the ones being nearest to the previous move raised to be evaluated first. The move yielding the optimal result for the player whose turn it is, is saved in a table. When entering the same game state within the same or a later iteration, the saved move is evaluated first.  
In the worst case scenario, the time complexity of the algorithm is O(b^k), where b is the branching factor and k is the depth of the search tree. The branching factor b varies due to alpha-beta pruning and the varying amount of moves to be evaluated.

 **update_moves_to_evaluate**
Updates the list of moves to be evaluated in minimax when the search proceeds to explore the next move. The moves are evaluated in reverse order. Thus, for prioritization purposes, all moves to be added to the list are appended to the end and moves already in the list are moved to the end. The move to be explored is removed from the list. The worst case time complexity is O((m+1)*n+m), where n is the length of the list to be updated and m is the amount of moves the list is updated with. 

 **get_table_key**
Gets the table key of a game state. Whenever decide_move gets called, the current game state, i.e., the actual moves made thus far, gets assigned an empty string as its key. In minimax, the key of the current game state is obtained by extending the key of the previous game state with a string depicting the last move. In the image below, the grey moves are actual moves and the colorful moves belong to the sequence of moves that led to the current game state that is being evaluated in minimax. The red move is the last move and would be depicted as "+0202". The key of the current game state would be "+0000-0001+0202-0203-0205+0302+0303". The time complexity is O(n).

![Game state key](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/game_state_key.png)

 **changed_rows**
Updates the sets, which keep track of the rows that may have changed. As diagonal rows vary in length, diagonal rows under five in length are ignored as they can not contain a row of five.

 **evaluate**
Evaluates the game state by updating and returning the board value. The board value is updated by reevaluating the changed board rows. The estimated time complexity is O(n*m), where n is the length of the row, which can vary, and m is the number of rows to reevaluate.

 **get_row_val**
Calculates the value of a board row. The method tries to find windows of length five in the row, which may only contain one player's marks and free squares. The value of a found window is added to the total value of the row or, if the player whose turn it is can get a win, a value very favorable to the player is returned as the value of the row. The time complexity is O(n), where n is the length of the row.

#### Board
The board class handles the calculations done on the board and, for the ease of the calculations, has different variations of the board, i.e., separate lists for horizontal, vertical and downward/upward diagonal rows.

 **mark_board**
Marks the correct square for each board variation. The time complexity is O(1).

 **row_of_five**
When given a move, determines whether a player has gotten a vertical, horizontal or diagonal row of five that contains the move.

 **check_row_of_five**
Checks a single row to determine if a player has gotten a row of five that contains a move that occupies the given column.

 **collect_moves_to_evaluate**
A function that collects the free squares at most two squares away from a given move on the board. The time complexity is O(1), as, for any call, the function checks which of 16 squares are valid.

## Possible flaws and improvements
The depth to which minimax is able to explore moves in a reasonable amount of time could be improved. This could be achieved by taking better advantage of alpha-beta pruning by introducing a better logic for the order in which moves are evaluated in minimax, thus causing more branches of the search tree to be eliminated. Additionaly, the evaluation function could be more efficient.

## Use of LLMs
No LLMs have been used in this project.

## Sources
Implementing the GUI with Tkinter
- https://www.youtube.com/watch?v=xx0qmpuA-vM
- https://ohjelmistotekniikka-hy.github.io/python/tkinter  

Minimax algorithm with alpha-beta pruning
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://www.youtube.com/watch?v=l-hh51ncgDI

Iterative deepening
- https://domwil.co.uk/minimaxer/part2/
