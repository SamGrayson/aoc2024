from collections import deque
from functools import cache
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


def do_it(test: str, max_depth: int):
    dir_path_map = {}

    @cache
    def recur_shortest(
        value: str,
        max_depth: int = 1,
        rtype: str = "NUM",
        start: str = "A",
        depth: int = 0,
    ) -> str:
        if max_depth == depth:
            return len(value)

        shortest = 0
        start = "A"
        for c in value:
            if rtype == "NUM":
                paths = find_next_paths_in_grid_num(start, c)
            else:
                if (start, c) in dir_path_map:
                    paths = dir_path_map[(start, c)]
                else:
                    paths = find_next_paths_in_grid_dir(start, c)

            totals = []
            for p in paths:
                totals.append(
                    recur_shortest((p + "A"), max_depth, "DIR", "A", depth + 1)
                )

            shortest += min(totals)
            start = c

        return shortest

    def find_next_paths_in_grid_num(
        start: str,
        target: str,
    ):
        max_r = len(num_pad)
        max_c = len(num_pad[0])
        start = num_pad_local[start]
        end = num_pad_local[target]
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
                if in_bounds(max_r, max_c, (nr, nc)) and num_pad[nr][nc] != "X":
                    queue.append(
                        (
                            nr,
                            nc,
                            path + DIR_MAP_STR[dir],
                        )
                    )
        return paths

    def find_next_paths_in_grid_dir(
        start: str,
        target: str,
    ):
        max_r = len(dir_pad)
        max_c = len(dir_pad[0])
        start = dir_pad_local[start]
        end = dir_pad_local[target]
        queue = deque([(start[0], start[1], "")])
        shortest_path = None
        visited = set()
        paths = []
        while queue:
            cr, cc, path = queue.popleft()
            if (cr, cc, path) in visited:
                continue
            visited.add((cr, cc, path))
            # # Go ahead and exit if current path is shorter than shortest path found
            if shortest_path and (len(path) > len(shortest_path)):
                continue
            if (cr, cc) == end:
                # If no path set yet, set stuff
                paths.append(path)
                if not shortest_path:
                    shortest_path = path
                    paths.append(path)
                    continue
                if len(path) <= len(shortest_path):
                    shortest_path == path
            # Reordering due to the weight of each away from A - left buttons are farthest from "A"
            for dir in [UP, RIGHT, DOWN, LEFT]:
                nr, nc = cr + dir[0], cc + dir[1]
                if in_bounds(max_r, max_c, (nr, nc)) and dir_pad[nr][nc] != "X":
                    queue.append((nr, nc, path + DIR_MAP_STR[dir]))
        dir_path_map[(start, target)] = paths
        return paths

    return recur_shortest(test, max_depth)


def part_1():
    with open(INPUT_PATH) as file:
        total = 0
        for l in file.readlines():
            path_count = do_it(l.strip(), 3)
            total += path_count * int(l.replace("A", ""))
    print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        total = 0
        for idx, l in enumerate(file.readlines()):
            path_count = do_it(l.strip(), 26)
            total += path_count * int(l.replace("A", ""))
    print("Part 2: " + str(total))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
