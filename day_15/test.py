from copy import deepcopy
import time
import unittest

from day_15.main import (
    get_gpc_calc,
    get_gpc_calc_boxes,
    get_movement,
    get_stones_set,
    move,
)
from utils.utils import string_to_grid, pretty_print_grid

test_grid = string_to_grid(
    """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
"""
)
test_dirs = "<^^>>>vv<v>>v<<"

test_grid_big = string_to_grid(
    """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########
"""
)

test_dirs_big = """<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


test_big_boxes = string_to_grid(
    """
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
"""
)

simple_test_double = string_to_grid(
    """
###########
##.[]##[]##
##.......##
##.[][]..##
##..[]...##
##..@....##
###########
  """
)


class Test(unittest.TestCase):
    def test_get_movement(self):
        dirs = get_movement(test_dirs)
        self.assertEqual(dirs[:4], [(0, -1), (-1, 0), (-1, 0), (0, 1)])

    def test_stones(self):
        stones = get_stones_set(test_grid)
        self.assertEqual(list(stones)[0], (1, 3))

    def test_move_small(self):
        dirs = get_movement(test_dirs)
        grid = deepcopy(test_grid)
        start = (2, 2)
        for m in dirs:
            result = move(grid, start, m)
            if result == 1:
                start = (start[0] + m[0], start[1] + m[1])

        # pretty_print_grid(grid)

        self.assertEqual(start, (4, 4))

    def test_move_big(self):
        dirs = get_movement("".join(test_dirs_big.split("\n")))
        grid = deepcopy(test_grid_big)
        start = (4, 4)
        for m in dirs:
            result = move(grid, start, m)
            if result == 1:
                start = (start[0] + m[0], start[1] + m[1])

        # pretty_print_grid(grid)

        self.assertEqual(start, (4, 3))

    def test_move_big_boxes(self):
        dirs = get_movement("".join(test_dirs_big.split("\n")))
        grid = deepcopy(test_big_boxes)
        start = (4, 8)
        for _, m in enumerate(dirs):
            result = move(grid, start, m)
            if result == 1:
                start = (start[0] + m[0], start[1] + m[1])

        self.assertEqual(start, (7, 4))

    def test_gps_calc_big(self):
        dirs = get_movement("".join(test_dirs_big.split("\n")))
        grid = deepcopy(test_grid_big)
        start = (4, 4)
        for m in dirs:
            result = move(grid, start, m)
            pretty_print_grid(grid)
            if result == 1:
                start = (start[0] + m[0], start[1] + m[1])

        gps_calc = get_gpc_calc(grid)

        self.assertEqual(gps_calc, 10092)

    def test_gps_calc_box(self):
        dirs = get_movement("".join(test_dirs_big.split("\n")))
        grid = deepcopy(test_big_boxes)
        start = (4, 8)
        for m in dirs:
            result = move(grid, start, m)
            if result == 1:
                start = (start[0] + m[0], start[1] + m[1])

        gps_calc = get_gpc_calc_boxes(grid)

        self.assertEqual(gps_calc, 9021)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
