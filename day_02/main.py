from copy import copy
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

def is_safe(l: list[int]) -> bool:
  i = 1
  curr = l[0]
  dir_check=[]
  while i < len(l) and not len(set(dir_check)) > 1:
    if curr > l[i]:
      dir_check.append("asc")
    if curr < l[i]:
      dir_check.append("desc")
    # No change? false
    if curr == l[i]:
      return False
    # If next item is abs > 3, go ahead and exit anyway as false
    if abs(curr - l[i]) > 3:
      return False
    curr=l[i]
    i+=1
  return len(set(dir_check)) == 1

def allow_failure_is_safe(l: list[int]) -> bool:
  for idx, i in enumerate(l):
    fresh = l[:]
    fresh.pop(idx)
    if is_safe(fresh):
      return True
  return False

def part_1():
    test_lines = []
    with open(INPUT_PATH) as file:
        for line in file:
          test_lines.append(list(map(int, line.split(" "))))
    total_safe = 0
    for t in test_lines:
      safe = is_safe(t)
      if safe:
        total_safe+=1
    print("Part 1: ", total_safe)


def part_2():
    test_lines = []
    with open(INPUT_PATH) as file:
        for line in file:
          test_lines.append(list(map(int, line.split(" "))))
    total_safe = 0
    for t in test_lines:
      safe = allow_failure_is_safe(t)
      if safe:
        total_safe+=1
    print("Part 2: ", total_safe)


if __name__ == "__main__":
    part_1()
    part_2()
