# Testing documentation

## Unit testing
The project uses the unittest unit testing framework for Python. The tests cover files concerned with program logic, thus the game.py file, which mainly handles the GUI, has been excluded from testing. The test coverage report can be accessed at Codecov via [this link](https://app.codecov.io/github/liinu-a/tic-tac-toe "Codecov report for tic-tac-toe").

![Test coverage](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/test_coverage.png)  
Tests run 7.3.2025.

For some reason, there are rows that are definitely covered by the tests, but appear as uncovered in the coverage report.

### Testing the AI class
Tests have been written to test the ability of the AI to choose the right move. In the images below, the -1s are moves made by the user and the 1s moves made by the AI. No moves other than the ones visible in the images have been made. The game states in the images are not realistic, but intented for testing the AI. It is the AI's turn to decide its next move, which should and is tested to be one of the squares highlighted in red.

Preventing the user from winning by preventing them from forming an open ended row of four:

![A potential open ended four for the user](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/broken_three_threat.png)

Preventing the user from winning by preventing them from forming a double of open ended threes:

![A potential double of open ended threes for the user](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/double_three_threat.png)

Win by forming an open ended four:

![Form an open ended four](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/open_ends_three_win.png)

Form a double of open ended threes:

![Form a double of open ended threes](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/form_double_three.png)

Other test cases:
- The list of moves to be evaluated in minimax is updated correctly when moving on to explore the next move, i.e., only free squares within the board boundaries are added to the list and those already in the list are moved to the back for prioritization reasons.
- The value of a row is calculated correctly, whether the row is valueless, has some value, or the player whose turn it is has the opportunity to make a row of five and win.
- When a move is made or tried in minimax, the rows that include the marked square are correctly added to the sets, which keep track of any rows that may have changed.
- When the game state is evaluated by the evaluation function, the value of the board as well as the values of the changed rows are updated correctly and the evaluation function returns the updated value of the board.
- The table key of a game state is generated correctly. If two game states are the same, the only difference being the order in which the moves leading to it were made, then they receive the same table key.

### Testing the Board class
The test cases verify the following:
- When a square is marked, all the board variations are marked correctly.
- A row of five is found if one exists in a horizontal, vertical or upward/downward diagonal row. In the game state below, a row of five containing the move highlighted in red is not found for player 1.

![No row of five found](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/no_row_of_five.png)

- The squares at most two squares away from a move are collected correctly, i.e., they are unmarked and within the board boundaries.

## Manual testing
During the development of the project, I have test played the game multiple times. The game does not appear to have any problems and the AI plays fairly well. Additionally, I tested the depth of the search tree. The depth will always be at least 4, but can reach 5 at times.

## Running the tests
After installing the project, activating the virtual environment and navigating to the root directory, the tests can be run and the coverage collected with the command

```bash
coverage run --branch -m pytest src
```

The coverage report can now be printed with the command

```bash
coverage report -m
```
