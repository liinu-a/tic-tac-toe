def minimax(grid, moves_to_evaluate, previous_move, depth, alpha, beta, turn):

    if grid.row_of_five(previous_move):
        return turn * (-1)
    
    if len(moves_to_evaluate) == 0:
        return 0
    
    best_value = turn * (-1)

    for move in moves_to_evaluate:
        grid.apply_move(move, turn)

        # Update moves_to_evaluate

        value = minimax(grid, moves_to_evaluate, move, depth + 1, alpha, beta, turn * (-1))

        grid.remove_move(move, turn)
        
        if turn == 1:
            best_value = max(value, best_value)
            alpha = max(value, alpha)
        else:
            best_value = min(value, best_value)
            beta = min(value, beta)

        if beta <= alpha:
            break

    return best_value
