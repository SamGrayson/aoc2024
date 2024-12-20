import time
import unittest

from day_19.main import all_can_create, can_create

possibles = set("r, wr, b, g, bwu, rb, gb, br".split(", "))

designs = "brwrr, bggr, gbbr, rrbgbr, ubwu, bwurrg, brgr, bbrgwb".split(", ")


class Test(unittest.TestCase):
    def test_can_create(self):
        yup = can_create(possibles, designs[5])
        self.assertTrue(yup)

    def test_call_can_create(self):
        cache = {}
        options = all_can_create(possibles, "rrbgbr", cache)
        self.assertEqual(options, 6)

    def test_total_create_count(self):
        success = 0
        cache = {}
        for d in designs:
            success += 1 if can_create(possibles, d, cache) else 0
        self.assertEqual(success, 6)

    def test_total_all_create_count(self):
        success = 0
        cache = {}
        for d in designs:
            success += all_can_create(possibles, d, cache)
        self.assertEqual(success, 16)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
