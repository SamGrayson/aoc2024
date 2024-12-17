import time
import unittest

from day_16.main import find_shortest_paths
from utils.utils import string_to_grid, find_first_str_in_matrix


test_maze = string_to_grid(
    """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
)


class Test(unittest.TestCase):
    def test_find_s_e(self):
        self.assertEqual(find_first_str_in_matrix(test_maze, "S"), (13, 1))
        self.assertEqual(find_first_str_in_matrix(test_maze, "E"), (1, 13))

    def test_find_shortest_paths(self):
        start = find_first_str_in_matrix(test_maze, "S")
        res = find_shortest_paths(test_maze, start)

        self.assertEqual(res, 7036)

    def test_success(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
