from collections import deque
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INSTRUCTIONS_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


def can_create(possibilities: set[str], item: str, cache: dict[str, bool] = {}) -> bool:
    if item in cache:
        return cache[item]

    if not item:
        return True

    for i in range(1, len(item) + 1):
        prefix = item[:i]
        if prefix in possibilities:
            if can_create(possibilities, item[i:], cache):
                cache[item] = True
                return True

    cache[item] = False
    return False


def all_can_create(
    possibilities: set[str],
    item: str,
    cache: dict[str, int] = {},
    count=0,
) -> bool:
    if item in cache:
        return cache[item]

    if not item:
        count += 1
        return count

    options = 0
    for i in range(1, len(item) + 1):
        prefix = item[:i]
        if prefix in possibilities:
            res = all_can_create(possibilities, item[i:], cache, count)
            if not res:
                continue
            options += res

    cache[item] = count + options
    return count + options


def part_1():
    with open(INSTRUCTIONS_PATH) as file:
        possibilities = set(file.read().strip().split(", "))

    with open(INPUT_PATH) as file:
        input_lines = [line.strip() for line in file.readlines()]

    cache = {}
    result = 0
    for line in input_lines:
        if can_create(possibilities, line, cache):
            result += 1

    print("Part 1: " + str(result))


def part_2():
    with open(INSTRUCTIONS_PATH) as file:
        possibilities = set(file.read().strip().split(", "))

    with open(INPUT_PATH) as file:
        input_lines = [line.strip() for line in file.readlines()]

    cache = {}
    result = 0
    for line in input_lines:
        result += all_can_create(possibilities, line, cache)

    print("Part 2: " + str(result))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
