from collections import deque
from utils.utils import (
    directions_plus,
    find_first_str_in_matrix,
    in_bounds,
    manhattan_distance,
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
# BFS super slow for part 1
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


# Refactor for part 2
def find_all_cheats(grid: list[list[str]], race_route: dict, max_collision: int):
    route_list = list(race_route.keys())
    end = route_list[-1]
    options = {}
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "#":
                continue
            if c == "E":
                print("Done")
            curr_idx = route_list.index((ridx, cidx))
            for p in route_list[curr_idx:]:
                man_distance = manhattan_distance((ridx, cidx), p)
                if man_distance > 0 and man_distance <= max_collision:
                    steps_to_point = race_route[(ridx, cidx)]
                    steps_to_next = man_distance
                    steps_to_end = (
                        race_route[end]
                        - race_route[p]
                        + (steps_to_point + steps_to_next)
                    )
                    time_saved = race_route[end] - steps_to_end
                    if time_saved > 0:
                        options[time_saved] = options.get(time_saved, 0) + 1
    return options


def part_1():
    with open(INPUT_PATH) as file:
        grid = string_to_grid(file.read())
        start = find_first_str_in_matrix(grid, "S")
        end = find_first_str_in_matrix(grid, "E")
        path = get_shortest_path(grid, start, end)
        options = find_all_cheats(grid, path, 100, 2)
        total = 0
        for k, v in sorted(options.items()):
            if k < 100:
                continue
            if k >= 100:
                total += v
        print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        grid = string_to_grid(file.read())
        start = find_first_str_in_matrix(grid, "S")
        end = find_first_str_in_matrix(grid, "E")
        path = get_shortest_path(grid, start, end)
        # Need to figure out when to cut off..
        options = find_all_cheats(grid, path, 100, 20)
        total = 0
        for k, v in sorted(options.items()):
            if k < 100:
                continue
            if k >= 100:
                total += v
        print("Part 2: " + str(total))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
