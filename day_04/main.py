from collections import deque
import os
from utils.utils import directions_square, flip_dir, string_to_grid, directions_corners

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def is_str_dir(
    grid: list[list[str]], start: tuple[int, int], dir: tuple[int, int], term
):
    # Get bounds of grid
    row_max = len(grid)
    col_max = len(grid[0])

    # 2 more steps tops
    i = len(term) - 1
    progress = term[0]
    current_row, current_col = start
    while i > 0:
        dx, dy = dir
        new_row = current_row + dx
        new_col = current_col + dy
        current_row = new_row
        current_col = new_col
        if 0 <= new_row < row_max and 0 <= new_col < col_max:
            progress += grid[new_row][new_col]
            if progress not in term:
                return False
        else:
            return False
        i -= 1
    if progress == term:
        return True


def get_mas_x(grid: list[list[str]], start: tuple[int, int]) -> int:
    # Get bounds of grid
    row_max = len(grid)
    col_max = len(grid[0])
    current_row, current_col = start
    mas_count = 0
    for dx, dy in directions_corners:
        # If next step is in bounds, check for "xmas"
        if (
            0 <= current_row + dx < row_max
            and 0 <= current_col + dy < col_max
            and grid[current_row + dx][current_col + dy] == "m"
        ):
            if is_str_dir(
                grid, (current_row + dx, current_col + dy), flip_dir((dx, dy)), "mas"
            ):
                mas_count += 1
    return 1 if mas_count == 2 else 0


def get_xmas_x_v(grid: list[list[str]], start: tuple[int, int]) -> int:
    # Get bounds of grid
    row_max = len(grid)
    col_max = len(grid[0])
    current_row, current_col = start
    xmas_count = 0
    for dx, dy in directions_square:
        # If next step is in bounds, check for "xmas"
        if 0 <= current_row + dx < row_max and 0 <= current_col + dy < col_max:
            if is_str_dir(grid, start, (dx, dy), "xmas"):
                xmas_count += 1
    return xmas_count


def part_1():
    with open(INPUT_PATH) as file:
        input_grid = string_to_grid(file.read().lower())
    total_xmas_count = 0
    for xidx, r in enumerate(input_grid):
        for yidx, c in enumerate(r):
            if c == "x":
                total_xmas_count += get_xmas_x_v(input_grid, (xidx, yidx))
    print("Part 1: " + str(total_xmas_count))


def part_2():
    with open(INPUT_PATH) as file:
        input_grid = string_to_grid(file.read().lower())
    total_mas_x = 0
    for xidx, r in enumerate(input_grid):
        for yidx, c in enumerate(r):
            if c == "a":
                total_mas_x += get_mas_x(input_grid, (xidx, yidx))
    print("Part 2: " + str(total_mas_x))


if __name__ == "__main__":
    part_1()
    part_2()
