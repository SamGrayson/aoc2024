import unittest

from day_01.main import getDiff, getSimilarityScore


class Test(unittest.TestCase):
    def test_distance_success(self):
        g1 = [1, 2, 3]
        g2 = [3, 2, 1]
        # Should equal 0 since no diff
        result = getDiff(g1, g2)
        self.assertEqual(result, 0)

    def test_get_sim_score(self):
        g1 = [1, 2, 3]
        g2 = [1, 1, 1]
        # Should equal 3, 1 appears 3 times
        result = getSimilarityScore(g1, g2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
