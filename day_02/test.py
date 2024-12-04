import unittest

from day_02.main import allow_failure_is_safe, is_safe


class Test(unittest.TestCase):
    def test_is_safe(self):
        desc = [7, 6, 4, 2, 1]
        asc = [1, 3, 5, 8]
        desc_result = is_safe(desc)
        asc_result = is_safe(asc)
        self.assertTrue(desc_result)
        self.assertTrue(asc_result)

    def test_is_not_safe(self):
        nope = [1, 8]
        nope_2 = [1, 2, 5, 4, 2]
        nope_3 = [1, 1, 1]
        desc_result = is_safe(nope)
        asc_result = is_safe(nope_2)
        no_result = is_safe(nope_3)
        self.assertFalse(desc_result)
        self.assertFalse(asc_result)
        self.assertFalse(no_result)

    def test_is_safe_one_fail(self):
        desc = [7, 6, 4, 9, 2, 1]
        asc = [1, 3, 1, 5, 8]
        eql = [1, 5, 3, 4]
        first = [10, 1, 2, 3]
        desc_result = allow_failure_is_safe(desc)
        asc_result = allow_failure_is_safe(asc)
        eql_result = allow_failure_is_safe(eql)
        first_result = allow_failure_is_safe(first)
        self.assertTrue(desc_result)
        self.assertTrue(asc_result)
        self.assertTrue(eql_result)
        self.assertTrue(first_result)

    def test_is_not_safe_one_fail(self):
        desc = [7, 6, 4, 9, 5, 2, 1]
        asc = [1, 3, 1, 2, 5, 8]
        eql = [1, 2, 3, 11, 50]
        desc_result = allow_failure_is_safe(desc)
        asc_result = allow_failure_is_safe(asc)
        eql_result = allow_failure_is_safe(eql)
        self.assertFalse(desc_result)
        self.assertFalse(asc_result)
        self.assertFalse(eql_result)


if __name__ == "__main__":
    unittest.main()
