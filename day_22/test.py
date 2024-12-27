import time
import unittest

from day_22.main import calc_secret_num, iter_calc_secret_num


class Test(unittest.TestCase):
    def test_get_secret_num(self):
        sn = calc_secret_num(123)
        self.assertEqual(sn, 15887950)

    def test_get_secret_num_2k_sn(self):
        sn, _ = iter_calc_secret_num(123, 2000)
        self.assertTrue(True)

    def test_get_secret_num_2k(self):
        sn, _ = iter_calc_secret_num(1, 2000)
        self.assertEqual(sn, 8685429)

    def test_get_secret_2k_total(self):
        total = 0
        for l in [1, 10, 100, 2024]:
            sn = iter_calc_secret_num(int(l), 2000)
            total += sn
        self.assertEqual(total, 37327623)

    def test_find_best_seq_2k(self):
        sequences: list[dict] = []
        for l in [1, 2, 3, 2024]:
            sn, seq = iter_calc_secret_num(int(l), 2000)
            sequences.append(seq)
        first = sequences[0]
        # Look at all the first sequences
        most_bananas = 0
        most_bananas_seq = None
        for seq, val in first.items():
            total_bananas = val
            # Calculate that sequence in all the others.
            for res in sequences[1:]:
                if seq in res:
                    total_bananas += res[seq]
            if total_bananas > most_bananas:
                most_bananas_seq = seq
                most_bananas = total_bananas

        self.assertEqual(most_bananas_seq, (-2, 1, -1, 3))
        self.assertEqual(most_bananas, 23)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
