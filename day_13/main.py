from math import inf, gcd
import os
import re
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


# Determinate
# Simplifying algorithm from..
# A * x1 + B * x2 = z
# A * x2 + B * y2 = z
#
def solve_a(guideline: dict) -> float:
    x1 = guideline["a"][0]
    x2 = guideline["b"][0]
    y1 = guideline["a"][1]
    y2 = guideline["b"][1]
    target_x = guideline["prize"][0]
    target_y = guideline["prize"][1]
    return (x2 * target_y - y2 * target_x) / (x2 * y1 - x1 * y2)


def parse_input(str: str, add_balloon: bool = False) -> dict[str, tuple[int, int]]:
    split = str.split("\n")
    guidelines = {}
    for line in split:
        digits = re.findall(r"\d+", line)
        if "A" in line:
            guidelines["a"] = (int(digits[0]), int(digits[1]))
        if "B" in line:
            guidelines["b"] = (int(digits[0]), int(digits[1]))
        if "Prize" in line:
            if add_balloon:
                guidelines["prize"] = (
                    10000000000000 + int(digits[0]),
                    10000000000000 + int(digits[1]),
                )
            else:
                guidelines["prize"] = (int(digits[0]), int(digits[1]))
    return guidelines


# I have this essentially: x1 + x2 * y1 + y2 = z
# I can turn it into this: y1 = (z - x1 * x2) / y2
def alg_formula(x1: int, a: int, z: int, x2: int) -> float:
    return (z - x1 * a) / x2


def calc_token_cost(a_presses: int, b_presses: int) -> int:
    return a_presses * 3 + b_presses * 1


# 100 is the limit, just check for the lowest token value
def get_shortest_win(guidelines: dict[str, tuple[int, int]], max=100) -> int:
    x1 = guidelines["a"][0]
    x2 = guidelines["b"][0]
    target_x = guidelines["prize"][0]
    a = solve_a(guidelines)
    b = alg_formula(x1, a, target_x, x2)
    if a.is_integer() and b.is_integer():
        return calc_token_cost(a, b)
    return None


def get_total_shortest_wins(li: list[str], add_balloon: bool = False) -> int:
    total = 0
    for l in li:
        g = parse_input(l, add_balloon)
        shortest_cost = get_shortest_win(g)
        if shortest_cost != None:
            total += shortest_cost
    return total


def part_1():
    with open(INPUT_PATH) as file:
        test = ""
        tests = []
        for l in file.readlines():
            if l and l != "\n":
                test += l + "\n"
            else:
                if test:
                    tests.append(test)
                test = ""
        if test:
            tests.append(test)
            test = ""
        total = get_total_shortest_wins(tests)
        print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        test = ""
        tests = []
        for l in file.readlines():
            if l and l != "\n":
                test += l + "\n"
            else:
                if test:
                    tests.append(test)
                test = ""
        if test:
            tests.append(test)
            test = ""
        total = get_total_shortest_wins(tests, True)
        print("Part 2: " + str(total))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
