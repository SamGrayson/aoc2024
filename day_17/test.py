import time
import unittest

from day_17.main import run_program

register_map = {"A": 729, "B": 0, "C": 0}

program = "0,1,5,4,3,0"


class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True, True)

    def test_read(self):
        output = run_program(register_map, program)
        self.assertEqual(output, "4,6,3,5,6,3,5,2,1,0")


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
