menu_strings = {'title_string': """
------------------------------------------------------------
                REA TOY ROBOT CHALLENGE
------------------------------------------------------------

Please choose how you want to play the game:
""",

                'help_string': """
The game can be played in manual mode or auto mode by reading a file.
When providing a filename, please make sure you either put the file in the same folder
as the game or provide the path to the file in the filename.
The commands that can be used in manual mode are as follows: 

COMMANDS
PLACE X,Y,FACE : This command will place the robot at coords (X,Y) facing direction FACE
(FACE can be either NORTH, EAST, SOUTH, WEST)

MOVE : This command will move the robot one position in the direction that it is facing

LEFT : This command will turn the robot 90 degrees to the left

RIGHT : This command will turn the robot 90 degrees to the right

REPORT : This command will print the current location of the robot

QUIT : This command will quit the manual input mode and return to main menu
""",
                'main_menu_string': """
1. File mode (read instructions from a file)
2. Manual input mode
3. Get help
4. Modify game board size
5. Quit
"""
                }
