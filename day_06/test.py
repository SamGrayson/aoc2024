import unittest
from day_06.main import find_loops, find_start, step_through
from utils.utils import string_to_grid

TEST_GRID = string_to_grid(
    """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
)


class Test(unittest.TestCase):
    def test_find_start(self):
        SIMPLE_TEST = string_to_grid(
            """
.#..
...#
.^..
            """
        )
        start = find_start(SIMPLE_TEST)
        self.assertEqual(start, (2, 1, "up"))

    def test_navigate_success_small(self):
        SIMPLE_TEST = string_to_grid(
            """
.#..
...#
.^..
            """
        )
        visits = step_through(SIMPLE_TEST, (2, 1, "up"))
        self.assertEqual(visits, 4)

    def test_navigate_loop_success_small(self):
        SIMPLE_TEST = string_to_grid(
            """
.#..
...#
#^..
..#
            """
        )
        visits = step_through(SIMPLE_TEST, (2, 1, "up"))
        self.assertEqual(visits, -1)

    def test_navigate_success_big(self):
        visits = step_through(TEST_GRID, (6, 4, "up"))
        self.assertEqual(visits, 41)

    def test_success_find_loops(self):
        loops = find_loops(TEST_GRID, (6, 4, "up"))
        self.assertEqual(loops, 6)


if __name__ == "__main__":
    unittest.main()
