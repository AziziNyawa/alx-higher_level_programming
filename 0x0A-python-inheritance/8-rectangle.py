#!/usr/bin/python3
"""Inherit from class baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle using basegeometry"""

    def __init__(self, width, height):
        """Intializing a new rectangle class
        """
        self.interger_validator("width", width)
        self.__width = width
        self.interger_validator("height", height)
        self.__height = height
