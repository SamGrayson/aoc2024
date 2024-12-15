import os
import re
import time

from utils.utils import create_matrix, in_bounds

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "output.txt")


class Robot:
    def __init__(self, pos, c_move, r_move):
        self.pos = pos
        self.c_move = c_move
        self.r_move = r_move
        self.start = pos


# p=0,4 v=3,-3
def get_instructions(info: str) -> Robot:
    split = info.split(" ")
    pos = re.findall(r"\d+", split[0])
    move = split[1].replace("v=", "").strip().split(",")
    return Robot((int(pos[1]), int(pos[0])), (0, int(move[0])), (int(move[1]), 0))


# Can use this for determining quadrants
def get_middle_coord(max_r, max_c) -> int:
    return (max_r / 2, max_c / 2)


def count_quadrants(middle: tuple[int, int], robots: list[Robot]):
    top_l = 0
    top_r = 0
    bottom_l = 0
    bottom_r = 0

    """
    ... ...
    ... ...
    
    ... ...
    ... ...
    """
    for r in robots:
        # Top left q
        if r.pos[0] < middle[0] and r.pos[1] < middle[1]:
            top_l += 1
        # Top right q
        if r.pos[0] < middle[0] and r.pos[1] > middle[1]:
            top_r += 1
        # Bottom left q
        if r.pos[0] > middle[0] and r.pos[1] < middle[1]:
            bottom_l += 1
        # Bottom right q
        if r.pos[0] > middle[0] and r.pos[1] > middle[1]:
            bottom_r += 1
    return top_l * top_r * bottom_l * bottom_r


# Updates robot class with new position
def move(max_r: int, max_c: int, robot: Robot, seconds=1):
    while seconds:
        seconds -= 1
        curr_r, curr_c = robot.pos
        next_r, next_c = curr_r + robot.r_move[0], curr_c + robot.c_move[1]
        # If in bound we're good
        if in_bounds(max_r, max_c, (next_r, next_c)):
            robot.pos = (next_r, next_c)
            continue
        # Handle "teleport"
        if next_r > max_r:
            next_r = 0 + (next_r - max_r) - 1
        if next_c > max_c:
            next_c = 0 + (next_c - max_c) - 1
        if next_r < 0:
            next_r = (max_r + next_r) + 1
        if next_c < 0:
            next_c = (max_c + next_c) + 1
        robot.pos = (next_r, next_c)


def part_1():
    with open(INPUT_PATH) as file:
        max_r, max_c = 103 - 1, 101 - 1
        middle = get_middle_coord(max_r, max_c)
        robots = []

        for l in file.readlines():
            robot = get_instructions(l)
            move(max_r, max_c, robot, 10000)
            robots.append(robot)

        valid_robots = count_quadrants(middle, robots)

        print("Part 1: " + str(valid_robots))


def part_2():
    max_r, max_c = 103 - 1, 101 - 1
    robots = []
    middle = get_middle_coord(max_r, max_c)
    quarter_r = round(middle[0] / 2)
    quarter_c = round(middle[1] / 2)

    with open(INPUT_PATH) as file:
        robots = [get_instructions(l) for l in file.readlines()]

        # Start blank
        with open(OUTPUT_PATH, "w") as file:
            file.write("")
            file.close()

        for s in range(10000):
            for r in robots:
                move(max_r, max_c, r)

            # Print grid
            matrix = create_matrix(max_r + 1, max_c + 1, "_")
            for r in robots:
                cr, cc = r.pos
                matrix[cr][cc] = "X"

            # Count the xs within a smaller grid, if its over 75% print??
            start_r = int(middle[0] - quarter_r)
            end_r = int(middle[0] + quarter_r)
            start_c = int(middle[1] - quarter_c)
            end_c = int(middle[1] + quarter_c)

            total = 0
            count = 0

            for r in range(start_r, end_r):
                for c in range(start_c, end_c):
                    total += 1
                    if matrix[r][c] == "X":
                        count += 1

            heat_percent = count / total

            if heat_percent > float(0.10):
                with open(OUTPUT_PATH, "a") as file:
                    file.write("STEP " + str(s + 1) + "\n")
                    for r in matrix:
                        file.write(" ".join(r) + "\n")
                    file.write("--------------" + "\n")


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
