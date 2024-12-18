from collections import deque
import os
import time
from math import floor

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INST_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


class Computer:
    def __init__(self, register_map: dict[str, int]):
        self.register_map = register_map
        self.pointer = 0
        self.output = []

    def adv(self, input: int):
        self.register_map["A"] = floor(
            self.register_map["A"] / pow(2, self.combo(input))
        )
        self.pointer += 2

    def bxl(self, input: int):
        self.register_map["B"] = self.register_map["B"] ^ input
        self.pointer += 2

    def bst(self, input: int):
        self.register_map["B"] = self.combo(input) % 8
        self.pointer += 2

    def jnz(self, input: int):
        if self.register_map["A"] == 0:
            self.pointer += 2
            return
        self.pointer = input

    def bxc(self, _: int):
        self.register_map["B"] = self.register_map["B"] ^ self.register_map["C"]
        self.pointer += 2

    def out(self, input: int):
        out = self.combo(input) % 8
        self.output.append(out)
        self.pointer += 2

    def bdv(self, input: int):
        self.register_map["B"] = floor(
            self.register_map["A"] / pow(2, self.combo(input))
        )
        self.pointer += 2

    def cdv(self, input: int):
        self.register_map["C"] = floor(
            self.register_map["A"] / pow(2, self.combo(input))
        )
        self.pointer += 2

    def combo(self, input: int):
        c_map = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.register_map["A"],
            5: self.register_map["B"],
            6: self.register_map["C"],
            7: "NOPE",
        }
        return c_map[input]

    def call(self, instruction: int, operand: int):
        f_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        f_map[instruction](operand)


def run_program(register_map: dict[str, int], program: str):
    l_program = [int(i) for i in program.split(",")]
    computer = Computer(register_map)
    while computer.pointer < len(l_program):
        instruction, operand = (
            l_program[computer.pointer],
            l_program[computer.pointer + 1],
        )
        computer.call(instruction, operand)
    return ",".join([str(o) for o in computer.output])


def part_1():
    with open(INPUT_PATH) as _f:
        input = _f.read().replace("Program:", "").strip()
    with open(INST_PATH) as _i:
        register = {}
        for l in _i.readlines():
            split = l.replace("Register", "").strip().split(": ")
            register[split[0].strip()] = int(split[1].strip())
    result = run_program(register, input)
    print("Part 1: " + result)


def part_2():
    with open(INPUT_PATH) as file:
        print(file.read())


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    # part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
