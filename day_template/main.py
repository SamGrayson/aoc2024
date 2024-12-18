import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def part_1():
    with open(INPUT_PATH) as file:
        print(file.read())


def part_2():
    with open(INPUT_PATH) as file:
        print(file.read())


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
