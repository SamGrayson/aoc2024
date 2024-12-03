import os
import re
from functools import reduce
from operator import mul

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

def get_muls(input: str) -> list[str]:
  mul_regex = r"mul\(\d{0,3},\d{0,3}\)"
  return re.findall(mul_regex, input)


def get_dos(input: str) -> list[str]:
  first_dos_regex=r"^.*?(?=don't\(\)|do)"
  do_dont_regex=r"(?<=do\(\)).*?(?=don't\(\)|$)"
  
  start = re.findall(first_dos_regex, input)
  all_dos = re.findall(do_dont_regex, input)
  
  return start + all_dos


def do_muls(muls: list[str]) -> list[int]:
  digit_regex = r"\d{0,3},\d{0,3}"
  mul_results = []
  for m in muls:
    nums = map(int, re.search(digit_regex, m).group(0).split(","))
    mul_results.append(reduce(mul, nums))
  return mul_results


def part_1():
    input = ""
    with open(INPUT_PATH) as file:
        input = file.read()
    muls = get_muls(input)
    mul_results = do_muls(muls)
    print("Part 1: "+ str(sum(mul_results)))
    

def part_2():
    input = ""
    with open(INPUT_PATH) as file:
        input = "".join(file.read().splitlines())        
    do_list = get_dos(input)
    muls = get_muls("".join(do_list))
    mul_results = do_muls(muls)
    print("Part 2: " + str(sum(mul_results)))


if __name__ == "__main__":
    part_1()
    part_2()
