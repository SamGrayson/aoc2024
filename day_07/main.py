from collections import deque
from copy import copy
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

options = ["*", "+"]


def recur_test_value(
    test: int, nums: deque[int], total: int, tracker: dict[str, int], enable_combo=False
):
    c = copy(nums)
    if len(c) > 0:
        add = total + c[0]
        times = total * c[0]
        if enable_combo:
            combo = int(str(total) + str(c[0]))
        c.popleft()
        add_result = recur_test_value(test, c, add, tracker, enable_combo)
        times_result = recur_test_value(test, c, times, tracker, enable_combo)
        # COMBO!!!
        if enable_combo:
            combo_result = recur_test_value(test, c, combo, tracker, enable_combo)
        if (
            add_result == test
            or times_result == test
            or (enable_combo and combo_result == test)
        ):
            tracker["count"] += 1
    else:
        return total


def get_valid_strip(s: str):
    split = s.split(":")
    test = split[0]
    list = map(int, split[1].strip().split(" "))
    return (int(test), deque(list))


def part_1():
    tests = []
    with open(INPUT_PATH) as file:
        for l in file:
            tests.append(get_valid_strip(l))
    total_success = 0
    for t in tests:
        tracker = {"count": 0}
        test, queue = t
        start = queue.popleft()
        recur_test_value(test, queue, start, tracker)
        if tracker["count"] > 0:
            total_success += test
    print("Part 1: " + str(total_success))


def part_2():
    tests = []
    with open(INPUT_PATH) as file:
        for l in file:
            tests.append(get_valid_strip(l))
    total_success = 0
    for t in tests:
        tracker = {"count": 0}
        test, queue = t
        start = queue.popleft()
        recur_test_value(test, queue, start, tracker, True)
        if tracker["count"] > 0:
            total_success += test
    print("Part 2: " + str(total_success))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
