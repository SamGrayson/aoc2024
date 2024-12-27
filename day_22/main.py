import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")


def iter_calc_secret_num(sn: int, itr: int) -> tuple[int, dict]:
    i = 0
    values = [int(str(sn)[-1])]
    key_val = {}
    for i in range(itr):
        i += 1
        n_sn = calc_secret_num(sn)
        ones_val = int(str(n_sn)[-1])
        prev_ones_val = int(str(sn)[-1])
        prev_key = None
        ones_diff = ones_val - prev_ones_val
        if i >= 3:
            prev_key = tuple(values[i - 3 : i] + [ones_diff])
        values.append(ones_diff)
        if prev_key and not key_val.get(prev_key, None):
            key_val[prev_key] = ones_val
        sn = n_sn
    return sn, key_val


def calc_secret_num(_sn: int):
    multn = _sn * 64
    sn = (_sn ^ multn) % 16777216

    divn = sn // 32
    sn = (sn ^ divn) % 16777216

    multBn = sn * 2048
    sn = (sn ^ multBn) % 16777216

    return sn


def part_1():
    with open(INPUT_PATH) as file:
        lines = file.readlines()
    total = 0
    for l in lines:
        sn, _ = iter_calc_secret_num(int(l), 2000)
        total += sn
    print("Part 1: " + str(total))


def part_2():
    with open(INPUT_PATH) as file:
        lines = file.readlines()
    sequences: list[dict] = []
    for l in lines:
        _, seq = iter_calc_secret_num(int(l), 2000)
        sequences.append(seq)
    first = sequences[0]
    # Look at all the first sequences
    most_bananas = 0
    for seq, val in first.items():
        total_bananas = val
        # Calculate that sequence in all the others.
        for res in sequences[1:]:
            if seq in res:
                total_bananas += res[seq]
        if total_bananas > most_bananas:
            most_bananas = total_bananas
    print("Part 2: " + str(most_bananas))


if __name__ == "__main__":
    start_time = time.time()
    part_1()
    part_2()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
