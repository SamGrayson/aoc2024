from collections import deque
from utils.utils import (
    directions_plus,
    find_first_str_in_matrix,
    in_bounds,
    string_to_grid,
)
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def get_shortest_path(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> dict:
    max_r = len(grid)
    max_c = len(grid[0])
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    seconds_left = {}
    while queue:
        cr, cc, steps = queue.popleft()
        if (cr, cc) == end:
            seconds_left[(cr, cc)] = steps
            return seconds_left
        if (cr, cc) in visited:
            continue
        visited.add((cr, cc))
        for dir in directions_plus:
            nr, nc = cr + dir[0], cc + dir[1]
            if in_bounds(max_r, max_c, (nr, nc)) and grid[nr][nc] != "#":
                seconds_left[(cr, cc)] = steps
                queue.append((nr, nc, steps + 1))


# Max collision is 1 less than the # of "pico" seconds you can trim off (stepping out of a wall is also 1)
def get_path_options(
    grid: list,
    start: tuple,
    end: tuple,
    target_saved: int,
    max_collision: int,
    steps_left: dict,
) -> dict:
    max_r = len(grid)
    max_c = len(grid[0])

    queue = deque([(start[0], start[1], 0, 0, 0, max_collision)])
    visited = set()
    options = {}

    while queue:
        cr, cc, pr, pc, steps, collision = queue.popleft()

        # Anything past our target we don’t care about.
        if steps > target_saved:
            return options

        if (cr, cc, steps, collision) in visited:
            continue

        visited.add((cr, cc, steps, collision))

        # If we've reached the end
        if (cr, cc) == end:
            options[steps] = options.get(steps, 0) + 1
            continue  # Continue to explore other paths

        # If a shorter path to the end has been found
        # Idk why this isn't working
        # if collision < max_collision and steps_left.get((cr, cc), None):
        #     options[steps + steps_left[(cr, cc)]] = (
        #         options.get(steps + steps_left[(cr, cc)], 0) + 1
        #     )
        #     continue

        for dir in directions_plus:
            nr, nc = cr + dir[0], cc + dir[1]

            if (
                in_bounds(max_r, max_c, (nr, nc))
                and grid[nr][nc] == "#"
                and collision > 0
                and (nr, nc) != (pr, pc)
            ):
                queue.append((nr, nc, cr, cc, steps + 1, collision - 1))

            elif in_bounds(max_r, max_c, (nr, nc)) and grid[nr][nc] != "#":
                queue.append((nr, nc, cr, cc, steps + 1, collision))

    return options


def part_1():
    with open(INPUT_PATH) as file:
        grid = string_to_grid(file.read())
        start = find_first_str_in_matrix(grid, "S")
        end = find_first_str_in_matrix(grid, "E")
        shortest = get_shortest_path(grid, start, end)
        options = get_path_options(grid, start, end, shortest - 100)
        total = 0
        for o in options.values():
            total += o
        print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        grid = string_to_grid(file.read())
        start = find_first_str_in_matrix(grid, "S")
        end = find_first_str_in_matrix(grid, "E")
        shortest = get_shortest_path(grid, start, end)
        options = get_path_options(grid, start, end, shortest - 100, 20)
        total = 0
        for o in options.values():
            total += o
        print("Part 2: " + str(total))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
