import time
import unittest

from day_11.main import (
    get_total_count_blinks,
    memoize_blink,
)

SIMPLE_TEST = "0 1 10 99 999"


class Test(unittest.TestCase):
    def test_blink(self):
        count = memoize_blink("125", 6) + memoize_blink("17", 6)
        self.assertEqual(count, 22)

    def test_memoize_stones_one_blink(self):
        total_count = get_total_count_blinks(SIMPLE_TEST, 1)
        self.assertEqual(total_count, 7)

    def test_count_stones_multi_blink(self):
        self.assertEqual(get_total_count_blinks("125 17", 6), 22)
        self.assertEqual(get_total_count_blinks("125 17", 25), 55312)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
