from collections import deque
import os
import time

from utils.utils import in_bounds, string_to_grid, directions_plus, manhattan_distance

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


num_pad = string_to_grid(
    """
789
456
123
X0A
"""
)

num_pad_local = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "X": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}
num_pad_local_str = {value: key for key, value in num_pad_local.items()}

dir_pad = string_to_grid(
    """
X^A
<v>
"""
)

dir_pad_local = {
    "X": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
dir_pad_local_str = {value: key for key, value in dir_pad_local.items()}


UP, RIGHT, DOWN, LEFT = directions_plus
DIR_MAP = {"^": UP, ">": RIGHT, "v": DOWN, "<": LEFT}
DIR_MAP_STR = {UP: "^", RIGHT: ">", DOWN: "v", LEFT: "<"}


def recur_shortest(
    value: str,
    max_depth: int = 1,
    rtype: str = "NUM",
    start: str = "A",
    depth: int = 0,
) -> str:
    if max_depth == depth:
        return value

    shortest = ""
    start = "A"
    # 029A
    # <A^A^^>AvvvA
    # v<<A>>^A<A>AvA<^AA>A<vAAA>^A
    for c in value:
        if rtype == "NUM":
            paths = find_next_paths_in_grid_num(num_pad_local, num_pad, start, c)
        if rtype == "DIR":
            paths = find_next_paths_in_grid_dir(dir_pad_local, dir_pad, start, c)
        for idx, p in enumerate(paths):
            paths[idx] = recur_shortest((p + "A"), max_depth, "DIR", "A", depth + 1)
        shortest += sorted(paths, key=len)[0]
        start = c

    return shortest


def find_next_paths_in_grid_num(
    test_grid_local: dict,
    test_grid: list[list[str]],
    start: str,
    target: str,
):
    max_r = len(test_grid)
    max_c = len(test_grid[0])
    start = test_grid_local[start]
    end = test_grid_local[target]
    queue = deque([(start[0], start[1], "")])
    paths = []
    short_len = None
    visited = set()
    while queue:
        cr, cc, path = queue.popleft()
        if (cr, cc, path) in visited:
            continue
        visited.add((cr, cc, path))
        if short_len and len(path) > short_len:
            continue
        if (cr, cc) == end:
            paths.append(path)
            short_len = len(path)
            continue
        # Reordering due to the weight of each away from A - left buttons are farthest from "A"
        for dir in [RIGHT, UP, DOWN, LEFT]:
            nr, nc = cr + dir[0], cc + dir[1]
            if in_bounds(max_r, max_c, (nr, nc)) and test_grid[nr][nc] != "X":
                queue.append(
                    (
                        nr,
                        nc,
                        path + DIR_MAP_STR[dir],
                    )
                )
    return paths


def find_next_paths_in_grid_dir(
    test_grid_local: dict,
    test_grid: list[list[str]],
    start: str,
    target: str,
):
    max_r = len(test_grid)
    max_c = len(test_grid[0])
    start = test_grid_local[start]
    end = test_grid_local[target]
    queue = deque([(start[0], start[1], "", 0, (start[0], start[1]))])
    shortest_pdist = None
    shortest_path = None
    visited = set()
    paths = []
    while queue:
        # pdist is the distance to "A" from the next point on the grid..
        cr, cc, path, pdist, prev_dir = queue.popleft()
        if (cr, cc, path) in visited:
            continue
        visited.add((cr, cc, path))
        # Go ahead and exit if current path is shorter than shortest path found
        if shortest_path and len(path) > len(shortest_path):
            continue
        if (cr, cc) == end:
            # If no path set yet, set stuff
            if not shortest_path:
                shortest_path = path
                shortest_pdist = pdist
                paths.append(path)
                continue
            # If paths are the same, but one pdist is less than another - set it
            if len(path) == len(shortest_path) and pdist <= shortest_pdist:
                shortest_path = path
                shortest_pdist = pdist
                paths.append(path)
                continue
            # If paths are the same, but one pdist is higher than another - skip
            if len(path) == len(shortest_path) and pdist > shortest_pdist:
                continue
            continue
        # Reordering due to the weight of each away from A - left buttons are farthest from "A"
        for dir in [RIGHT, UP, DOWN, LEFT]:
            nr, nc = cr + dir[0], cc + dir[1]
            if in_bounds(max_r, max_c, (nr, nc)) and test_grid[nr][nc] != "X":
                queue.append(
                    (
                        nr,
                        nc,
                        path + DIR_MAP_STR[dir],
                        pdist
                        + manhattan_distance(
                            dir_pad_local[DIR_MAP_STR[dir]],
                            prev_dir,
                        ),
                        dir_pad_local[DIR_MAP_STR[dir]],
                    )
                )
    return paths


def part_1():
    with open(INPUT_PATH) as file:
        total = 0
        for l in file.readlines():
            path = recur_shortest(l.strip(), 3)
            total += len(path) * int(l.replace("A", ""))
    print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        total = 0
        for idx, l in enumerate(file.readlines()):
            path = recur_shortest(l.strip(), 26)
            total += len(path) * int(l.replace("A", ""))
            print(str(idx + 1) + "complete: " + total)
    print("Part 2: " + str(total))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
