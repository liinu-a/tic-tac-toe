import unittest
from ai import AI

class TestAI(unittest.TestCase):
    def setUp(self):
        self.AI = AI()


    def test_space_is_marked_correctly(self):
        self.AI.mark_space(1, 0, 19)

        self.assertEqual(self.AI.grid[0][19], 1)
        self.assertNotEqual(self.AI.grid[0][19], self.AI.grid[1][19])


    def test_free_spaces_at_most_two_spaces_away_all_in_grid_correct(self):
        self.assertEqual(
            self.AI.get_free_valid_spaces(3, 3), [
                (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4),
                (1, 1), (1, 3), (1, 5), (3, 1), (3, 5), (5, 1), (5, 3), (5, 5)
            ]
        )

        self.AI.mark_space(1, 2, 3)
        self.AI.mark_space(-1, 5, 5)
        self.AI.mark_space(1, 1, 3)
        self.AI.mark_space(-1, 1, 5)

        self.assertEqual(
            self.AI.get_free_valid_spaces(3, 3), [
                (2, 2), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3),
                (4, 4), (1, 1), (3, 1), (3, 5), (5, 1), (5, 3)
            ]
        )


    def test_free_spaces_at_most_two_spaces_away_not_all_in_grid_correct(self):
        self.assertEqual(
            self.AI.get_free_valid_spaces(1, 0), [
                (0, 0), (0, 1), (1, 1), (2, 0), (2, 1), (1, 2), (3, 0), (3, 2)
            ]
        )

        self.AI.mark_space(1, 0, 0)
        self.AI.mark_space(-1, 1, 1)
        self.AI.mark_space(1, 2, 0)

        self.assertEqual(
            self.AI.get_free_valid_spaces(1, 0), [
                (0, 1), (2, 1), (1, 2), (3, 0), (3, 2)
            ]
        )


    def test_not_any_free_spaces_at_most_two_spaces_away(self):
        for r, c in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)]:
            self.AI.mark_space(1, r, c)

        self.assertEqual(self.AI.get_free_valid_spaces(0, 0), [])
