import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_mark_boad(self):
        self.board.mark_board((0, 0), 1)
        self.assertEqual(self.board.board[0][0], 1)
        self.assertEqual(self.board.board_vertical[0][0], 1)
        self.assertEqual(self.board.board_downward_diag[19][0], 1)
        self.assertEqual(self.board.board_upward_diag[0][0], 1)

        self.board.mark_board((0, 19), -1)
        self.assertEqual(self.board.board[0][19], -1)
        self.assertEqual(self.board.board_vertical[19][0], -1)
        self.assertEqual(self.board.board_downward_diag[0][0], -1)
        self.assertEqual(self.board.board_upward_diag[19][0], -1)

        self.board.mark_board((3, 8), 1)
        self.assertEqual(self.board.board[3][8], 1)
        self.assertEqual(self.board.board_vertical[8][3], 1)
        self.assertEqual(self.board.board_downward_diag[14][3], 1)
        self.assertEqual(self.board.board_upward_diag[11][3], 1)

        self.board.mark_board((16, 10), 1)
        self.assertEqual(self.board.board[16][10], 1)
        self.assertEqual(self.board.board_vertical[10][16], 1)
        self.assertEqual(self.board.board_downward_diag[25][10], 1)
        self.assertEqual(self.board.board_upward_diag[26][9], 1)


    def test_horizontal_row_of_five(self):
        for i in range(5):
            self.board.mark_board((0, i), 1)

        self.assertEqual(self.board.row_of_five((0, 0), 1), True)
        self.assertEqual(self.board.row_of_five((0, 2), 1), True)
        self.assertEqual(self.board.row_of_five((0, 4), 1), True)

    def test_vertical_row_of_five(self):
        for i in range(5):
            self.board.mark_board((i, 0), -1)

        self.assertEqual(self.board.row_of_five((0, 0), -1), True)
        self.assertEqual(self.board.row_of_five((2, 0), -1), True)
        self.assertEqual(self.board.row_of_five((4, 0), -1), True)

    def test_downward_diag_row_of_five(self):
        for i in range(5):
            self.board.mark_board((i, i), 1)

        self.assertEqual(self.board.row_of_five((0, 0), 1), True)
        self.assertEqual(self.board.row_of_five((2, 2), 1), True)
        self.assertEqual(self.board.row_of_five((4, 4), 1), True)

    def test_upward_diag_row_of_five(self):
        for i in range(5):
            self.board.mark_board((i, 19 - i), -1)

        self.assertEqual(self.board.row_of_five((0, 19), -1), True)
        self.assertEqual(self.board.row_of_five((2, 17), -1), True)
        self.assertEqual(self.board.row_of_five((4, 15), -1), True)

    def test_row_of_five_cut_off(self):
        for i in range(9):
            self.board.mark_board((i, i), 1)

        self.board.mark_board((4, 4), -1)

        self.assertEqual(self.board.row_of_five((2, 2), 1), False)


    def test_collected_moves_to_evaluate_correct_inner_square(self):
        self.assertEqual(self.board.collect_moves_to_evaluate((4, 7)), [
            (2, 5), (2, 9), (6, 5), (6, 9), (2, 7), (4, 5), (4, 9), (6, 7),
            (3, 6), (3, 8), (5, 6), (5, 8), (3, 7), (4, 6), (4, 8), (5, 7)
        ])

        self.board.mark_board((2, 5), 1)
        self.board.mark_board((4, 5), -1)
        self.board.mark_board((3, 7), 1)

        self.assertEqual(self.board.collect_moves_to_evaluate((4, 7)), [
            (2, 9), (6, 5), (6, 9), (2, 7), (4, 9), (6, 7), (3, 6), (3, 8),
            (5, 6), (5, 8), (4, 6), (4, 8), (5, 7)
        ])

    def test_collected_moves_to_evaluate_correct_edge_square(self):
        self.assertEqual(self.board.collect_moves_to_evaluate((18, 17)), [
            (16, 15), (16, 19), (16, 17), (18, 15), (18, 19), (17, 16), (17, 18), (19, 16),
            (19, 18), (17, 17), (18, 16), (18, 18), (19, 17)
        ])

        self.board.mark_board((19, 18), -1)
        self.board.mark_board((17, 16), 1)
        self.board.mark_board((18, 19), 1)

        self.assertEqual(self.board.collect_moves_to_evaluate((18, 17)), [
            (16, 15), (16, 19), (16, 17), (18, 15), (17, 18), (19, 16), (17, 17), (18, 16),
            (18, 18), (19, 17)
        ])
