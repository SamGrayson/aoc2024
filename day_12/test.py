import time
import unittest

from day_12.main import get_a_p, get_all_region_prices, get_total_shape_sides
from utils.utils import string_to_grid

test_grid = string_to_grid(
    """
AAAA
BBCD
BBCC
EEEC
"""
)

x_grid = string_to_grid(
    """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO 
"""
)

big_grid = string_to_grid(
    """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
)

every_test = string_to_grid(
    """
....x....
..xxxxx..
xxxx.xxxx
.xxxxxxx.
....x....  
"""
)

annoying_fence = string_to_grid(
    """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
  """
)


class Test(unittest.TestCase):

    def test_get_total_shape_sides(self):
        # A sides
        _, _, visited_a = get_a_p(test_grid, (0, 0))
        total_sides_a = get_total_shape_sides(test_grid, visited_a)
        # C sides
        _, _, visited_c = get_a_p(test_grid, (1, 2))
        total_sides_c = get_total_shape_sides(test_grid, visited_c)
        # D sides
        _, _, visited_d = get_a_p(test_grid, (1, 3))
        total_sides_d = get_total_shape_sides(test_grid, visited_d)
        # X sides
        _, _, visited_x = get_a_p(x_grid, (1, 1))
        total_sides_x = get_total_shape_sides(x_grid, visited_x)
        # O sides
        _, _, visited_o = get_a_p(x_grid, (0, 0))
        total_sides_o = get_total_shape_sides(x_grid, visited_o)
        #  every_test
        _, _, visited_all = get_a_p(every_test, (0, 4))
        total_sides_all = get_total_shape_sides(every_test, visited_all)

        self.assertEqual(total_sides_a, 4)
        self.assertEqual(total_sides_c, 8)
        self.assertEqual(total_sides_d, 4)
        self.assertEqual(total_sides_x, 4)
        self.assertEqual(total_sides_o, 20)
        self.assertEqual(total_sides_all, 24)

    def test_get_a_p(self):
        # # A test
        a_a, a_p, _ = get_a_p(test_grid, (0, 0))
        # B test
        b_a, b_p, _ = get_a_p(test_grid, (1, 0))
        # # C Test
        c_a, c_p, _ = get_a_p(test_grid, (1, 2))
        # # D Test
        d_a, d_p, _ = get_a_p(test_grid, (1, 3))
        # # E Test
        e_a, e_p, _ = get_a_p(test_grid, (3, 0))
        # # Tests
        self.assertEqual((a_a, a_p), (4, 10))
        self.assertEqual((b_a, b_p), (4, 8))
        self.assertEqual((c_a, c_p), (4, 10))
        self.assertEqual((d_a, d_p), (1, 4))
        self.assertEqual((e_a, e_p), (3, 8))

    def test_get_all_region_prices(self):
        total_price, total_side_price = get_all_region_prices(test_grid)
        total_price_x, total_side_price_x = get_all_region_prices(x_grid)
        total_price_bg, _ = get_all_region_prices(big_grid)
        _, total_side_price_annoying = get_all_region_prices(annoying_fence)
        self.assertEqual(total_price, 140)
        self.assertEqual(total_price_x, 772)
        self.assertEqual(total_price_bg, 1930)
        self.assertEqual(total_side_price, 80)
        self.assertEqual(total_side_price_x, 436)
        self.assertEqual(total_side_price_annoying, 368)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
