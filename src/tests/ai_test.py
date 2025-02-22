import unittest
from ai import AI
from board import Board

class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.ai = AI()


    def test_moves_to_evaluate_updated_correctly(self):
        self.board.mark_board((7, 10), -1)
        self.ai.update_moves_to_evaluate(self.ai.moves_to_evaluate, (7, 10), self.board)

        self.board.mark_board((11, 15), 1)
        self.ai.update_moves_to_evaluate(self.ai.moves_to_evaluate, (11, 15), self.board)

        self.board.mark_board((9, 12), -1)
        self.ai.update_moves_to_evaluate(self.ai.moves_to_evaluate, (9, 12), self.board)

        self.assertEqual(self.ai.moves_to_evaluate, [
            (5, 8), (5, 12), (9, 8), (5, 10), (7, 8), (6, 9), (6, 11), (8, 9),
            (6, 10), (7, 9), (7, 11), (8, 10), (9, 17), (13, 13), (13, 17), (9, 15),
            (11, 13), (11, 17), (13, 15), (10, 14), (10, 16), (12, 14), (12, 16), (10, 15),
            (11, 16), (12, 15), (7, 14), (11, 10), (11, 14), (7, 12), (9, 10), (9, 14),
            (11, 12), (8, 11), (8, 13), (10, 11), (10, 13), (8, 12), (9, 11), (9, 13),
            (10, 12)
        ])


    def test_row_with_no_val(self):
        self.assertEqual(self.ai.get_row_val([
            1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1
        ], 1), 0)

        self.assertEqual(self.ai.get_row_val([
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ], 1), 0)

    def test_row_with_val(self):
        self.assertEqual(self.ai.get_row_val([
            0, 0, -1, -1, -1, 0, 0, -1, 1, -1, 0, 0, 0, -1, 0, 1, 1, 1, 1, 0
        ], -1), 19919)

        self.assertEqual(self.ai.get_row_val([
            1, 1, 0, 0, 1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0
        ], -1), -41)

    def test_row_leading_to_win_val(self):
        self.assertEqual(self.ai.get_row_val([
            0, -1, -1, -1, -1, 0, 0, -1, 1, 1, 1, 1, 0, -1, 0, 0, 0, 0, 0, 0
        ], 1), 100000000)


    def test_adding_to_updated_rows(self):
        self.ai.updated_rows((5, 4))

        self.assertSetEqual(self.ai.updated_horizontals, {5})
        self.assertSetEqual(self.ai.updated_verticals, {4})
        self.assertSetEqual(self.ai.updated_downward_diags, {20})
        self.assertSetEqual(self.ai.updated_upward_diags, {9})

        self.ai.updated_rows((6, 4))
        self.ai.updated_rows((7, 6))
        self.ai.updated_rows((5, 13))

        self.assertSetEqual(self.ai.updated_horizontals, {5, 6, 7})
        self.assertSetEqual(self.ai.updated_verticals, {4, 6, 13})
        self.assertSetEqual(self.ai.updated_downward_diags, {20, 21, 11})
        self.assertSetEqual(self.ai.updated_upward_diags, {9, 10, 13, 18})

        self.ai.updated_rows((18, 0))
        self.ai.updated_rows((16, 19))

        self.assertSetEqual(self.ai.updated_horizontals, {5, 6, 7, 18, 16})
        self.assertSetEqual(self.ai.updated_verticals, {4, 6, 13, 0, 19})
        self.assertSetEqual(self.ai.updated_downward_diags, {20, 21, 11, 16})
        self.assertSetEqual(self.ai.updated_upward_diags, {9, 10, 13, 18})


    def test_board_evaluation(self):
        for move in [(3, 6), (4, 5), (5, 5), (5, 6), (6, 6), (6, 7)]:
            self.board.mark_board(move, 1)
            self.ai.updated_rows(move)

        for move in [(2, 4), (2, 6), (2, 7), (1, 7), (3, 5)]:
            self.board.mark_board(move, -1)
            self.ai.updated_rows(move)

        self.ai.evaluate(self.board, -1)

        self.assertEqual(self.ai.horizontal_vals[2], -43)
        self.assertEqual(self.ai.horizontal_vals[5], 4)
        self.assertEqual(self.ai.horizontal_vals[6], 4)

        self.assertEqual(self.ai.vertical_vals[5], 1)
        self.assertEqual(self.ai.vertical_vals[6], 22)
        self.assertEqual(self.ai.vertical_vals[7], -2)

        self.assertEqual(self.ai.downward_diags_vals[17], -3)
        self.assertEqual(self.ai.downward_diags_vals[18], 62)
        self.assertEqual(self.ai.downward_diags_vals[19], 4)

        self.assertEqual(self.ai.upward_diags_vals[8], -41)
        self.assertEqual(self.ai.upward_diags_vals[9], 1)

        self.assertEqual(self.ai.board_eval, 9)

        self.board.mark_board((4, 4), -1)
        self.ai.updated_rows((4, 4))
        self.board.mark_board((7, 8), 1)
        self.ai.updated_rows((7, 8))

        self.ai.evaluate(self.board, -1)

        self.assertEqual(self.ai.vertical_vals[4], -3)
        self.assertEqual(self.ai.downward_diags_vals[18], 20042)
        self.assertEqual(self.ai.downward_diags_vals[19], 1)
        self.assertEqual(self.ai.upward_diags_vals[8], -100000000)

        self.assertEqual(self.ai.board_eval, -99979976)


    def test_block_broken_three_threat(self):
        for move in [(3, 7), (3, 8), (3, 10)]:
            self.board.mark_board(move, -1)

        self.ai.moves_to_evaluate = [
            (1, 5), (1, 9), (5, 5), (5, 9), (1, 7), (3, 5), (5, 7), (2, 6),
            (4, 6), (1, 6), (1, 10), (5, 6), (5, 10), (1, 8), (3, 6), (3, 10),
            (5, 8), (2, 7), (2, 9), (4, 7), (4, 9), (2, 8), (3, 9), (4, 8)
        ]
        self.ai.horizontal_vals[3] = self.ai.board_eval = -4

        self.assertEqual(self.ai.decide_move((3, 10), self.board), (3, 9))

    def test_block_two_of_three_threat(self):
        for move in [(5, 4), (4, 4), (3, 5), (3, 6)]:
            self.board.mark_board(move, -1)

        self.ai.moves_to_evaluate = [
            (3, 2), (7, 2), (7, 6), (5, 2), (5, 6), (7, 4), (6, 3), (6, 5),
            (2, 2), (6, 2), (6, 6), (4, 2), (6, 4), (4, 3), (1, 3), (1, 7),
            (5, 3), (5, 7), (1, 5), (3, 3), (3, 7), (5, 5), (2, 4), (2, 6),
            (4, 6), (2, 5), (3, 4), (3, 6), (4, 5)
        ]
        self.ai.vertical_vals[4] = self.ai.upward_diags_vals[8] = -4 
        self.ai.board_eval = -8

        self.assertEqual(self.ai.decide_move((3, 6), self.board), (3, 4))
