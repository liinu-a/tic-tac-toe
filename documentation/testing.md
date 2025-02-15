# Testing documentation

## Unit Testing
The unit test coverage of the project has gone down as I haven't had time to write tests for the evaluation function yet. What is tested:
- Free squares no more than two squares away from a move and within the boundaries of the game board are correctly collected into a list.
- The list that contains the moves to be evaluated is updated correclty.
- If a row of five exists, it is found if a move contained in it is given.

![Test coverage](https://github.com/liinu-a/tic-tac-toe/blob/main/documentation/test_coverage_week5.png)

## Manual testing
I have tested the gameplay of the AI through the GUI. A version of the evaluation function has been implemented and seems to be somewhat working. I was able to detect and fix some bucgs. However, the program has significantly slowed down.