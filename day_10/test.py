import time
import unittest
from day_10.main import get_range_score, get_total_range_score
from utils.utils import string_to_grid

test_range = string_to_grid(
    """
0123
1234
8765
9876"""
)

test_range_double = string_to_grid(
    """9990999
9991999
9992999
6543456
7999997
8199918
9999999
  """
)

test_range_four = string_to_grid(
    """9990999
9991998
9992997
6543456
7659987
8769919
9879999
  """
)

test_full_range_map = string_to_grid(
    """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
)


class Test(unittest.TestCase):
    def test_get_range_score(self):
        range_score = get_range_score(test_range, (0, 0))
        range_score_double = get_range_score(test_range_double, (0, 3))
        range_score_four = get_range_score(test_range_four, (0, 3))
        self.assertEqual(range_score, 1)
        self.assertEqual(range_score_double, 2)
        self.assertEqual(range_score_four, 4)

    def test_get_total_range_score(self):
        total_range_score = get_total_range_score(test_full_range_map)
        self.assertEqual(total_range_score, 36)

    def test_get_total_range_score(self):
        total_range_score = get_total_range_score(test_full_range_map, True)
        self.assertEqual(total_range_score, 81)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
