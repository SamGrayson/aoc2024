import time
import unittest


class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
