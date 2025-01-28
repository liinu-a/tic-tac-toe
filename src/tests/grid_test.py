import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()


    def test_free_spaces_at_most_two_spaces_away_all_in_grid_correct(self):
        self.assertEqual(
            self.grid.get_valid_moves((3, 3)), [
                (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4),
                (1, 1), (1, 3), (1, 5), (3, 1), (3, 5), (5, 1), (5, 3), (5, 5)
            ]
        )

        self.grid.apply_move((2, 3), 1)
        self.grid.apply_move((5, 5), -1)
        self.grid.apply_move((1, 3), 1)
        self.grid.apply_move((1, 5), -1)

        self.assertEqual(
            self.grid.get_valid_moves((3, 3)), [
                (2, 2), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3),
                (4, 4), (1, 1), (3, 1), (3, 5), (5, 1), (5, 3)
            ]
        )


    def test_free_spaces_at_most_two_spaces_away_not_all_in_grid(self):
        self.assertEqual(
            self.grid.get_valid_moves((1, 0)), [
                (0, 0), (0, 1), (1, 1), (2, 0), (2, 1), (1, 2), (3, 0), (3, 2)
            ]
        )

        self.grid.apply_move((0, 0), 1)
        self.grid.apply_move((1, 1), -1)
        self.grid.apply_move((2, 0), 1)

        self.assertEqual(
            self.grid.get_valid_moves((1, 0)), [
                (0, 1), (2, 1), (1, 2), (3, 0), (3, 2)
            ]
        )


    def test_not_any_free_spaces_at_most_two_spaces_away(self):
        for r, c in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)]:
            self.grid.apply_move((r, c), 1)

        self.assertEqual(self.grid.get_valid_moves((0, 0)), [])
