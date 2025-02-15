def evaluate(board, cur_turn):
    next_turn = cur_turn * (-1)
    start_row = start_col = end_row = end_col = 0
    last = -1
    count = 0
    player = None

    value = 0
    best_for_cur_turn = winning_rows_for_next = 0
    values = {
        0: 0,
        1: 1,
        2: 10,
        3: 100,
        4: 10000
    }

    for row in board:
        count = 0
        while end_col < 20 and row[end_col] == 0:
            end_col += 1

        if end_col == 20:
            continue

        player = row[end_col]
        start_col = 0 if end_col <= 4 else end_col - 4

        while end_col < 20:
            if row[end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last >= start_col:
                    start_col = last + 1

            if row[end_col] == player:
                count += 1
                last = end_col

            if end_col - start_col == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(row[start_col])
                start_col += 1

            end_col += 1


    for col in range(20):
        count = 0
        while end_row < 20 and board[end_row][col] == 0:
            end_row += 1

        if end_row == 20:
            continue

        player = board[end_row][col]
        start_row = 0 if end_row <= 4 else end_row - 4

        while end_row < 20:
            if board[end_row][col] == (-1) * player:
                player *= (-1)
                count = 0
                if last >= start_row:
                    start_row = last + 1

            if board[end_row][col] == player:
                count += 1
                last = end_row

            if end_row - start_row == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(board[start_row][col])
                start_row += 1

            end_row += 1

    last_row = last_col = -1

    for i in range(16):
        count = 0
        start_row = end_row = i
        start_col = end_col = 0

        while end_row < 20 and board[end_row][end_col] == 0:
            end_row += 1
            end_col += 1

        if end_row == 20:
            continue

        player = board[end_row][end_col]
        start_row, start_col = (i, 0) if end_col <= 4 else (end_row - 4, end_col - 4)

        while end_row < 20:
            if board[end_row][end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last_row >= start_row:
                    start_row = last_row + 1
                    start_col = last_col + 1

            if board[end_row][end_col] == player:
                count += 1
                last_row = end_row
                last_col = end_col

            if end_row - start_row == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(board[start_row][start_col])
                start_row += 1
                start_col += 1

            end_row += 1
            end_col += 1


    for i in range(1, 16):
        count = 0
        start_row = end_row = 0
        start_col = end_col = i

        while end_col < 20 and board[end_row][end_col] == 0:
            end_row += 1
            end_col += 1

        if end_col == 20:
            continue

        player = board[end_row][end_col]
        start_row, start_col = (0, i) if end_row <= 4 else (end_row - 4, end_col - 4)

        while end_col < 20:
            if board[end_row][end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last_row >= start_row:
                    start_row = last_row + 1
                    start_col = last_col + 1

            if board[end_row][end_col] == player:
                count += 1
                last_row = end_row
                last_col = end_col

            if end_row - start_row == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(board[start_row][start_col])
                start_row += 1
                start_col += 1

            end_row += 1
            end_col += 1


    for i in range(16):
        count = 0
        start_row = end_row = i
        start_col = end_col = 19

        while end_row < 20 and board[end_row][end_col] == 0:
            end_row += 1
            end_col -= 1

        if end_row == 20:
            continue

        player = board[end_row][end_col]
        start_row, start_col = (i, 19) if end_col >= 15 else (end_row - 4, end_col + 4)

        while end_row < 20:
            if board[end_row][end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last_row >= start_row:
                    start_row = last_row + 1
                    start_col = last_col - 1

            if board[end_row][end_col] == player:
                count += 1
                last_row = end_row
                last_col = end_col

            if end_row - start_row == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(board[start_row][start_col])
                start_row += 1
                start_col -= 1

            end_row += 1
            end_col -= 1


    for i in range(18, 3, -1):
        count = 0
        start_row = end_row = 0
        start_col = end_col = i

        while end_col >= 0 and board[end_row][end_col] == 0:
            end_row += 1
            end_col -= 1

        if end_col == -1:
            continue

        player = board[end_row][end_col]
        start_row, start_col = (0, i) if end_row <= 4 else (end_row - 4, end_col + 4)

        while end_col >= 0:
            if board[end_row][end_col] == (-1) * player:
                player *= (-1)
                count = 0
                if last_row >= start_row:
                    start_row = last_row + 1
                    start_col = last_col - 1

            if board[end_row][end_col] == player:
                count += 1
                last_row = end_row
                last_col = end_col

            if end_row - start_row == 4:
                if count == 4:
                    if player == cur_turn:
                        return 10000000 * cur_turn

                    winning_rows_for_next += 1

                if winning_rows_for_next < 2:
                    if player == cur_turn:
                        best_for_cur_turn = max(best_for_cur_turn, count)
                    value += values[count] * player

                count -= abs(board[start_row][start_col])
                start_row += 1
                start_col -= 1

            end_row += 1
            end_col -= 1

    if winning_rows_for_next >= 2:
        return 10000000 * next_turn

    value -= values[best_for_cur_turn] * cur_turn
    value += values[best_for_cur_turn + 1] * cur_turn
    return value
