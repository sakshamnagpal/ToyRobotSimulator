"""
This file contains the code for the Toy Robot, including initialisation and movement.
This toy robot will be able to freely roam around on the game board
"""
from face import Face
from IntegerValidation import validate_integer
from ToyRobotError import ToyRobotError


class ToyRobot:
    """
    This class contains the code for the ToyRobot and its move set. The robot will
    roam freely and will not raise any errors if any movement would cause it to
    fall off the board
    """
    def __init__(self) -> None:
        """
        This is the constructor for the ToyRobot class which creates a ToyRobot
        """
        self.x_coordinate = None
        self.y_coordinate = None
        self.face = None
        self.placed = False

    def __str__(self) -> str:
        """
        This function will return a string representation of the robot's position and face
        :return: a string containing the coordinates and the face of the robot
        """
        if not self.placed:
            return ""
        else:
            return str(self.x_coordinate) + "," + str(self.y_coordinate) + "," + str(self.face.name)

    def get_x_value(self) -> int:
        """
        This function will return the current x coordinate of the robot
        :return: The x coordinate of the robot
        """
        return self.x_coordinate

    def get_y_value(self) -> int:
        """
        This function will return the current y coordinate of the robot
        :return: The y coordinate of the robot
        """
        return self.y_coordinate

    def get_face_value(self) -> Face:
        """
        This function will return the current face value of the robot
        :return: The face value of the robot
        """
        return self.face

    def is_placed(self) -> bool:
        """
        This function will return the placed status of the robot
        :return: True if the robot is placed, false otherwise
        """
        return self.placed

    def place(self, x, y, face) -> None:
        """
        This method changes the coordinates of the toy robot and places it
        :param x: The x coordinate of where the robot is placed
        :param y: The y coordinate of where the robot is placed
        :param face: The face of the robot while it is placed
        :return: None
        """
        if not validate_integer(x) or not validate_integer(y) or not isinstance(face, Face):
            raise ToyRobotError
        else:
            self.x_coordinate = x
            self.y_coordinate = y
            self.face = face
            self.placed = True

    def move(self) -> None:
        """
        This method will move the robot one step in one particular direction
        according to the face of the robot
        :return: none
        """
        if self.face == Face.NORTH:
            self.y_coordinate += 1
        elif self.face == Face.SOUTH:
            self.y_coordinate -= 1
        elif self.face == Face.WEST:
            self.x_coordinate -= 1
        elif self.face == Face.EAST:
            self.x_coordinate += 1

    def left(self) -> None:
        """
        This method will turn the robot 90 degrees to the left
        :return: None
        """
        current_value = self.face.value
        new_value = ((current_value - 1 % 4) + 4) % 4
        self.face = Face(new_value)

    def right(self):
        """
        This method will turn the robot 90 degrees to the right
        :return: None
        """
        current_value = self.face.value
        new_value = ((current_value + 1 % 4) + 4) % 4
        self.face = Face(new_value)
