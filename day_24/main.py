from collections import deque
import os
import time
from graphviz import Digraph

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INSTRUCTIONS_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


class Gate:
    def __init__(self, l, opp, r, eq):
        self.l: str = l
        self.opp: str = opp
        self.r: str = r
        self.eq: str = eq


def parse_input(gates: list[str]):
    # "x00 AND y00 -> z00"
    parsed = []
    for g in gates:
        split = g.split(" ")
        parsed.append(Gate(split[0], split[1], split[2], split[4]))
    return parsed


def do_gate(wires: dict, gate: Gate):
    # AND
    if gate.opp == "AND":
        value = 1 if (wires[gate.l] == 1 and wires[gate.r] == 1) else 0
    # OR
    if gate.opp == "OR":
        value = 1 if (wires[gate.l] == 1 or wires[gate.r] == 1) else 0
    # XOR
    if gate.opp == "XOR":
        value = 1 if (wires[gate.l] != wires[gate.r]) else 0

    wires[gate.eq] = value


def get_wire_bits(wires: dict, wire: str):
    bits = deque([])
    s_wires = dict(sorted(wires.items()))
    for k, v in s_wires.items():
        if k.startswith(wire):
            bits.appendleft(str(v))
    return "".join(bits)


def get_bits(wires: dict, gates: list[Gate], starts_with: str) -> str:
    # Have to wait until both values exist in the map

    x_bits = get_wire_bits(wires, "x")
    y_bits = get_wire_bits(wires, "y")

    queue = deque(gates)
    bits = deque([])
    while queue:
        gate = queue.popleft()
        if gate.l in wires and gate.r in wires:
            do_gate(wires, gate)
        # add back to the queue
        else:
            queue.append(gate)

    s_wires = dict(sorted(wires.items()))
    for k, v in s_wires.items():
        if k.startswith(starts_with):
            bits.appendleft(str(v))

    return "".join(bits)


# Call after the initial run
def create_wire_graph(wires: dict, gates: list[Gate]):
    dot = Digraph("graph")

    opp_colors = {"AND": "blue", "OR": "purple", "XOR": "green"}

    # Points
    for p in wires.keys():
        dot.node(p, p, shape="circle")

    # All my gates
    for g in gates:
        dot.node(
            f"{g.l} {g.opp} {g.r}", f"{g.opp}", shape="rect", color=opp_colors[g.opp]
        )
        # z must be solved with xor - unless at end
        if g.eq != "z45" and g.opp != "XOR" and g.eq.startswith("z"):
            dot.edge(f"{g.l} {g.opp} {g.r}", g.eq, color="red")
            print("BAD OUTPUT TO Z: " + g.eq)
        # only xs & ys can have xor opp
        elif (
            g.opp == "XOR"
            and not g.eq.startswith("z")
            and (not (g.l.startswith("x") or g.l.startswith("y")))
            and (not (g.r.startswith("x") or g.r.startswith("y")))
        ):
            dot.edge(f"{g.l} {g.opp} {g.r}", g.eq, color="red")
            print("BAD INPUT TO XOR: " + g.eq)
        else:
            dot.edge(f"{g.l} {g.opp} {g.r}", g.eq)

        dot.edges([(g.l, f"{g.l} {g.opp} {g.r}"), (g.r, f"{g.l} {g.opp} {g.r}")])

    # with dot.subgraph() as sub:
    #     sub.attr(rank="same")  # Force the same rank
    #     for wire in wires.keys():
    #         if wire.startswith("z"):
    #             sub.node(wire)

    dot = dot.unflatten(stagger=3)

    dot.render("graph", format="png", cleanup=True, directory=SCRIPT_DIR)


def part_1():
    with open(INSTRUCTIONS_PATH) as file:
        raw_gates = [l.strip() for l in file.readlines()]
        gates = parse_input(raw_gates)
    with open(INPUT_PATH) as file:
        wires = {}
        for l in file.readlines():
            split = l.strip().split(": ")
            wires[split[0]] = int(split[1])
    bits = get_bits(wires, gates, "z")
    print("Part 1: " + str(int(bits, 2)))


# Going to attempt by hand with some smart hints along the way??
def part_2():
    with open(INSTRUCTIONS_PATH) as file:
        raw_gates = [l.strip() for l in file.readlines()]
        gates = parse_input(raw_gates)
    with open(INPUT_PATH) as file:
        wires = {}
        for l in file.readlines():
            split = l.strip().split(": ")
            wires[split[0]] = int(split[1])
    get_bits(wires, gates, "z")
    create_wire_graph(wires, gates)


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
