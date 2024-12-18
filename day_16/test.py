import time
import unittest

from day_16.main import dijkstra_shortest
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

    def test_d_shortest(self):
        start = find_first_str_in_matrix(test_maze, "S")
        end = find_first_str_in_matrix(test_maze, "E")
        shortest, visited = dijkstra_shortest(test_maze, start, end)

        self.assertEqual(shortest, 7036)

    def test_success(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
