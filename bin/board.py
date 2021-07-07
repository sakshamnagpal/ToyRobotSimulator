"""
This file contains the code for the Game Board.
The game board is a square board where the Toy Robot can freely roam around according
to the commands passed
"""

from ToyRobotError import ToyRobotError
from IntegerValidation import validate_integer
from face import Face, RobotIcon


class GameBoard:
    """
    The game board class contains the code to create and operate the game board.
    The board can be created to be of different sizes but it needs to be a square.
    """
    def __init__(self, size: int) -> None:
        """
        This method initialises a game board with a give declared size.
        :param size: The size of the square game board
        """
        if not validate_integer(size):
            raise ToyRobotError
        else:
            self.board = [["_" for _ in range(size)] for _ in range(size)]
            self.size = size
            self.current_robot_position = (None, None)

    def __str__(self) -> str:
        """
        This method is called when the board is printed
        It shows a string representation of the board with '_' denoting empty spots
        :return: A string representation of the board
        """
        returning_string = ""
        for i in range(self.size):
            returning_string += "| "
            for j in range(self.size):
                returning_string += self.board[self.size - i - 1][j]
                returning_string += " | "
            returning_string += "\n"
        return returning_string

    def __len__(self) -> int:
        """
        This method returns the size of the board
        :return: Size of the board
        """
        return self.size

    def reset_board(self, size: int = None) -> None:
        """
        This method will reset the board to a specified size. If a size is not mentioned,
        then the original size will be applied
        :param size:
        :return:
        """
        if size is None:
            size = self.size
        self.board = GameBoard(size)
        self.size = size

    def place_robot(self, x: int, y: int, face: Face) -> None:
        """
        This method will place (diagramatically) the robot on
        a particular spot on the game board. This can be viewed by
        calling the str method of the board
        :param x: the x coordinate of the robot
        :param y: the y coordinate of the robot
        :return: None
        """
        if not validate_integer(x) or not validate_integer(y):
            raise ToyRobotError
        elif x >= self.size or y >= self.size:
            raise ToyRobotError
        else:
            self.board[x][y] = RobotIcon[face.name].value
            if self.current_robot_position == (None, None):
                self.current_robot_position = (x, y)
            else:
                self.board[self.current_robot_position[0]][self.current_robot_position[1]] = "_"
