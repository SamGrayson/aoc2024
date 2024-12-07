from collections import deque
import time
import unittest

from day_07.main import get_valid_strip, recur_test_value, recur_test_value


class Test(unittest.TestCase):
    def test_valid_strip(self):
        test, queue = get_valid_strip("3267: 81 40 27")
        self.assertEqual(test, 3267)
        self.assertEqual(queue, deque([81, 40, 27]))

    def test_valid_amounts(self):
        # 3267: 81 40 27
        tracker = {"count": 0}
        recur_test_value(3267, deque([40, 27]), 81, tracker)
        self.assertEqual(tracker["count"], 2)

    def test_invalid_amounts(self):
        # 161011: 16 10 13
        tracker = {"count": 0}
        recur_test_value(161011, deque([10, 13]), 16, tracker)
        self.assertEqual(tracker["count"], 0)

    def test_valid_amounts_new_opp(self):
        # 7290: 8 6 15
        tracker = {"count": 0}
        recur_test_value(7290, deque([8, 6, 15]), 6, tracker, True)
        self.assertTrue(tracker["count"] > 0)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
