import unittest
from day_03.main import get_dos, get_muls, do_muls


class Test(unittest.TestCase):
    def test_detect_mul_success(self):
        mul_test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
        muls = get_muls(mul_test)
        self.assertEqual(muls, ["mul(2,4)", "mul(5,5)"])

    def test_multiply_muls_success(self):
        muls = ["mul(2,4)", "mul(5,5)"]
        result = do_muls(muls)
        self.assertEqual(result, [8, 25])

    def test_get_dos(self):
        mul_test = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        result = get_dos(mul_test)
        self.assertEqual(result, ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"])


if __name__ == "__main__":
    unittest.main()
