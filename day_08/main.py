from collections import deque
from utils.utils import directions_square, string_to_grid
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def calc_multi_nodes(
    max_r: int, max_y: int, start: tuple[int, int], diff: tuple[int, int]
) -> list[tuple[int, int]]:
    # Keep going till out of bounds one way
    anti_nodes = []
    queue = deque([start])
    while len(queue) > 0:
        c_r, c_c = queue.popleft()
        n_r = c_r + diff[0]
        n_c = c_c + diff[1]
        if 0 <= n_r < max_r and 0 <= n_c < max_y:
            anti_nodes.append((n_r, n_c))
            queue.append((n_r, n_c))
    return anti_nodes


def get_antinode_options_multi(max_r, max_y, start, next) -> list[tuple[int, int]]:
    start_r, start_c = start
    next_r, next_c = next
    # Find distance between nodes
    diff = ((start_r - next_r), (start_c - next_c))

    l = calc_multi_nodes(max_r, max_y, next, diff)
    r = calc_multi_nodes(max_r, max_y, start, ((-1 * diff[0]), ((-1 * diff[1]))))

    return l + r


def get_antinode_options(
    start: tuple[int, int], next: tuple[int, int]
) -> list[tuple[int, int]]:
    start_r, start_c = start
    next_r, next_c = next
    # Find distance between nodes
    diff = ((start_r - next_r), (start_c - next_c))
    l = ((start_r + diff[0]), (start_c + diff[1]))
    r = ((next_r + (-1 * diff[0])), (next_c + (-1 * diff[1])))
    return [l, r]


def find_all_same_locations(
    grid: list[list[str]], start: tuple[int, int]
) -> list[tuple[int, int]]:
    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    start_row, start_col = start
    queue = deque([(start_row, start_col)])

    same_locations = []
    while len(queue) > 0:
        curr_row, curr_col = queue.popleft()
        directions_square

        # Skip visited
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        # If its the same antenna type, add to list
        if grid[start_row][start_col] == grid[curr_row][curr_col]:
            same_locations.append((curr_row, curr_col))

        for xr, xy in directions_square:
            new_row = curr_row + xr
            new_col = curr_col + xy
            # If in bounds, go to next step
            if 0 <= new_row < max_row and 0 <= new_col < max_col:
                queue.append((new_row, new_col))

    return same_locations


def get_all_antinodes(
    input_grid: list[list[str]], multi=False
) -> list[set[tuple[int, int]]]:
    max_row = len(input_grid)
    max_col = len(input_grid[0])

    all_antinodes = set()
    for ridx, r in enumerate(input_grid):
        for cidx, c in enumerate(r):
            if c != ".":
                locations = find_all_same_locations(input_grid, (ridx, cidx))
                start = locations[0]
                next_locations = locations[1:]
                for nl in next_locations:
                    # p1, not multi
                    if not multi:
                        antinodes = get_antinode_options(start, nl)
                        for a in antinodes:
                            # If in bounds, add:
                            if 0 <= a[0] < max_row and 0 <= a[1] < max_col:
                                all_antinodes.add(a)
                    # p2 multi
                    else:
                        max_row = len(input_grid)
                        max_col = len(input_grid[0])

                        antinodes = get_antinode_options_multi(
                            max_row, max_col, start, nl
                        )
                        for a in antinodes:
                            all_antinodes.add(a)
    return all_antinodes


def part_1():
    with open(INPUT_PATH) as file:
        input_grid = string_to_grid(file.read())
    all_antinodes = get_all_antinodes(input_grid)
    print("Part 1: " + str(len(all_antinodes)))


def part_2():
    with open(INPUT_PATH) as file:
        input_grid = string_to_grid(file.read())
    all_antinodes = get_all_antinodes(input_grid, True)
    print("Part 2: " + str(len(all_antinodes)))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
