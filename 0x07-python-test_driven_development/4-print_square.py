#!/usr/bin/python3
"""

This module is made up of function that prints a square with the character #

"""


def print_square(size):
    """ Function that prints a square with the char #

    Arguments:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an int number


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
