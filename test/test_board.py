# This file tests the GameBoard class and its methods

import unittest
from board import GameBoard
from ToyRobotError import ToyRobotError


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.test_board = GameBoard(5)

    def tearDown(self) -> None:
        del self.test_board

    def test_initialise(self):
        # Test the initialisation of the board
        test_size = 3
        self.test_board = GameBoard(test_size)

        # Test the dimensions
        self.assertEqual(len(self.test_board.board), test_size, msg="Test Initialise: Board size incorrect")

        # Test if a negative value for size raises a ValueError
        with self.assertRaises(ToyRobotError):
            self.test_board = GameBoard(-1)

        # Test if a character value for size raises a TypeError
        with self.assertRaises(ToyRobotError):
            self.test_board = GameBoard('1')

    def test_reset_board_size(self):
        # Initialise the board
        self.test_board = GameBoard(5)

        # Change dimensions and check the board
        self.test_board.reset_board(3)

        self.assertEqual(len(self.test_board.board), 3, msg="Test Resize: Board length incorrect")

        # Test negative value should raise a ValueError
        with self.assertRaises(ToyRobotError):
            self.test_board.reset_board(-3)

        # Test non-integers should raise a TypeError
        with self.assertRaises(ToyRobotError):
            self.test_board.reset_board('5')


if __name__ == '__main__':
    unittest.main()
