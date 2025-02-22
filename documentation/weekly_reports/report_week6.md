# Report week 6
I was able to optimize the evaluation function by only updating the values of rows, which have changed. The old values of the changed rows are subtracted from the value of the board, to which the new values are then added. Also, instead of one board, I created seperate boards for handling vertical, downward diagonal and upward diagonal rows, which may have sped up the program a bit. The test coverage is a lot better now.

Next week I'll finish documentation. I hope to also look into optimizing the program with iterative deepening as it is still a bit slow at times.

The time spent on the project was around 20h.
