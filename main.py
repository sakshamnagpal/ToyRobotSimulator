"""
This file contains the main interaction between the user and the game.
Any future work will expand on the current given menu and possibly
change the UI of the menu
"""
from bin.Localised_Strings import menu_strings
from bin.controller import Controller
from bin.ToyRobotError import ToyRobotError
from bin.IntegerValidation import validate_integer


def manual_input() -> None:
    """
    This method handles the manual input of commands from the user
    and performs actions on the game robot
    :return: None
    """
    while True:
        user_command = input("Enter command: ")
        if user_command == 'QUIT':
            return None
        try:
            output = controller.execute_command(user_command)
            if output:
                print(output)
        except ToyRobotError:
            pass


def read_file() -> None:
    """
    This method handles the input being read from a file. This method
    will return none and exit back to the main menu if the filename
    provided is incorrect/doesn't exist
    :return: None
    """
    filename = input("Enter filename: ")
    try:
        with open(filename) as fn:
            file_contents = fn.readlines()
    except FileNotFoundError:
        print("Invalid filename")
        return None
    else:
        for command in file_contents:
            try:
                output = controller.execute_command(command.strip('\n'))
                if output:
                    print(output)
            except ToyRobotError:
                pass


if __name__ == '__main__':
    game_board_size = 5
    controller = Controller(game_board_size)
    print(menu_strings['title_string'])
    main_menu_quit = False
    while not main_menu_quit:
        print(menu_strings['main_menu_string'])
        try:
            user_input = int(input('>_ '))
            if user_input not in [1, 2, 3, 4, 5, 6]:
                raise ValueError
        except ValueError:
            print("Invalid command")
        else:
            if user_input == 1:
                read_file()
            elif user_input == 2:
                manual_input()
            elif user_input == 3:
                try:
                    board_size = int(input("Enter new game board size: "))
                    if validate_integer(board_size):
                        controller = Controller(board_size)
                except ValueError:
                    print("Invalid size. Returning to main menu")
            elif user_input == 4:
                print(menu_strings['help_string'])
            elif user_input == 5:
                print(menu_strings['rules_string'])
            elif user_input == 6:
                main_menu_quit = True
