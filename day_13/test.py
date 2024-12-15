from math import inf
import time
import unittest

from day_13.main import (
    calc_token_cost,
    get_shortest_win,
    get_total_shortest_wins,
    parse_input,
)


test_case = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""


input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


class Test(unittest.TestCase):
    def test_parse(self):
        guidelines = parse_input(test_case)
        self.assertEqual(list(guidelines.keys()), ["a", "b", "prize"])
        self.assertEqual(guidelines["a"], (94, 34))
        self.assertEqual(guidelines["b"], (22, 67))
        self.assertEqual(guidelines["prize"], (8400, 5400))

    def test_get_shortest_win_success(self):
        guidelines = parse_input(test_case, False)
        shortest = get_shortest_win(guidelines)
        self.assertEqual(shortest, 280)

    def test_get_shortest_win_impossible(self):
        guidelines = parse_input(test_case, True)
        shortest = get_shortest_win(guidelines)
        self.assertEqual(shortest, None)

    def test_calc_tokens(self):
        tokens = calc_token_cost(10, 1)
        self.assertEqual(tokens, 31)

    def test_get_all_prizes_cost(self):
        test = ""
        tests = []
        for l in input.split("\n"):
            if l:
                test += l + "\n"
            else:
                if test:
                    tests.append(test)
                test = ""
        total = get_total_shortest_wins(tests)
        self.assertEqual(total, 480)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
