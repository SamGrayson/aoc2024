import os
import time
from collections import deque
from utils.utils import (
    directions_plus,
    find_first_str_in_matrix,
    flip_dir,
    in_bounds,
    string_to_grid,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def get_result(l: tuple[int, int]) -> int:
    steps, turns = l
    return turns * 1000 + steps


def find_shortest_paths(
    grid: list[list[str]], start: tuple[int, int]
) -> tuple[int, int]:
    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    start_row, start_col = start
    queue = deque([(start_row, start_col, 0, 0, (0, 0))])

    lowest = 0

    while queue:
        curr_row, curr_col, steps, turns, prev_dir = queue.popleft()

        res = get_result((steps, turns))
        if lowest and res > lowest:
            continue

        if grid[curr_row][curr_col] == "E":
            if lowest == 0 or res < lowest:
                lowest = res
            continue

        state = (curr_row, curr_col, turns, prev_dir, steps)
        if state in visited:
            continue
        visited.add(state)

        for curr_dir in directions_plus:
            xr, xy = curr_dir
            new_row = curr_row + xr
            new_col = curr_col + xy

            # Skip if out of bounds or hitting a wall
            if (
                not in_bounds(max_row, max_col, (new_row, new_col))
                or grid[new_row][new_col] == "#"
            ):
                continue

            new_turns = turns
            if prev_dir and prev_dir != curr_dir:
                new_turns += 1

            queue.append((new_row, new_col, steps + 1, new_turns, (xr, xy)))

    return lowest


def part_1():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
        start = find_first_str_in_matrix(input, "S")
        lowest = find_shortest_paths(input, start)
        print("Part 1: " + str(lowest))


def part_2():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
        start = find_first_str_in_matrix(input, "S")
        lowest = find_shortest_paths_seats(input, start)
        print("Part 2: " + str(lowest))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
