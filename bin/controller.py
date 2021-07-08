"""
This file contains the game logic and the controller that plays the game.
This file's class and methods will be called from the main file
"""
from bin.board import GameBoard
from bin.robot import ToyRobot
from typing import Optional
from bin.face import Face
from bin.ToyRobotError import ToyRobotError
from bin.IntegerValidation import validate_integer


class Controller:
    """
    This class acts as the interface for board and robot, combining them together.
    The class contains logic for playing the game, including interpreting user's commands.
    """
    def __init__(self, board_size: int = 5) -> None:
        """
        This method creates a game board and the robot. The default
        size for the game board is 5, however, this can be changed by the user
        :param board_size: The size of the game board, default value is 5
        """
        self.board = GameBoard(board_size)
        self.robot = ToyRobot()
        self.valid_commands = ["MOVE", "LEFT", "RIGHT", "REPORT"]

    def execute_command(self, command: str) -> Optional[str]:
        """
        This method interprets and runs a command entered by the user. The
        details of the commands can be found in the README.md file
        :param command: The command entered by the user
        :return: String of the robot if the command is report, none otherwise
        """
        command_list = command.split(" ")
        valid_faces = [face.name for face in Face]
        # The place command differs from the others and hence needs to be dealt differently
        if len(command_list) > 1 and command_list[0] == "PLACE":
            try:
                x_coord, y_coord, face_value = command_list[1].split(",")
                if not validate_integer(int(x_coord)) or not \
                        validate_integer(int(y_coord)) or face_value not in valid_faces:
                    raise ToyRobotError
            except KeyError:
                raise ToyRobotError
            except ValueError:
                raise ToyRobotError
            else:
                if 0 <= int(x_coord) < len(self.board) and 0 <= int(y_coord) < len(self.board):
                    self.robot.place(int(x_coord), int(y_coord), Face[face_value])
                    return None
                else:
                    raise ToyRobotError
        # All the other commands are single word and hence can be dealt with rather similarly
        elif command_list[0] in self.valid_commands:
            if command_list[0] == 'LEFT':
                if not self.robot.is_placed():
                    raise ToyRobotError
                self.robot.left()
                return None
            elif command_list[0] == 'RIGHT':
                if not self.robot.is_placed():
                    raise ToyRobotError
                self.robot.right()
                return None
            elif command_list[0] == 'MOVE':
                if not self.robot.is_placed():
                    raise ToyRobotError
                current_coords = (self.robot.get_x_value(), self.robot.get_y_value())
                current_face = self.robot.get_face_value()
                self.robot.move()
                # Check if the movement will make the robot go off the board, raise an error if that's the case
                if 0 <= self.robot.get_x_value() < len(self.board) and 0 <= self.robot.get_y_value() < len(self.board):
                    return None
                else:
                    self.robot.place(current_coords[0], current_coords[1], current_face)
                    raise ToyRobotError
            elif command_list[0] == "REPORT":
                return str(self.robot)
