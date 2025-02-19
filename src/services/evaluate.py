VALUES = {
    2: 5,
    3: 20,
    4: 10000
}

def get_horizontal_val(board, row, cur_turn):
    start_col = end_col = 0
    count = value = 0
    last = -1
    player = None

    while end_col < 20 and board[row][end_col] == 0:
        end_col += 1

    if end_col == 20:
        return 0

    player = board[row][end_col]
    start_col = 0 if end_col <= 4 else end_col - 4

    while end_col < 20:
        if board[row][end_col] == (-1) * player:
            player *= (-1)
            count = 0
            if last >= start_col:
                start_col = last + 1

        if board[row][end_col] == player:
            count += 1
            last = end_col

        if end_col - start_col == 4:
            if count == 4:
                if player == cur_turn:
                    return 100000000 * cur_turn

            if count > 1:
                value += VALUES[count] * player

            count -= abs(board[row][start_col])
            start_col += 1
        end_col += 1

    return value


def get_vertical_val(board, col, cur_turn):
    start_row = end_row = 0
    count = value = 0
    last = -1
    player = None

    while end_row < 20 and board[end_row][col] == 0:
        end_row += 1

    if end_row == 20:
        return 0

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
                    return 100000000 * cur_turn

            if count > 1:
                value += VALUES[count] * player

            count -= abs(board[start_row][col])
            start_row += 1
        end_row += 1

    return value


def get_downward_diag_val(board, diag_begin, cur_turn):
    start_row = end_row = diag_begin[0]
    start_col = end_col = diag_begin[1]
    count = value = 0
    last_row = last_col = -1
    player = None

    while end_col < 20 > end_row and board[end_row][end_col] == 0:
        end_row += 1
        end_col += 1

    if end_col == 20 or end_row == 20:
        return 0

    player = board[end_row][end_col]
    if end_row - start_row > 4:
        start_row, start_col = end_row - 4, end_col - 4

    while end_col < 20 > end_row:
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
                    return 100000000 * cur_turn

            if count > 1:
                value += VALUES[count] * player

            count -= abs(board[start_row][start_col])
            start_row += 1
            start_col += 1
        end_row += 1
        end_col += 1

    return value


def get_upward_diag_val(board, diag_begin, cur_turn):
    start_row = end_row = diag_begin[0]
    start_col = end_col = diag_begin[1]
    count = value = 0
    last_row = last_col = -1
    player = None

    while end_col >= 0 and end_row < 20 and board[end_row][end_col] == 0:
        end_row += 1
        end_col -= 1

    if end_col < 0 or end_row == 20:
        return 0

    player = board[end_row][end_col]
    if end_row - start_row > 4:
        start_row, start_col = end_row - 4, end_col + 4

    while end_col >= 0 and end_row < 20:
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
                    return 100000000 * cur_turn

            if count > 1:
                value += VALUES[count] * player

            count -= abs(board[start_row][start_col])
            start_row += 1
            start_col -= 1
        end_row += 1
        end_col -= 1

    return value
