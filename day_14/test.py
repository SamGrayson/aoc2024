import time
import unittest

from day_14.main import Robot, count_quadrants, get_instructions, get_middle_coord, move


robo_test = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


# Positive x means the robot is moving to the right, and positive y means the robot is moving down.
class Test(unittest.TestCase):
    def test_parse(self):
        robot: Robot = get_instructions("p=0,4 v=3,-3")
        self.assertEqual(robot.pos, (4, 0))
        self.assertEqual(robot.c_move, (0, 3))
        self.assertEqual(robot.r_move, (-3, 0))

    def test_move_5(self):
        robot = get_instructions("p=2,4 v=2,-3")
        # 0 indexed
        max_r, max_c = 7 - 1, 11 - 1
        move(max_r, max_c, robot, 5)
        self.assertEqual(robot.pos, (3, 1))

    def test_move_100(self):
        robot = get_instructions("p=2,0 v=2,-1")
        # 0 indexed
        max_r, max_c = 7 - 1, 11 - 1
        move(max_r, max_c, robot, 100)
        self.assertEqual(robot.pos, (5, 4))

    def test_count_quadrants(self):
        max_r, max_c = 7 - 1, 11 - 1
        middle = get_middle_coord(max_r, max_c)
        robots = []
        for l in robo_test.strip().split("\n"):
            robot = get_instructions(l)
            move(max_r, max_c, robot, 100)
            robots.append(robot)

        valid_robots = count_quadrants(middle, robots)

        self.assertEqual(middle, (3, 5))
        self.assertEqual(valid_robots, 12)

    def test_success(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    print("Finished in: " + str(round(time.time() - start_time)) + "s")
