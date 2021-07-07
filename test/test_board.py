# This file tests the GameBoard class and its methods

import unittest
from board import GameBoard


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
        self.assertEqual(len(self.test_board.board), test_size, msg="Test Initialise: Board length incorrect")
        self.assertEqual(len(self.test_board.board[0]), test_size, msg="Test Initialise: Board width incorrect")

    def test_reset_board_size(self):
        # Initialise the board
        self.test_board = GameBoard(5)

        # Change dimensions and check the board
        self.test_board.reset_board_size(3)

        self.assertEqual(len(self.test_board.board), 3, msg="Test Resize: Board length incorrect")
        self.assertEqual(len(self.test_board.board[0]), 3, msg="Test Resize: Board width incorrect")

        # Test negative value should raise a ValueError
        with self.assertRaises(ValueError):
            self.test_board.reset_board_size(-3)

        # Test non-integers should raise a TypeError
        with self.assertRaises(TypeError):
            self.test_board.reset_board_size('5')


if __name__ == '__main__':
    unittest.main()
