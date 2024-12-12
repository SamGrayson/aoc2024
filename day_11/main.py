from functools import reduce
import functools
import os
import time
from math import ceil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next


# "0 1 10 99 999"
def create_ll(input: str) -> Node:
    split = input.split(" ")
    return reduce(
        lambda next_node, value: Node(value, next_node), reversed(split), None
    )


def get_total_count_blinks(start: str, blinks: int) -> int:
    test_str = start
    total_count = 0
    while blinks >= 1:
        print("BLINK! - " + str(blinks))
        blink_count = 0
        blink_str = ""
        for s in test_str.split(" "):
            s_count, new_str = memoize_blink(s)
            blink_count += s_count
            blink_str += f" {new_str}"
        total_count = blink_count
        test_str = blink_str.strip()
        blinks -= 1
    return total_count


@functools.cache
def memoize_blink(i: str) -> tuple[int, str]:
    go = True
    curr = create_ll(i)
    count = 0
    new_stones = ""
    while go:
        # Current stone
        key = curr.key
        if int(key) == 0:
            curr.key = "1"
            count += 1
            new_stones += " 1"
        elif len(key) % 2 == 0:
            curr.key = str(int(key[: ceil(len(key) / 2)]))
            next_node = Node(str(int(key[ceil(len(key) / 2) :])), curr.next)
            curr.next = next_node
            # We're splitting the stones, so the next is actually the _new_ next
            new_stones += f" {curr.key} {next_node.key}"
            curr = next_node
            count += 2
        else:
            curr.key = str(int(key) * 2024)
            count += 1
            new_stones += f" {curr.key}"
        # Handle next
        if curr.next == None:
            go = False
        else:
            curr = curr.next
    return count, new_stones.strip()


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
