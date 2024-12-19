from collections import deque
import os
import time
from math import floor

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INST_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


class Computer:
    def __init__(self, a):
        self.register_map = {"A": a, "B": 0, "C": 0}
        self.pointer = 0
        self.output = []

    def set_map(self, a: int, b: int, c: int):
        if a:
            self.register_map["A"] = a
        if b:
            self.register_map["B"] = b
        if c:
            self.register_map["C"] = c

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
        return


def run_program(a: int, program: str):
    l_program = [int(i) for i in program.split(",")]
    computer = Computer(a)
    while computer.pointer < len(l_program):
        instruction, operand = (
            l_program[computer.pointer],
            l_program[computer.pointer + 1],
        )
        computer.call(instruction, operand)
    return ",".join([str(o) for o in computer.output])


def run_program_literal(program: list[int], res=0):
    if not program:
        return res

    # All possible numbers (0 - 8)
    for i in range(8):
        test = (res << 3) + i
        a = test
        b = a % 8  # bst
        b = b ^ 3  # bxl
        c = a >> b  # cdv
        a = a >> 3  # adv
        b = b ^ 5  # bxl
        b = b ^ c  # bxc
        if b % 8 == program[-1]:  # out
            # add back in the a >> 3 since that has to be the incoming value
            sub = run_program_literal(program[:-1], test)
            if not sub:
                continue
            return sub


# "0,3,5,4,3,0"
def run_program_for_test(program: list[int], res=0):
    if not program:
        # Idk why we do it an extra time..
        return res

    # All possible numbers (0 - 8)
    for i in range(8):
        test = (res << 3) + i
        a = test
        a = a >> 3
        if a % 8 == program[-1]:  # out
            # add back in the a >> 3 since that has to be the incoming value
            sub = run_program_for_test(program[:-1], test)
            if not sub:
                continue
            return sub


def part_1():
    with open(INPUT_PATH) as _f:
        input = _f.read().replace("Program:", "").strip()
    with open(INST_PATH) as _i:
        register = {}
        for l in _i.readlines():
            split = l.replace("Register", "").strip().split(": ")
            register[split[0].strip()] = int(split[1].strip())
    result = run_program(register["A"], input)
    print("Part 1: " + result)


def part_2():
    with open(INPUT_PATH) as _f:
        input = _f.read().replace("Program:", "").strip()
    with open(INST_PATH) as _i:
        register = {}
        for l in _i.readlines():
            split = l.replace("Register", "").strip().split(": ")
            register[split[0].strip()] = int(split[1].strip())

    program = [int(p) for p in input.split(",")]
    res = run_program_literal(program, 0)

    print("Part 2: " + str(res))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
