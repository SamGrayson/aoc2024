from collections import deque
import os
import time
from utils.utils import in_bounds, string_to_grid, directions_plus

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def get_range_score(grid: list[list[str]], start: tuple[int, int], each=False) -> int:
    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    start_row, start_col = start
    queue = deque([(start_row, start_col)])

    score = 0
    while len(queue) > 0:
        cr, cc = queue.popleft()
        curr_value = int(grid[cr][cc])
        if (cr, cc) in visited:
            continue
        if curr_value == 9:
            # We only care about the 9s being visited
            if not each:
                visited.add((cr, cc))
            score += 1
            continue
        for dir in directions_plus:
            nr, nc = cr + dir[0], cc + dir[1]
            if (
                in_bounds(max_row, max_col, (nr, nc))
                and int(grid[nr][nc]) == curr_value + 1
            ):
                queue.append((nr, nc))
    return score


def get_total_range_score(grid: list[list[str]], each=False) -> int:
    total_score = 0
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "0":
                total_score += get_range_score(grid, (ridx, cidx), each)
    return total_score


def part_1():
    with open(INPUT_PATH) as file:
        print("Part 1: " + str(get_total_range_score(string_to_grid(file.read()))))


def part_2():
    with open(INPUT_PATH) as file:
        print(
            "Part 2: " + str(get_total_range_score(string_to_grid(file.read()), True))
        )


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
