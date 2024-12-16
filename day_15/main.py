import os
import time
from utils.utils import string_to_grid, directions_plus, pretty_print_grid

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INST_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


def find_at(grid: list[list[str]]) -> set:
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "@":
                return (ridx, cidx)


def get_stones_set(grid: list[list[str]]) -> set:
    stone_set = set()
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "O":
                stone_set.add((ridx, cidx))
    return stone_set


def get_box_set(grid: list[list[str]]) -> set:
    stone_set = set()
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == "[":
                stone_set.add((ridx, cidx))
    return stone_set


#  "<^^>>>vv<v>>v<<"
def get_movement(dirs: str) -> list[tuple[int, int]]:
    res = []
    for i in dirs:
        up, right, down, left = directions_plus
        if i == "^":
            res.append(up)
        if i == "<":
            res.append(left)
        if i == ">":
            res.append(right)
        if i == "v":
            res.append(down)
    return res


def can_move_box_vertical(
    grid: list[list[str]], box_start: list[tuple[int, int]], dir: tuple[int, int]
) -> bool:
    l, r = box_start[0], box_start[1]
    nlr, nlc = l[0] + dir[0], l[1] + dir[1]
    nrr, nrc = r[0] + dir[0], r[1] + dir[1]

    # If both the next values are ".", true
    if grid[nlr][nlc] == "." and grid[nrr][nrc] == ".":
        return True

    if grid[nlr][nlc] == "#" or grid[nrr][nrc] == "#":
        return False

    if grid[nlr][nlc] == "]":
        box_start_l = [(nlr, nlc - 1), (nlr, nlc)]
    if grid[nlr][nlc] == "[":
        box_start_l = [(nlr, nlc), (nlr, nlc + 1)]

    if grid[nrr][nrc] == "]":
        box_start_r = [(nrr, nrc - 1), (nrr, nrc)]
    if grid[nrr][nrc] == "[":
        box_start_r = [(nrr, nrc), (nrr, nrc + 1)]

    move_left = (
        True if grid[nlr][nlc] == "." else can_move_box_vertical(grid, box_start_l, dir)
    )
    move_right = (
        True if grid[nrr][nrc] == "." else can_move_box_vertical(grid, box_start_r, dir)
    )

    if move_left and move_right:
        return True


# Return 1 if moved, return 0 if not moved
def move(grid: list[list[str]], start: tuple[int, int], dir: tuple[int, int]) -> int:
    cr, cc = start
    nr, nc = cr + dir[0], cc + dir[1]

    curr = grid[cr][cc]
    next = grid[nr][nc]

    # If wall, nope
    if next == "#":
        return 0
    # If stone, try to move stone
    if next == "O" or ((next == "[" or next == "]") and dir in [(0, 1), (0, -1)]):
        if move(grid, (nr, nc), dir) == 1:
            grid[cr][cc] = "."
            grid[nr][nc] = curr
            return 1
        else:
            return 0

    """
    ###
    [].
    .[]
    .@.
    """
    # Big box up and down
    if next in ["[", "]"] and dir in [(1, 0), (-1, 0)]:
        if next == "]":
            box_start = [(nr, nc - 1), (nr, nc)]
        if next == "[":
            box_start = [(nr, nc), (nr, nc + 1)]
        if can_move_box_vertical(grid, box_start, dir):
            move(grid, box_start[0], dir)
            move(grid, box_start[1], dir)
            grid[cr][cc] = "."
            grid[nr][nc] = curr
            return 1
        else:
            return 0

    # else move
    if next == ".":
        grid[cr][cc] = "."
        grid[nr][nc] = curr
        return 1

    return 0


def get_gpc_calc(grid: list[list[str]]):
    gps_total = 0
    stone_set = get_stones_set(grid)
    for s in stone_set:
        gps_total += 100 * s[0] + s[1]
    return gps_total


def get_gpc_calc_boxes(grid: list[list[str]]):
    gps_total = 0
    box_set = get_box_set(grid)
    for s in box_set:
        gps_total += 100 * s[0] + s[1]
    return gps_total


def part_1():
    with open(INPUT_PATH) as file:
        grid = string_to_grid(file.read())
    with open(INST_PATH) as inst:
        instructions = "".join(inst.read().strip().split("\n"))
    dirs = get_movement(instructions)

    start = find_at(grid)
    for m in dirs:
        result = move(grid, start, m)
        if result == 1:
            start = (start[0] + m[0], start[1] + m[1])

    gps_calc = get_gpc_calc(grid)

    print("Part 1: " + str(gps_calc))


def part_2():
    with open(INPUT_PATH) as file:
        input = file.read()
        # Widen
        input = input.replace("#", "##")
        input = input.replace("O", "[]")
        input = input.replace(".", "..")
        input = input.replace("@", "@.")

        grid = string_to_grid(input)
    with open(INST_PATH) as inst:
        instructions = "".join(inst.read().strip().split("\n"))
    dirs = get_movement(instructions)
    start = find_at(grid)
    for m in dirs:
        result = move(grid, start, m)
        if result == 1:
            start = (start[0] + m[0], start[1] + m[1])
        # pretty_print_grid(grid)

    gps_calc = get_gpc_calc_boxes(grid)

    print("Part 2: " + str(gps_calc))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
