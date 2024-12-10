from itertools import groupby
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


# "0099811188827773336446555566.............."
def calc_checksum(input: list[str]) -> int:
    checksum = 0
    for idx, i in enumerate(input):
        if i != ".":
            checksum += int(i) * idx
    return checksum


# "0..111....22222"
# "022111222......"
def move_files(li: list[str]) -> list[str]:
    for lidx, i in enumerate(li):
        if i == ".":
            pop = "."
            while pop == ".":
                pop = li.pop()
            if lidx <= len(li):
                li[lidx] = pop
            else:
                # Add back last pop if not "."
                if pop != ".":
                    li.append(pop)

    return li


# "00...111...2...333.44.5555.6666.777.888899"
# "00992111777.44.333....5555.6666.....8888.."
def move_files_block(li: list[str]) -> list[str]:
    groups = [list(group) for _, group in groupby(li)]
    queue = groups[:]
    while queue:
        test = queue.pop()
        if test[0] != ".":
            # Open space
            for nidx, nl in enumerate(groups):
                if nl[0] == ".":
                    if len(nl) >= len(test):
                        groups[nidx] = test
                        if len(nl) - len(test) > 0:
                            groups.insert(
                                nidx + 1, ["." for _ in range(len(nl) - len(test))]
                            )
                        for ridx, bl in reversed(list(enumerate(groups))):
                            if bl == test:
                                groups[ridx] = ["." for _ in bl]
                                break
                        break

    return [x for xs in groups for x in xs]


# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
def format_str(input: str) -> list[str]:
    li = []
    idx = -1
    # Loop every 2
    for i in range(0, len(input), 2):
        idx += 1
        # Add block
        block = [str(idx) for _ in range(int(input[i]))]
        li = li + block
        # Add free space (as long as its there)
        if i == len(input) - 1:
            break
        free = ["." for _ in range(int(input[i + 1]))]
        li = li + free
    return li


def part_1():
    with open(INPUT_PATH) as file:
        input = file.read()
    checksum = calc_checksum(move_files(format_str(input)))
    print("Part 1: " + str(checksum))


def part_2():
    with open(INPUT_PATH) as file:
        input = file.read()
    checksum = calc_checksum(move_files_block(format_str(input)))
    print("Part 2: " + str(checksum))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
