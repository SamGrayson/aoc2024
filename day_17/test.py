import time
import unittest

from day_17.main import run_program, run_program_for_test, run_program_literal

register_map = {"A": 729, "B": 0, "C": 0}
# 2024 is the start though..
register_repeat = {"A": 117440, "B": 0, "C": 0}

program = "0,1,5,4,3,0"
repeat_program = "0,3,5,4,3,0"


class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True, True)

    def test_read(self):
        output = run_program(729, program)
        self.assertEqual(output, "4,6,3,5,6,3,5,2,1,0")

    def test_repeat(self):
        output = run_program(117440, repeat_program)
        self.assertEqual(output, repeat_program)

    def test_repeat_find(self):
        p_l = [int(p) for p in repeat_program.split(",")]
        output = run_program_for_test(p_l)
        self.assertEqual(output, 117440)

    def test_find_num(self):
        found = False
        i = 0
        while not found:
            i += 1
            output = run_program(i, repeat_program)
            if output == repeat_program:
                found = i
            print(f"Staring A: {i} Output: {tuple(output)}")
        self.assertEqual(found, 117440)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
