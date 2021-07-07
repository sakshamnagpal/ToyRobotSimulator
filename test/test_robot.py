from robot import ToyRobot
import unittest
from face import Face


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.test_robot = ToyRobot()

    def test_initialise(self):
        self.test_robot = ToyRobot()

        # Test that the robot doesn't have any coordinates
        self.assertIsNone(self.test_robot.x_coordinate)
        self.assertIsNone(self.test_robot.y_coordinate)

        # Test that the robot is not facing any direction
        self.assertIsNone(self.test_robot.face)

    def test_is_placed(self):
        self.test_robot = ToyRobot()

        # Test that the robot is not placed when created
        self.assertFalse(self.test_robot.is_placed())

        # Place the robot
        self.test_robot.place(0, 0, Face.NORTH)
        # Test that the robot is placed
        self.assertTrue(self.test_robot.is_placed())

    def test_place(self):
        # Initialise a robot
        self.test_robot = ToyRobot()

        # Place the robot with valid values
        self.test_robot.place(0, 0, Face.NORTH)

        # Test the coordinates and direction of the robot
        self.assertEqual(self.test_robot.x_coordinate, 0)
        self.assertEqual(self.test_robot.y_coordinate, 0)
        self.assertEqual(self.test_robot.face, Face.NORTH)



if __name__ == '__main__':
    unittest.main()
