#!/usr/bin/python3
"""Defines a Rectangle subclass of square class""" 
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprtesents a square class"""

    def __init__(self,size):
        """intializing a new square"
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
