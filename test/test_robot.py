from robot import ToyRobot
from ToyRobotError import ToyRobotError
import unittest
from face import Face


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.test_robot = ToyRobot()

    def test_initialise(self):
        self.test_robot = ToyRobot()

        # Test that the robot doesn't have any coordinates
        self.assertIsNone(self.test_robot.get_x_value())
        self.assertIsNone(self.test_robot.get_y_value())

        # Test that the robot is not facing any direction
        self.assertIsNone(self.test_robot.get_face_value())

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
        self.assertEqual(self.test_robot.get_x_value(), 0)
        self.assertEqual(self.test_robot.get_y_value(), 0)
        self.assertEqual(self.test_robot.get_face_value(), Face.NORTH)

        # Test negative values for position raises ValueError
        with self.assertRaises(ToyRobotError):
            self.test_robot.place(-1, 0, Face.NORTH)

        with self.assertRaises(ToyRobotError):
            self.test_robot.place(0, -1, Face.NORTH)

        # Test non-enum values of Face raises TypeError
        with self.assertRaises(ToyRobotError):
            self.test_robot.place(0, 0, "NORTH")

    def test_left(self):
        # Initialise a robot
        self.test_robot = ToyRobot()

        # Place the robot
        self.test_robot.place(0, 0, Face.SOUTH)

        # Test left movements
        self.test_robot.left()
        self.assertEqual(self.test_robot.get_face_value(), Face.EAST)

        self.test_robot.left()
        self.assertEqual(self.test_robot.get_face_value(), Face.NORTH)

        self.test_robot.left()
        self.assertEqual(self.test_robot.get_face_value(), Face.WEST)

        self.test_robot.left()
        self.assertEqual(self.test_robot.get_face_value(), Face.SOUTH)

    def test_right(self):
        # Initialise a robot
        self.test_robot = ToyRobot()

        # Place the robot
        self.test_robot.place(0, 0, Face.SOUTH)

        # Test right movements
        self.test_robot.right()
        self.assertEqual(self.test_robot.get_face_value(), Face.WEST)

        self.test_robot.right()
        self.assertEqual(self.test_robot.get_face_value(), Face.NORTH)

        self.test_robot.right()
        self.assertEqual(self.test_robot.get_face_value(), Face.EAST)

        self.test_robot.right()
        self.assertEqual(self.test_robot.get_face_value(), Face.SOUTH)

    def test_move(self):
        # Initialise a robot
        self.test_robot = ToyRobot()

        # Place the robot
        self.test_robot.place(0, 0, Face.NORTH)

        # Move the robot one step north and check y coordinate
        self.test_robot.move()
        self.assertEqual(self.test_robot.get_y_value(), 1)

        # Turn right, move one step and check x coordinate
        self.test_robot.right()
        self.test_robot.move()
        self.assertEqual(self.test_robot.get_x_value(), 1)

        # Place robot and check movement backwards on grid
        self.test_robot.place(1, 1, Face.NORTH)
        self.test_robot.left()
        self.test_robot.move()
        self.assertEqual(self.test_robot.get_x_value(), 0)

        self.test_robot.place(1, 1, Face.WEST)
        self.test_robot.left()
        self.test_robot.move()
        self.assertEqual(self.test_robot.get_y_value(), 0)

    def test_str(self):
        # Initialise and place the robot
        self.test_robot = ToyRobot()
        self.test_robot.place(0, 0, Face.NORTH)

        # Check if the str returns the correct string
        self.assertEqual(str(self.test_robot), "0,0,NORTH")

        # Rotate right and test the correct string
        self.test_robot.right()
        self.assertEqual(str(self.test_robot), "0,0,EAST")

        # Move and test the correct string
        self.test_robot.move()
        self.assertEqual(str(self.test_robot), "1,0,EAST")


if __name__ == '__main__':
    unittest.main()
