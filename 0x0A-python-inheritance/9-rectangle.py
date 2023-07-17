#!/usr/bin/python3
"""Defines a class rectangle that inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that represents a rectangle BaseGeometry"""

    def __init__(self, width, height):
        """ Initializes instance rectangle"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the value of the area"""
        return self.__width * self.__height

    def __str__(self):
        """ Special method that returns the printable str of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
