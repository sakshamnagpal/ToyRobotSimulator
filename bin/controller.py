from board import GameBoard
from robot import ToyRobot


class Game:
    def __init__(self, board_size = 5):
        self.board = GameBoard(board_size)
        self.robot = ToyRobot()

    def interpret_command(self, command):
        pass

    def __execute_command(self, command):
        pass

    def report(self):
        pass

    def controller(self):
        pass
