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
    string_to_grid,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def dijkstra_shortest(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
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
    pq = [(0, (start, (0, 1)))]
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

        return shortest_distances, previous_nodes

    distances, nodes = add_scoring()

    return distances[end]


def part_1():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())
        start = find_first_str_in_matrix(input, "S")
        end = find_first_str_in_matrix(input, "E")
        lowest = dijkstra_shortest(input, start, end)
        print("Part 1: " + str(lowest))


def part_2():
    with open(INPUT_PATH) as file:
        input = string_to_grid(file.read())


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
