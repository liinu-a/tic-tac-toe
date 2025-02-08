# Implementation document

## Project structure

### Classes and helper functions

#### Game
The game class builds and handles the GUI and takes care of user interaction. It receives input from the user, to which it then gets a response from the AI. It additionally handles the state of the game, i.e., has the game ended, does the user request the game to be restarted.

#### AI
The AI class handles the decision making of the AI.

#### minimax
The minimax algorithm is a method of the AI class and used to calculate the next move of the AI. The minimax algorithm is optimized with alpha-beta pruning.  

Thus far, no LLMs have been used in this project.

## Sources
Implementing the GUI with Tkinter
- https://www.youtube.com/watch?v=xx0qmpuA-vM
- https://ohjelmistotekniikka-hy.github.io/python/tkinter  

Minimax algorithm with alpha-beta pruning
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://www.youtube.com/watch?v=l-hh51ncgDI