# Report week 2
I created a function that produces a list of moves or markable spaces, which are at most two spaces away from a given space, free and within the grid. In the context of the application, the given space is a move made by either player and the moves produced based on it are to be added to the list of moves to explore. 

The list containing the moves to explore should have the following features:
- The list should not contain duplicates.
- Potential moves around the previous move should be prioritized in the list order, as they should be explored first. 

It took some time to come up with a way to implement the list. This is how the list could be updated, when a move is made and the potential moves around it need to be added to the list:
- There is a 20x20 table that can be used to check the index of an element in the list. Grid spaces not in the list get the value -1. 
- There is a variable i that stores the position of the last item in the list.
- If a move to be added is already in the list (its position can be checked from the table), then it swaps positions with the item at i and i is decreased by one.
- Else, the move is appended to the end of the list.
Additionally, any move that is made must be removed from the list (if present). This way duplicates could be avoided and the prioritized moves would be at the back of the list. For example, if the list is [(1, 2), (0, 0), (4, 2), (7, 3), (9, 15), (19, 0)] and it is updated with [(1, 2), (3, 1), (3, 3), (9, 15), (19, 0)], the result would be [(7, 3), (0, 0), (4, 2), (19, 0), (9, 15), (1, 2), (3, 1), (3, 3)].

I hope I explained the idea well enough. I am open to a better solution. 

Additionally, I created some unittests and started measuring the code coverage with coverage.py.

The time spent on the project was around 16h.