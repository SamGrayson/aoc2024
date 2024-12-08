import time
import unittest
from utils.utils import string_to_grid
from day_08.main import (
    find_all_same_locations,
    get_all_antinodes,
    get_antinode_options,
    get_antinode_options_multi,
)

TEST_GRID = string_to_grid(
    """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
)

SIMPLE_TEST = string_to_grid(
    """
....
.AA.
....
"""
)


class Test(unittest.TestCase):
    def test_find_all_same_locations_simple(self):
        # Find all the same char locations
        locals = find_all_same_locations(SIMPLE_TEST, (1, 1))
        self.assertEquals(locals, [(1, 1), (1, 2)])

    def test_find_all_same_locations(self):
        # Find all the same char locations
        locals = find_all_same_locations(TEST_GRID, ((1, 8)))
        self.assertEquals(locals, [(1, 8), (3, 7), (2, 5), (4, 4)])

    def test_get_antinode_options_simple(self):
        antinodes = get_antinode_options((1, 1), (1, 2))
        self.assertEquals(antinodes, [(1, 0), (1, 3)])

    def test_get_antinode_options(self):
        antinodes = get_antinode_options((1, 8), (3, 7))
        self.assertEquals(antinodes, [(-1, 9), (5, 6)])

    def test_get_antinode_options_multi(self):
        max_row = len(TEST_GRID)
        max_col = len(TEST_GRID[0])

        antinodes = get_antinode_options_multi(max_row, max_col, (1, 8), (3, 7))
        self.assertEquals(antinodes, [(1, 8), (3, 7), (5, 6), (7, 5), (9, 4), (11, 3)])

    def test_get_all_antinodes_simple(self):
        all_antinodes = get_all_antinodes(SIMPLE_TEST)
        self.assertEqual(len(all_antinodes), 2)

    def test_get_all_antinodes_simple_multi(self):
        all_antinodes = get_all_antinodes(SIMPLE_TEST, True)
        self.assertEqual(len(all_antinodes), 4)

    def test_get_all_antinodes(self):
        all_antinodes = get_all_antinodes(TEST_GRID)
        self.assertEqual(len(all_antinodes), 14)

    def test_get_all_antinodes_multi(self):
        all_antinodes = get_all_antinodes(TEST_GRID, True)
        for coord in all_antinodes:
            TEST_GRID[coord[0]][coord[1]] = "#"
        self.assertEqual(len(all_antinodes), 34)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
