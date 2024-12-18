from heapq import heapify, heappop, heappush
from math import inf
import os
import time
from collections import deque
from utils.utils import (
    directions_plus,
    find_first_str_in_matrix,
    flip_dir,
    in_bounds,
    pretty_print_grid,
    string_to_grid,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def dijkstra_shortest(
    grid: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
    start_dir=(0, 1),
):
    graph = {}

    def create_weighted_graph():
        for ridx, r in enumerate(grid):
            for cidx, c in enumerate(r):
                if c == "#":
                    continue
                node = (ridx, cidx)
                graph[node] = {}

        # Connections
        for ridx, r in enumerate(grid):
            for cidx, c in enumerate(r):
                if c == "#":
                    continue
                curr_node = (ridx, cidx)

                for dir in directions_plus:
                    xr, xc = dir
                    new_row = ridx + xr
                    new_col = cidx + xc

                    if in_bounds(len(grid), len(grid[0]), (new_row, new_col)):
                        if grid[new_row][new_col] != "#":
                            new_node = (new_row, new_col)
                            graph[curr_node][new_node] = float("inf")

    # Initialize a priority queue
    pq = [(0, (start, start_dir))]
    heapify(pq)
    create_weighted_graph()

    # Dictionary to store the shortest distance to each node
    shortest_distances = {node: float("inf") for node in graph}
    shortest_distances[start] = 0

    # Dictionary to track the previous node (for reconstructing paths if needed)
    previous_nodes = {node: None for node in graph}

    def add_scoring():
        while pq:
            current_distance, pop = heappop(pq)
            current_node, prev_dir = pop

            # Skip processing if a better path was already found
            if current_distance > shortest_distances[current_node]:
                continue

            # Process all neighbors
            for n in graph[current_node]:
                if n == current_node:
                    continue

                # Calculate direction and weight
                dir = (n[0] - current_node[0], n[1] - current_node[1])

                # Base weight is 1, add 1000 if changing direction
                weight = 1
                if prev_dir is not None and dir != prev_dir:
                    weight = 1001

                distance = current_distance + weight

                # Update if we found a better path
                if distance < shortest_distances[n]:
                    shortest_distances[n] = distance
                    previous_nodes[n] = current_node
                    heappush(pq, (distance, (n, dir)))

        return shortest_distances

    distances = add_scoring()

    unique_nodes = set([end])
    queue = deque([end])
    while queue:
        curr = queue.pop()
        if curr:
            next = previous_nodes[curr]
            if next:
                unique_nodes.add(next)
                queue.append(next)

    return distances[end], unique_nodes


def part_1():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
        start = find_first_str_in_matrix(input, "S")
        end = find_first_str_in_matrix(input, "E")
        lowest, u_nodes = dijkstra_shortest(input, start, end)
        valid_p = list(u_nodes)
        valid_p.reverse()
        prev_dir = (0, 1)
        for idx, curr in enumerate(valid_p):
            if idx == len(valid_p) - 1:
                break
            next = valid_p[idx + 1]
            lowest_true, _ = dijkstra_shortest(input, next, end, prev_dir)
            for dir in directions_plus:
                p = (curr[0] + dir[0], curr[1] + dir[1])
                if input[p[0]][p[1]] == "#":
                    continue
                if p not in u_nodes:
                    lowest, new_nodes = dijkstra_shortest(input, p, end, prev_dir)
                if lowest == lowest_true:
                    u_nodes = u_nodes.union(new_nodes)
            prev_dir = (next[0] - curr[0], next[1] - curr[1])

        for n in u_nodes:
            input[n[0]][n[1]] = "O"
        pretty_print_grid(input)

        print("Part 1: " + str(lowest))
        print("Part 2: " + str(len(u_nodes)))


def part_2():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
