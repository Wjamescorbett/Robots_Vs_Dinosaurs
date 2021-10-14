from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot("Robot 1", 100)
        robot_2 = Robot("Robot 2", 200)
        robot_3 = Robot("Robot 3", 300)
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)


