from board import GameBoard
from robot import ToyRobot
from typing import Optional
from face import Face
from ToyRobotError import ToyRobotError
from IntegerValidation import validate_integer


class Controller:
    def __init__(self, board_size=5):
        self.board = GameBoard(board_size)
        self.robot = ToyRobot()
        self.valid_commands = ["MOVE", "LEFT", "RIGHT", "REPORT"]

    def execute_command(self, command) -> Optional[str]:
        command_list = command.split(" ")
        valid_faces = [face.name for face in Face]
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
                self.robot.place(int(x_coord), int(y_coord), Face[face_value])
                return None
        elif command_list[0] in self.valid_commands:
            if command_list[0] == 'LEFT':
                self.robot.left()
                return None
            elif command_list[0] == 'RIGHT':
                self.robot.right()
                return None
            elif command_list[0] == 'MOVE':
                current_coords = (self.robot.get_x_value(), self.robot.get_y_value())
                current_face = self.robot.get_face_value()
                self.robot.move()
                if 0 <= self.robot.get_x_value() < len(self.board) and 0 <= self.robot.get_y_value() < len(self.board):
                    return None
                else:
                    self.robot.place(current_coords[0], current_coords[1], current_face)
                    raise ToyRobotError
            elif command_list[0] == "REPORT":
                return str(self.robot)


if __name__ == '__main__':
    controller = Controller()
    controller.execute_command("PLACE 1,2,EAST")
    controller.execute_command("MOVE")
    controller.execute_command("MOVE")
    controller.execute_command("LEFT")
    controller.execute_command("MOVE")
    print(controller.execute_command("REPORT"))
