import time
import unittest

from day_23.main import (
    all_connect,
    create_connection_map,
    get_connections,
    get_connections_all_connect,
)

test_input = [
    "kh-tc",
    "qp-kh",
    "de-cg",
    "ka-co",
    "yn-aq",
    "qp-ub",
    "cg-tb",
    "vc-aq",
    "tb-ka",
    "wh-tc",
    "yn-cg",
    "kh-ub",
    "ta-co",
    "de-co",
    "tc-td",
    "tb-wq",
    "wh-td",
    "ta-ka",
    "td-qp",
    "aq-cg",
    "wq-ub",
    "ub-vc",
    "de-ta",
    "wq-aq",
    "wq-vc",
    "wh-yn",
    "ka-de",
    "kh-ta",
    "co-tc",
    "wh-qp",
    "tb-vc",
    "td-yn",
]


three_comps = list(
    map(
        lambda c: tuple(c.split(",")),
        [
            "aq,cg,yn",
            "aq,vc,wq",
            "co,de,ka",
            "co,de,ta",
            "co,ka,ta",
            "de,ka,ta",
            "kh,qp,ub",
            "qp,td,wh",
            "tb,vc,wq",
            "tc,td,wh",
            "td,wh,yn",
            "ub,vc,wq",
        ],
    )
)


class Test(unittest.TestCase):
    def test_find_sets_of_three(self):
        connection_map = create_connection_map(test_input)
        connections = get_connections(connection_map, 3)
        three_len = list(filter(lambda c: len(c) == 3, connections))
        self.assertTrue(all([c in three_comps for c in three_len]))
        tstart_count = 0
        for conn in three_len:
            for c in conn:
                if c.startswith("t"):
                    tstart_count += 1
                    break  # just need to count the lines once
        self.assertEqual(tstart_count, 7)

    def test_find_largest_connection(self):
        connection_map = create_connection_map(test_input)
        connections = get_connections_all_connect(connection_map)
        max_connection = max(connections, key=lambda item: (len(item), item))
        self.assertEqual(max_connection, ("co", "de", "ka", "ta"))

    def test_all_connect(self):
        connect = ["co", "de", "ka"]
        connection_map = create_connection_map(test_input)
        all_c = all_connect(connection_map, connect, "ta")
        self.assertTrue(all_c)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
