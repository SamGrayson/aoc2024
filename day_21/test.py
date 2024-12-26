from collections import deque
import time
import unittest
from day_21.main import (
    recur_shortest,
)


class Test(unittest.TestCase):
    def test_find_paths_in_grid(self):
        path = recur_shortest("029A")
        self.assertEqual(len(path), 12)

    def test_find_paths_in_grid_recur_one(self):
        path = recur_shortest("029A", 2)
        self.assertEqual(len(path), 28)

    def test_find_paths_in_grid_recur_deep(self):
        path = recur_shortest("379A", 3)
        self.assertEqual(len(path), 64)

    def test_get_sum_all_sequences(self):
        sequences = ["029A", "980A", "179A", "456A", "379A"]
        total = 0
        for l in sequences:
            path = recur_shortest(l, 3)
            total += len(path) * int(l.replace("A", ""))
        self.assertEqual(total, 126384)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
