import time
import unittest

from day_24.main import Gate, do_gate, get_bits, parse_input

wires = {"x00": 1, "x01": 1, "x02": 1, "y00": 0, "y01": 1, "y02": 0}
gates = ["x00 AND y00 -> z00", "x01 XOR y01 -> z01", "x02 OR y02 -> z02"]
parsed: list[Gate] = parse_input(gates)

# (X) 101010 + (Y) 101100
bit_math_wires = {
    "x00": 0,
    "x01": 1,
    "x02": 0,
    "x03": 1,
    "x04": 0,
    "x05": 1,
    "y00": 0,
    "y01": 0,
    "y02": 1,
    "y03": 1,
    "y04": 0,
    "y05": 1,
}

bit_math_gates = [
    "x00 AND y00 -> z05",
    "x01 AND y01 -> z02",
    "x02 AND y02 -> z01",
    "x03 AND y03 -> z03",
    "x04 AND y04 -> z04",
    "x05 AND y05 -> z00",
]


class Test(unittest.TestCase):
    def test_parse_formula(self):
        self.assertEqual(parsed[0].l, "x00")
        self.assertEqual(parsed[0].opp, "AND")
        self.assertEqual(parsed[0].r, "y00")
        self.assertEqual(parsed[0].eq, "z00")

    def test_do_gate(self):
        do_gate(wires, parsed[0])
        self.assertEqual(wires["z00"], 0)

    def test_return_bits(self):
        bits = get_bits(wires, parsed, "z")
        self.assertEqual(int(bits, 2), 4)

    def test_fix_bits(self):
        parsed_math = parse_input(bit_math_gates)
        bits = get_bits(bit_math_wires, parsed_math, "z")
        self.assertEqual(bits, format(40, "b"))


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
