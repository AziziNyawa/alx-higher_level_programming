#!/usr/bin/python3
# 4-square written by Azizi
"""A module to define a square"""


class Square:
    """A class that does square"""

    def __init__(self, size=0):
        """Intialize a class of square
        Arguments:
            sizes: repre the size of the square that is defined
            position: position the square is
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """The property of size as the length of class Square
        Raises:
            TypeError: if size is not interger
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square
        Raises:
            TypeError: if value is not a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
                                                          """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
         """prints the square in the position"""
         print(self.pos_print(), end='')
