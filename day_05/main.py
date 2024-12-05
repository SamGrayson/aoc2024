import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")
INSTRUCTIONS_PATH = os.path.join(SCRIPT_DIR, "instructions.txt")


def create_instruction(ins: str) -> tuple[int, int]:
    split = ins.split("|")
    return (int(split[0]), int(split[1]))


def is_correct(instruction_list: set[str], test: str) -> bool:
    ints = [int(x) for x in test.split(",")]
    pairs = [(ints[i], ints[i + 1]) for i in range(len(ints) - 1)]
    return all(map(lambda x: x in instruction_list, pairs))


def fix_line(instruction_list: set[str], test: str) -> str:
    split = test.split(",")
    fixed = False
    while not fixed:
        # Get original idx
        idx_replace = len(split) - 1
        char_test = split[-1]
        for i, e in reversed(list(enumerate(split))):
            # Don't compare with self
            if i == len(split) - 1:
                continue
            if (int(char_test), int(e)) in instruction_list:
                idx_replace = i
            # At beginning, replace then try again
            if i == 0:
                split.pop()
                split.insert(idx_replace, char_test)
                break
        # Make sure all items are in the correct spot
        for i, e in reversed(list(enumerate(split))):
            # We made it to the end with no errors
            if i == 0:
                fixed = True
                break
            if (int(e), int(split[i - 1])) in instruction_list:
                split.append(split.pop(i))
                break

    return ",".join(split)


def get_middle(test: str) -> int:
    split = test.split(",")
    middle = split[len(split) // 2]
    return int(middle)


def part_1():
    instructions = set()
    with open(INSTRUCTIONS_PATH) as file:
        for i in file:
            instructions.add(create_instruction(i))

    with open(INPUT_PATH) as file:
        # Test each input and see if correct
        middle_sum = 0
        for input in file:
            if is_correct(instructions, input):
                middle_sum += get_middle(input)
        print("Part 1: " + str(middle_sum))


def part_2():
    instructions = set()
    with open(INSTRUCTIONS_PATH) as file:
        for i in file:
            instructions.add(create_instruction(i))

    with open(INPUT_PATH) as file:
        # Test each input and see if correct
        middle_sum = 0
        for input in file:
            if not is_correct(instructions, input):
                fixed = fix_line(instructions, input)
                middle_sum += get_middle(fixed)
        print("Part 2: " + str(middle_sum))


if __name__ == "__main__":
    part_1()
    part_2()
