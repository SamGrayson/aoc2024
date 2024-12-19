from collections import deque
import os
import time

from utils.utils import create_matrix, directions_plus, in_bounds

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def create_grid(grid_size, byte_coords: list[tuple[int, int]], limit):
    grid = create_matrix(grid_size + 1, grid_size + 1)
    i = 0
    for byte in byte_coords:
        if i == limit:
            break
        i += 1
        x, y = byte
        grid[y][x] = "#"
    return grid


def navigate_grid(grid: list[list[str]]):
    max_r = len(grid)
    max_c = len(grid[0])
    end = (max_r - 1, max_c - 1)
    queue = deque([(0, 0, 0)])
    visited = set()
    while queue:
        cr, cc, steps = queue.popleft()
        if (cr, cc) == end:
            return steps
        if (cr, cc) in visited:
            continue
        visited.add((cr, cc))
        for dir in directions_plus:
            nr, nc = cr + dir[0], cc + dir[1]
            if in_bounds(max_r, max_c, (nr, nc)) and grid[nr][nc] != "#":
                queue.append((nr, nc, steps + 1))
    return -1


def part_1():
    with open(INPUT_PATH) as file:
        test = [tuple(map(int, l.strip().split(","))) for l in file.readlines()]
        grid = create_grid(70, test, 1024)
        shortest = navigate_grid(grid)
        print("Part 1: " + str(shortest))


def part_2():
    with open(INPUT_PATH) as file:
        test = [tuple(map(int, l.strip().split(","))) for l in file.readlines()]
        for i in range(len(test)):
            grid = create_grid(70, test, i)
            shortest = navigate_grid(grid)
            if shortest == -1:
                print("Part 2: " + str(test[i - 1]))
                return


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
