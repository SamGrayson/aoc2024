import unittest
from day_05.main import create_instruction, fix_line, get_middle, is_correct

TEST_INSTRUCTIONS = set(
    [
        (47, 53),
        (97, 75),
        (47, 13),
        (97, 29),
        (53, 29),
        (97, 47),
        (97, 53),
        (75, 29),
        (53, 13),
        (97, 13),
        (29, 13),
        (75, 47),
        (47, 61),
        (75, 53),
        (75, 13),
        (61, 29),
        (97, 61),
        (61, 53),
        (75, 61),
        (61, 13),
        (47, 29),
    ]
)


class Test(unittest.TestCase):
    def test_check_order(self):
        instruction = create_instruction("47|53")
        self.assertEqual(instruction, (47, 53))

    def test_is_correct_success(self):
        correct = is_correct(TEST_INSTRUCTIONS, "75,47,61,53,29")
        self.assertTrue(correct)

    def test_is_correct_fail(self):
        correct = is_correct(TEST_INSTRUCTIONS, "97,13,75,29,47")
        self.assertFalse(correct)

    def test_get_middle(self):
        test = get_middle("1,2,3,4,5")
        self.assertTrue(test, 3)

    def test_fix_line(self):
        test_1 = fix_line(TEST_INSTRUCTIONS, "75,97,47,61,53")
        test_2 = fix_line(TEST_INSTRUCTIONS, "61,13,29")
        test_3 = fix_line(TEST_INSTRUCTIONS, "97,13,75,29,47")
        self.assertEqual(test_1, "97,75,47,61,53")
        self.assertEqual(test_2, "61,29,13")
        self.assertEqual(test_3, "97,75,47,29,13")


if __name__ == "__main__":
    unittest.main()
