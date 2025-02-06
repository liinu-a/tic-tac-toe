import unittest
from services.board import collect_moves_to_evaluate, update_moves_to_evaluate


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
        update_moves_to_evaluate(self.moves_to_evaluate, (2, 18), self.board)

        self.assertEqual(self.moves_to_evaluate, [
            (0, 16), (4, 16), (0, 18), (2, 16), (4, 18), (1, 17), (1, 19), (3, 17),
            (3, 19), (1, 18), (2, 17), (2, 19), (3, 18)
        ])

    def test_update_moves_to_evaluate_with_overlapping_move(self):
        self.board[3][4] = -1
        update_moves_to_evaluate(self.moves_to_evaluate, (3, 4), self.board)
        update_moves_to_evaluate(self.moves_to_evaluate, (4, 5), self.board)

        self.assertEqual(self.moves_to_evaluate, [
            (1, 2), (1, 6), (5, 2), (1, 4), (3, 2), (2, 4), (3, 3), (2, 3),
            (2, 7), (6, 3), (6, 7), (2, 5), (4, 3), (4, 7), (6, 5), (3, 6),
            (5, 4), (5, 6), (3, 5), (4, 4), (4, 6), (5, 5)
        ])