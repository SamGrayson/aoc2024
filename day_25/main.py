import os
import time

from utils.utils import rot_90, string_to_grid

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def fits(key: list[list[str]], lock: list[list[str]]):
    space = len(key[0])
    for idx, k in enumerate(key):
        if (k.count("#") + lock[idx].count("#")) > space:
            return False
    return True


def part_1():
    with open(INPUT_PATH) as file:
        keys = []
        locks = []
        options = []
        o = ""
        for l in file.readlines():
            if l.strip() == "":
                if len(o) > 0:
                    options.append(o)
                    o = ""
                continue
            o += l
        fit_count = 0
        if len(o) > 0:
            options.append(o)
            o = ""

        while options:
            o = options.pop()
            if o[0] == ".":
                keys.append(rot_90(string_to_grid(o)))
            if o[0] == "#":
                locks.append(rot_90(string_to_grid(o)))

        for k in keys:
            for l in locks:
                fit_count += 1 if fits(k, l) else 0

        print("Part 1: " + str(fit_count))


def part_2():
    with open(INPUT_PATH) as file:
        print(file.read())


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
