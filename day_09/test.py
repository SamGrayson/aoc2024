import time
import unittest

from day_09.main import calc_checksum, format_str, move_files, move_files_block

TEST_STR = "2333133121414131402"
RESULT = "00...111...2...333.44.5555.6666.777.888899"
BLOCK_MOVE_RESULT = "00992111777.44.333....5555.6666.....8888.."
TEST_MOVE = "0099811188827773336446555566"
TEST_SIMPLE = "12345"
SIMPLE_RESULT = "0..111....22222"
TEST_SIMPLE_MOVE = "022111222"


class Test(unittest.TestCase):
    def test_format_str_simple(self):
        result = format_str(TEST_SIMPLE)
        self.assertEqual("".join(result), SIMPLE_RESULT)

    def test_format_str(self):
        result = format_str(TEST_STR)
        self.assertEqual("".join(result), RESULT)

    def test_move_simple(self):
        result = move_files(list(SIMPLE_RESULT))
        self.assertEqual(result, list(TEST_SIMPLE_MOVE))

    def test_move(self):
        result = move_files(list(RESULT))
        self.assertEqual(result, list(TEST_MOVE))

    def test_move_block(self):
        result = move_files_block(list(RESULT))
        self.assertEqual("".join(result), BLOCK_MOVE_RESULT)

    def test_success(self):
        self.assertEqual(True, True)

    def test_checksum(self):
        checksum = calc_checksum(list(TEST_MOVE))
        self.assertEqual(checksum, 1928)

    def test_checksum_block(self):
        checksum = calc_checksum(list(BLOCK_MOVE_RESULT))
        self.assertEqual(checksum, 2858)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
