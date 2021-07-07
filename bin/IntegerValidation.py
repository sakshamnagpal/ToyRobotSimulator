"""
This file contains a method that will be used to validate values
to make sure they are positive integers
"""


def validate_integer(value) -> bool:
    """
    This method validates an integer value to be a positive integer
    :param value: The value to be validated
    :return: True if its a positive integer, false otherwise
    """
    if isinstance(value, int) and value >= 0:
        return True
    return False
