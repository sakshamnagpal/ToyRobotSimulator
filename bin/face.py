"""
This file contains the enums for faces and Robot icons to be displayed on the game grid.
Unicode characters are used to denote the robot icons using triangles
"""

from enum import Enum


class Face(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class RobotIcon(Enum):
    NORTH = '\u1403'        # normal triangle
    EAST = '\u1405'         # right facing triangle
    SOUTH = '\u1401'        # upside down triangle
    WEST = '\u140A'         # left facing triangle
