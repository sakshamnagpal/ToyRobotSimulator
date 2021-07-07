from board import GameBoard
from robot import ToyRobot
from face import Face
from ToyRobotError import ToyRobotError
from controller import Controller
import unittest


class TestController(unittest.TestCase):
    def test_initialise(self):
        # Initialise a controller with default values
        self.controller = Controller()

        # Test if board and robot get initialised properly
        self.assertIsInstance(self.controller.board, GameBoard)
        self.assertIsInstance(self.controller.robot, ToyRobot)

        # Test if the board has the correct (default) size
        self.assertEqual(self.controller.board.get_size(), 5)

    def test_interpret_command(self):
        # Initialise a controller with default values
        self.controller = Controller()

        # Test if a place command is interpreted correctly
        self.controller.execute_command("PLACE 0,0,NORTH")
        self.assertTrue(self.controller.robot.is_placed())
        self.assertEqual(self.controller.robot.get_x_value(), 0)
        self.assertEqual(self.controller.robot.get_y_value(), 0)

        # Test if a move command is interpreted correctly
        self.controller.execute_command("PLACE 0,0,NORTH")
        self.controller.execute_command("MOVE")
        self.assertEqual(self.controller.robot.get_y_value(), 1)

        # Test if a rotation command is interpreted correctly
        self.controller.execute_command("PLACE 0,0,NORTH")
        self.controller.execute_command("LEFT")
        self.assertEqual(self.controller.robot.get_face_value(), Face.WEST)
        self.controller.execute_command("RIGHT")
        self.assertEqual(self.controller.robot.get_face_value(), Face.NORTH)

        # Test if a report command is interpreted correctly
        self.controller.execute_command("PLACE 1,2,NORTH")
        self.assertEqual(self.controller.execute_command("REPORT"), "1,2,NORTH")

    def test_out_of_board_robot(self):
        # Initialise a controller with the robot at the edge
        self.controller = Controller()
        self.controller.execute_command("PLACE 4,4,NORTH")

        # Test if moving the robot out of bounds raises an error
        with self.assertRaises(ToyRobotError):
            self.controller.execute_command("MOVE")


if __name__ == '__main__':
    unittest.main()
