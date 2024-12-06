import time
import os

from collections import deque
from utils.utils import string_to_grid
from utils.utils import directions_plus


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

UP, RIGHT, DOWN, LEFT = directions_plus
DIR_MAP = {"up": UP, "right": RIGHT, "down": DOWN, "left": LEFT}
TURN = {"up": "right", "right": "down", "down": "left", "left": "up"}


def find_start(grid: list[list[str]]) -> tuple[int, int, str]:
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "^":
                return (ridx, cidx, "up")


# Dir will start UP
def step_through(grid: list[list[str]], start: tuple[int, int, str]) -> int:
    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    start_row, start_col, dir = start
    queue = deque([(start_row, start_col, dir)])

    unique_coord = set([(start_row, start_col)])
    while len(queue) > 0:
        curr_row, curr_col, dir = queue.popleft()

        # If we've been here, skip
        if (curr_row, curr_col, dir) in visited:
            # If -1, we've been here before - loop!
            return -1

        visited.add((curr_row, curr_col, dir))
        new_row = curr_row + DIR_MAP[dir][0]
        new_col = curr_col + DIR_MAP[dir][1]

        # We're at the end - made it out
        if 0 > new_row > max_row and 0 > new_col > max_col:
            break

        # If next step is not obstacle, step that way
        if (
            0 <= new_row < max_row
            and 0 <= new_col < max_col
            and grid[new_row][new_col] != "#"
        ):
            unique_coord.add((new_row, new_col))
            queue.append((new_row, new_col, dir))
            continue

        # If next step IS an obstacle, turn right
        if (
            0 <= new_row < max_row
            and 0 <= new_col < max_col
            and grid[new_row][new_col] == "#"
        ):
            queue.append((curr_row, curr_col, TURN[dir]))
            continue

    return len(unique_coord)


def find_loops(grid: list[list[str]], start: tuple[int, int, str]):
    # Shocked if this works
    loops = 0
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            # Skip existing obstacles
            if c == "#":
                continue
            # Skip starting point
            if (ridx, cidx) != start:
                # Replace current spot with obstruction
                grid[ridx][cidx] = "#"
                # Loop found, add it and continue
                result = step_through(grid, start)
                if result == -1:
                    loops += 1
                # Put it back and continue
                grid[ridx][cidx] = "."
    return loops


def part_1():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
    start = find_start(input)

    print("Part 1: " + str(step_through(input, start)))


def part_2():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
    start = find_start(input)

    print("Part 2: " + str(find_loops(input, start)))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
