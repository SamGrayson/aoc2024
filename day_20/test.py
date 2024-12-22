import time
import unittest

from day_20.main import get_path_options, get_shortest_path
from utils.utils import string_to_grid, find_first_str_in_matrix


test_grid = string_to_grid(
    """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
)


class Test(unittest.TestCase):
    def test_shortest_path(self):
        start = find_first_str_in_matrix(test_grid, "S")
        end = find_first_str_in_matrix(test_grid, "E")
        steps_left = get_shortest_path(test_grid, start, end)
        shortest_path = steps_left[end]
        for k, v in steps_left.items():
            steps_left[k] = shortest_path - v
        options = get_path_options(
            test_grid, start, end, shortest_path - 64, 1, steps_left
        )
        self.assertEqual(options[shortest_path - 64], 1)

    def test_shortest_paths_more(self):
        start = find_first_str_in_matrix(test_grid, "S")
        end = find_first_str_in_matrix(test_grid, "E")
        steps_left = get_shortest_path(test_grid, start, end)
        shortest_path = steps_left[end]
        for k, v in steps_left.items():
            steps_left[k] = shortest_path - v
        options = get_path_options(
            test_grid, start, end, shortest_path - 50, 20, steps_left
        )
        total = 0
        for o in options.values():
            total += o
        self.assertEqual(total, 315)

    def test_success(self):
        self.assertEqual(True, True)
