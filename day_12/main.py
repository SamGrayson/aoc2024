import os
import time
from utils.utils import directions_plus, directions_square, in_bounds, string_to_grid
from collections import deque

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


# Check if all items in list are letter
def check_letter(li: list, letter):
    return any(map(lambda c: c == letter, li))


# make a square around the point, check all the characters
def get_total_shape_sides(grid: list[list[str]], visited: list) -> int:
    # Individual polys have 4 corners
    if len(visited) == 1:
        return 4

    corners = 0
    for coord in visited:
        letter_test = grid[coord[0]][coord[1]]
        values = []
        for dir in directions_square:
            if in_bounds(
                len(grid), len(grid[0]), (coord[0] + dir[0], coord[1] + dir[1])
            ):
                values.append(grid[coord[0] + dir[0]][coord[1] + dir[1]])
            else:
                values.append(None)

        top_l, top, top_r, left, right, bottom_l, bottom, bottom_r = values

        """
        a.a
        .aa
        a.a
        """
        # All the singular line ends
        if right == letter_test and not check_letter([top, left, bottom], letter_test):
            corners += 2
        if left == letter_test and not check_letter([top, right, bottom], letter_test):
            corners += 2
        if top == letter_test and not check_letter([left, right, bottom], letter_test):
            corners += 2
        if bottom == letter_test and not check_letter([top, left, right], letter_test):
            corners += 2

        # Check all the criteria for corners (probably a lot)
        # Outer corners
        """
        ....
        .aa.
        .a..
        ....
        """
        if (
            right == letter_test
            and bottom == letter_test
            and not check_letter([top, left], letter_test)
        ):
            corners += 1
        if right == letter_test and bottom == letter_test and bottom_r != letter_test:
            corners += 1
        """
        ....
        ..a.
        .aa.
        ...a
        """
        if (
            left == letter_test
            and top == letter_test
            and not check_letter([bottom, right], letter_test)
        ):
            corners += 1
        if left == letter_test and top == letter_test and top_l != letter_test:
            corners += 1
        """
        ....
        .aa.
        ..a.
        ....
        """
        if (
            bottom == letter_test
            and left == letter_test
            and not check_letter([top, right], letter_test)
        ):
            corners += 1
        if bottom == letter_test and left == letter_test and bottom_l != letter_test:
            corners += 1
        """
        ....
        .a.
        .aa.
        ....
        """
        if (
            top == letter_test
            and right == letter_test
            and not check_letter([left, bottom], letter_test)
        ):
            corners += 1
        if top == letter_test and right == letter_test and top_r != letter_test:
            corners += 1

    return corners


def get_all_region_prices(grid):
    # Scan grid for starting points, keep track of all visited nodes from get_a_p
    total_price = 0
    total_side_price = 0
    all_visited = set()
    for ridx, r in enumerate(grid):
        for cidx, _ in enumerate(r):
            if (ridx, cidx) not in all_visited:
                a, p, visited = get_a_p(grid, (ridx, cidx))
                all_visited = all_visited.union(visited)
                total_side_price += a * get_total_shape_sides(grid, visited)
                total_price += a * p
                # Get total side price
    return total_price, total_side_price


def get_a_p(grid: list[list[str]], start: tuple[int, int]) -> tuple[int, int, set]:
    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    queue = deque([start])
    letter = grid[start[0]][start[1]]

    t_p = 0
    while len(queue) > 0:
        curr_row, curr_col = queue.popleft()
        # Each new letter adds to area

        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        neighbor = []
        for xr, xy in directions_plus:
            new_row = curr_row + xr
            new_col = curr_col + xy
            # If in bounds and not visited and letter match, add to queue
            if (
                0 <= new_row < max_row
                and 0 <= new_col < max_col
                and letter == grid[new_row][new_col]
            ):
                neighbor.append((new_row, new_col))
                # Skip visited - further down to account for neighbor count
                if (new_row, new_col) in visited:
                    continue
                visited.add((curr_row, curr_col))
                queue.append((new_row, new_col))

        neighbors = len(neighbor)

        # Add the perimeter
        t_p += 4 - neighbors

    return len(visited), t_p, visited


def main():
    with open(INPUT_PATH) as file:
        p1, p2 = get_all_region_prices(string_to_grid(file.read().strip()))
        print("Part 1: " + str(p1))
        print("Part 2: " + str(p2))


# def part_2():
#     with open(INPUT_PATH) as file:
#         print(file.read())


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
