from collections import deque
import time
import unittest
from day_21.main import (
    do_it,
)


class Test(unittest.TestCase):
    def test_find_paths_in_grid(self):
        path_count = do_it("029A", 1)
        self.assertEqual(path_count, 12)

    def test_find_paths_in_grid_recur_one(self):
        path_count = do_it("029A", 2)
        self.assertEqual(path_count, 28)

    def test_find_paths_in_grid_recur_deep(self):
        path_count = do_it("029A", 3)
        self.assertEqual(path_count, 68)

    def test_get_sum_all_sequences(self):
        sequences = ["029A", "980A", "179A", "456A", "379A"]
        total = 0
        for l in sequences:
            path_count = do_it(l, 3)
            total += path_count * int(l.replace("A", ""))
        self.assertEqual(total, 126384)

    def test_get_sum_all_sequences_big(self):
        sequences = ["029A", "980A", "179A", "456A", "379A"]
        total = 0
        for l in sequences:
            path_count = do_it(l, 26)
            res = path_count * int(l.replace("A", ""))
            print(f"{l}:" + str(res))
            total += res
        self.assertEqual(total, 154115708116294)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
