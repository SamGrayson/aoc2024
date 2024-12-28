from collections import deque
from functools import cache
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.connections = set()

    def addConnection(self, node):
        self.connections.add(node)


# "td-yn"
def create_connection_map(connections: list[str]) -> dict:
    computers = {}
    for cc in connections:
        split = cc.split("-")
        c1: Node = computers.get(split[0], Node(split[0]))
        c2: Node = computers.get(split[1], Node(split[1]))
        computers[split[0]] = c1
        computers[split[1]] = c2
        c1.addConnection(c2)
        c2.addConnection(c1)
    return computers


# { td: yn, yn: td}
def get_connections(c_map: dict, max_c: int) -> list[tuple[str]]:

    valid_circles = set()
    visited = set()
    paths = deque([[n] for n in c_map.keys()])

    while paths:
        current_path = paths.popleft()
        last_node = current_path[-1]

        if len(current_path) == max_c + 1:
            continue

        if tuple(sorted(current_path)) in visited:
            continue
        visited.add(tuple(sorted(current_path)))

        # Get possible next nodes
        connections = c_map[last_node].connections
        for next_node in connections:
            new_path = current_path + [next_node.name]
            if next_node.name == current_path[0]:
                valid_circles.add(tuple(sorted(current_path)))
            if next_node.name not in current_path:
                new_path = current_path + [next_node.name]
                paths.append(new_path)

    return valid_circles


def all_connect(c_map: str, path: list[str], next: str) -> bool:
    for p in path:
        str_conn = [c.name for c in c_map[p].connections]
        if next not in str_conn:
            return False
    return True


# { td: yn, yn: td}
# All computers need to connect to each other in part 2...
def get_connections_all_connect(c_map: dict) -> list[tuple[str]]:

    valid_circles = set()
    visited = set()
    paths = deque([[n] for n in c_map.keys()])

    while paths:
        current_path = paths.popleft()
        last_node = current_path[-1]

        if tuple(sorted(current_path)) in visited:
            continue
        visited.add(tuple(sorted(current_path)))

        # Get possible next nodes
        connections = c_map[last_node].connections
        for next_node in connections:
            new_path = current_path + [next_node.name]
            if next_node.name == current_path[0]:
                valid_circles.add(tuple(sorted(current_path)))
            if next_node.name not in current_path and all_connect(
                c_map, current_path, next_node.name
            ):
                new_path = current_path + [next_node.name]
                paths.append(new_path)

    return valid_circles


def part_1():
    with open(INPUT_PATH) as file:
        lines = [l.strip() for l in file.readlines()]
    connection_map = create_connection_map(lines)
    connections = get_connections(connection_map, 3)
    tstart_count = 0
    for conn in connections:
        for c in conn:
            if c.startswith("t"):
                tstart_count += 1
                break  # just need to count the lines once
    print("Part 1: " + str(tstart_count))


def part_2():
    with open(INPUT_PATH) as file:
        lines = [l.strip() for l in file.readlines()]
    connection_map = create_connection_map(lines)
    connections = get_connections_all_connect(connection_map)

    max_connection = max(connections, key=lambda item: (len(item), item))

    print("Part 2: " + ",".join(max_connection))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
