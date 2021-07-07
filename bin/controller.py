from board import GameBoard
from robot import ToyRobot
from typing import Optional
from ToyRobotError import ToyRobotError


class Controller:
    def __init__(self, board_size=5):
        self.board = GameBoard(board_size)
        self.robot = ToyRobot()

    def __interpret_command(self, command):
        pass

    def execute_command(self, command) -> Optional[str]:
        pass
