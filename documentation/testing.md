# Testing documentation

## Unit testing
The project uses the unittest unit testing framework for Python. The tests cover files concerned with program logic, thus the game.py file, which mainly handles the GUI, has been excluded from testing.

![Test coverage](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/test_coverage.png)  

For some reason, there are rows that are definitely covered by the tests, but appear as uncovered in the coverage report.

### Testing the AI
A few tests have been written to test the ability of the AI to choose the right move. In the images below, the -1s are moves made by the user and the 1s moves made by the AI. The game states in the images are not realistic, but intented for testing the AI. It is the AI's turn to decide its next move, which should be one of the squares highlighted in red.  
Preventing the user from winning with an open ended row of four:
![Broken three threat](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/broken_three_threat.png)  
Preventing the user from winning with a double of open ended threes:
![Double three threat](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/double_three_threat.png)  
Win by forming an open ended four:
![Form an open ended four](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/open_ends_three_win.png)  
Form a double of open ended threes:
![Form an open ended double three](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/form_double_three.png)  




## Manual testing
