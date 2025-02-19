import unittest
from services.board import collect_moves_to_evaluate, update_moves_to_evaluate, row_of_five


class TestCollectMovesToEvaluate(unittest.TestCase):
    def setUp(self):
        self.board = [[0 for _ in range(20)] for _ in range(20)]

    def test_collected_moves_to_evaluate_correct_when_no_square_marked(self):
        self.assertEqual(collect_moves_to_evaluate(self.board, (4, 7)), [
            (2, 5), (2, 9), (6, 5), (6, 9), (2, 7), (4, 5), (4, 9), (6, 7),
            (3, 6), (3, 8), (5, 6), (5, 8), (3, 7), (4, 6), (4, 8), (5, 7)
        ])

    def test_collected_moves_to_evaluate_correct_inner_square(self):
        self.board[2][3] = -1
        self.board[5][5] = 1
        self.board[1][3] = -1
        self.board[1][5] = 1

        self.assertEqual(collect_moves_to_evaluate(self.board, (3, 3)), [
            (1, 1), (5, 1), (3, 1), (3, 5), (5, 3), (2, 2), (2, 4), (4, 2),
            (4, 4), (3, 2), (3, 4), (4, 3)
        ])

    def test_collected_moves_to_evaluate_correct_corner_square_lower_left(self):
        self.board[1][0] = -1
        self.board[1][1] = 1

        self.assertEqual(collect_moves_to_evaluate(self.board, (0, 0)), [
            (2, 2), (0, 2), (2, 0), (0, 1)
        ])

    def test_collected_moves_to_evaluate_correct_corner_square_upper_right(self):
        self.board[18][18] = -1

        self.assertEqual(collect_moves_to_evaluate(self.board, (19, 19)), [
            (17, 17), (17, 19), (19, 17), (18, 19), (19, 18)
        ])

    def test_collected_moves_to_evaluate_empty_when_every_square_marked(self):
        for row, col in [(1, 0), (1, 1), (2, 2), (0, 2), (2, 0), (0, 1)]:
            self.board[row][col] = -1

        self.assertEqual(collect_moves_to_evaluate(self.board, (0, 0)), [])


class TestUpdateMovesToEvaluate(unittest.TestCase):
    def setUp(self):
        self.board = [[0 for _ in range(20)] for _ in range(20)]
        self.moves_to_evaluate = []

    def test_updating_empty_moves_to_evaluate(self):
        self.board[2][18] = -1
        update_moves_to_evaluate(self.moves_to_evaluate, (2, 18), self.board)

        self.assertEqual(self.moves_to_evaluate, [
            (0, 16), (4, 16), (0, 18), (2, 16), (4, 18), (1, 17), (1, 19), (3, 17),
            (3, 19), (1, 18), (2, 17), (2, 19), (3, 18)
        ])

    def test_update_moves_to_evaluate_with_overlapping_move(self):
        self.board[3][4] = -1
        update_moves_to_evaluate(self.moves_to_evaluate, (3, 4), self.board)

        self.board[4][5] = 1
        update_moves_to_evaluate(self.moves_to_evaluate, (4, 5), self.board)

        self.assertEqual(self.moves_to_evaluate, [
            (1, 2), (1, 6), (5, 2), (1, 4), (3, 2), (2, 4), (3, 3), (2, 3),
            (2, 7), (6, 3), (6, 7), (2, 5), (4, 3), (4, 7), (6, 5), (3, 6),
            (5, 4), (5, 6), (3, 5), (4, 4), (4, 6), (5, 5)
        ])

    def test_update_moves_to_evaluate_with_three_moves(self):
        self.board[7][10] = -1
        update_moves_to_evaluate(self.moves_to_evaluate, (7, 10), self.board)

        self.board[11][15] = 1
        update_moves_to_evaluate(self.moves_to_evaluate, (11, 15), self.board)

        self.board[9][12] = -1
        update_moves_to_evaluate(self.moves_to_evaluate, (9, 12), self.board)

        self.assertEqual(self.moves_to_evaluate, [
            (5, 8), (5, 12), (9, 8), (5, 10), (7, 8), (6, 9), (6, 11), (8, 9),
            (6, 10), (7, 9), (7, 11), (8, 10), (9, 17), (13, 13), (13, 17), (9, 15),
            (11, 13), (11, 17), (13, 15), (10, 14), (10, 16), (12, 14), (12, 16), (10, 15),
            (11, 16), (12, 15), (7, 14), (11, 10), (11, 14), (7, 12), (9, 10), (9, 14),
            (11, 12), (8, 11), (8, 13), (10, 11), (10, 13), (8, 12), (9, 11), (9, 13),
            (10, 12)
        ])


