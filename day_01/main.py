def getDiff(g1: list[int], g2: list[int]) -> int:
    g1.sort()
    g2.sort()

    diff = 0
    for idx, i in enumerate(g1):
        diff += abs(g2[idx] - i)
    return diff


def getSimilarityScore(g1: list[int], g2: list[int]) -> int:
    num_count = {}
    for i in g2:
        if i not in num_count:
            num_count[i] = 1
        else:
            num_count[i] += 1

    total_sim_score = 0
    for i in g1:
        total_sim_score += i * num_count.get(i, 0)
    return total_sim_score


def part_1():
    with open("day_01/input.txt", "r") as file:
        g1 = []
        g2 = []
        for line in file:
            groups = line.strip().split("   ")
            g1.append(groups[0])
            g2.append(groups[1])
    g1 = list(map(int, g1))
    g2 = list(map(int, g2))
    print("Part 1: " + str(getDiff(g1, g2)))


def part_2():
    with open("day_01/input.txt", "r") as file:
        g1 = []
        g2 = []
        for line in file:
            groups = line.strip().split("   ")
            g1.append(groups[0])
            g2.append(groups[1])
    g1 = list(map(int, g1))
    g2 = list(map(int, g2))
    print("Part 2: " + str(getSimilarityScore(g1, g2)))


if __name__ == "__main__":
    part_1()
    part_2()
