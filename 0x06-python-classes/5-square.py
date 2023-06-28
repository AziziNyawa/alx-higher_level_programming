#!/usr/bin/python3
# 4-square written by Azizi
"""A module to define a square"""


class Square:
    """A class that does square"""

    def __init__(self, size=0):
        """Intialize a class of square
        Arguments:
            sizes: repre the size of the square that is defined
        Raises:
            TypeError: if the size used is not an interger
            ValueError: if the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Does retrieving of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    def area(self):
        """
        Doing the calculation on the square
        Returns: The square answer
        """

        return (self.__size **2)

    def my_print(self):
        """print the square in # form"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