class TestRowOfFive(unittest.TestCase):
    def setUp(self):
        self.board = [[0 for _ in range(20)] for _ in range(20)]

    def test_vertical_row_exists(self):
        for row in range(5):
            self.board[row][0] = 1

        self.assertEqual(row_of_five(self.board, (0, 0), 1), True)
        self.assertEqual(row_of_five(self.board, (2, 0), 1), True)
        self.assertEqual(row_of_five(self.board, (4, 0), 1), True)

    def test_vertical_row_cut_off_top(self):
        for row in range(4):
            self.board[row][0] = 1

        self.assertEqual(row_of_five(self.board, (3, 0), 1), False)

    def test_vertical_row_cut_off_bottom(self):
        for row in range(16, 20):
            self.board[row][0] = -1

        self.assertEqual(row_of_five(self.board, (17, 0), -1), False)

    def test_vertical_row_cut_off_by_opponent(self):
        for row in range(10):
            self.board[row][0] = 1

        self.board[4][0] = -1

        self.assertEqual(row_of_five(self.board, (3, 0), 1), False)

    def test_horizontal_row_exists(self):
        for col in range(5):
            self.board[0][col] = -1

        self.assertEqual(row_of_five(self.board, (0, 0), -1), True)
        self.assertEqual(row_of_five(self.board, (0, 2), -1), True)
        self.assertEqual(row_of_five(self.board, (0, 4), -1), True)

    def test_horizontal_row_cut_off_left(self):
        for col in range(4):
            self.board[0][col] = 1

        self.assertEqual(row_of_five(self.board, (0, 3), 1), False)

    def test_horizontal_row_cut_off_right(self):
        for col in range(16, 20):
            self.board[0][col] = 1

        self.assertEqual(row_of_five(self.board, (0, 17), 1), False)

    def test_horizontal_row_cut_off_by_opponent(self):
        for col in range(10):
            self.board[0][col] = -1

        self.board[0][4] = 1

        self.assertEqual(row_of_five(self.board, (0, 3), -1), False)

    def test_downward_diagonal_row_exists(self):
        for i in range(5):
            self.board[i][i] = 1

        self.assertEqual(row_of_five(self.board, (0, 0), 1), True)
        self.assertEqual(row_of_five(self.board, (2, 2), 1), True)
        self.assertEqual(row_of_five(self.board, (4, 4), 1), True)

    def test_downward_diagonal_row_cut_off_top_left(self):
        for i in range(4):
            self.board[i][i] = -1

        self.assertEqual(row_of_five(self.board, (2, 2), -1), False)

    def test_downward_diagonal_row_cut_off_bottom_right(self):
        for i in range(16, 20):
            self.board[i][i] = -1

        self.assertEqual(row_of_five(self.board, (16, 16), -1), False)

    def test_downward_diagonal_row_cut_off_by_opponent(self):
        for i in range(10):
            self.board[i][i] = 1

        self.board[4][4] = -1

        self.assertEqual(row_of_five(self.board, (3, 3), 1), False)

    def test_upward_diagonal_row_exists(self):
        for i in range(5):
            self.board[19 - i][i] = 1

        self.assertEqual(row_of_five(self.board, (19, 0), 1), True)
        self.assertEqual(row_of_five(self.board, (17, 2), 1), True)
        self.assertEqual(row_of_five(self.board, (15, 4), 1), True)

    def test_upward_diagonal_row_cut_off_top_right(self):
        for i in range(4):
            self.board[i][19 - i] = -1

        self.assertEqual(row_of_five(self.board, (3, 16), -1), False)

    def test_upward_diagonal_row_cut_off_bottom_left(self):
        for i in range(4):
            self.board[19 - i][i] = 1

        self.assertEqual(row_of_five(self.board, (17, 2), 1), False)

    def test_upward_diagonal_row_cut_off_by_opponent(self):
        for i in range(10):
            self.board[i][19 - i] = 1

        self.board[4][15] = -1

        self.assertEqual(row_of_five(self.board, (3, 16), 1), False)
