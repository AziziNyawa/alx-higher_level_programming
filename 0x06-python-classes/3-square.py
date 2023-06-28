#!/usr/bin/python3
# 3-square.p done by Azizi
"""Defines the class square"""


class Square:
    """A class of Square to done cal"""

    def __init__(self, size=0):
        """Intializing the square class
        Arguments:
            size: repres the size of the class square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero value
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Does the calculation of square
        Returns: The square answer
        """

        return (self.__size ** 2)
