import unittest
from day_04.main import get_mas_x, get_xmas_x_v, is_mas, is_xmas

simple_grid = [
    ["x", "m", "a", "s"],
    [".", "m", "m", "m"],
    [".", ".", "a", "."],
    [".", "s", ".", "s"],
]


class Test(unittest.TestCase):
    def test_fan_out_dir_success(self):
        self.assertTrue(is_xmas(simple_grid, (0, 0), (0, 1)))
        self.assertTrue(is_xmas(simple_grid, (0, 0), (1, 1)))

    def test_fan_out_dir_fail(self):
        self.assertFalse(is_xmas(simple_grid, (0, 0), (1, 0)))

    def test_mas_x_success(self):
        self.assertTrue(is_mas(simple_grid, (1, 1), (1, 1)))

    def test_mas_x_fail(self):
        self.assertTrue(is_mas(simple_grid, (1, 3), (1, -1)))

    def test_find_all_mas_x(self):
        total_mas_x = 0
        for xidx, r in enumerate(simple_grid):
            for yidx, c in enumerate(r):
                if c == "a":
                    total_mas_x += get_mas_x(simple_grid, (xidx, yidx))
        self.assertEqual(total_mas_x, 1)

    def test_find_all_xmas_h_v(self):
        total_xmas = 0
        for xidx, r in enumerate(simple_grid):
            for yidx, c in enumerate(r):
                if c == "x":
                    total_xmas += get_xmas_x_v(simple_grid, (xidx, yidx))
        self.assertEquals(total_xmas, 2)


if __name__ == "__main__":
    unittest.main()