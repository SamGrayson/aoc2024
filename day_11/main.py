from functools import reduce, cache
import functools
import os
import time
from math import ceil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


# "125 17"
def get_total_count_blinks(start: str, blinks: int) -> int:
    test_str = start
    total_count = 0
    for s in test_str.split(" "):
        total_count += memoize_blink(s, blinks)
    return total_count


@cache
def memoize_blink(i: str, blink_depth: int) -> int:
    if blink_depth >= 1:
        # Current stone
        key = i
        if int(key) == 0:
            return memoize_blink("1", blink_depth - 1)
        elif len(key) % 2 == 0:
            return memoize_blink(
                str(int(key[: ceil(len(key) / 2)])), blink_depth - 1
            ) + memoize_blink(str(int(key[ceil(len(key) / 2) :])), blink_depth - 1)
        else:
            return memoize_blink(str(int(key) * 2024), blink_depth - 1)
    return 1


def part_1():
    with open(INPUT_PATH) as file:
        print("Part 1: " + str(get_total_count_blinks(file.read().strip(), 25)))


def part_2():
    with open(INPUT_PATH) as file:
        print("Part 1: " + str(get_total_count_blinks(file.read().strip(), 75)))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
