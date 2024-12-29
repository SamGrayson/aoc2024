import time
import unittest

from day_25.main import fits
from utils.utils import rot_90, string_to_grid

lock = rot_90(
    string_to_grid(
        """
#####
.####
.####
.####
.#.#.
.#...
....."""
    )
)

key = rot_90(
    string_to_grid(
        """
.....
#....
#....
#....
#.#.#
#.###
#####"""
    )
)


class Test(unittest.TestCase):
    def test_key_fits_lock(self):
        f = fits(key, lock)
        self.assertEqual(f, True)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
