#!/usr/bin/python3
# 2-square.py done by Azizi
"""A module that defines square class"""


class Square:
    """A square class that is used in 2-square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: repr the size of the square to be defined
        Raises:
            TypeError: if the size to use is not interger
            ValueError: if size is less than zero value
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
