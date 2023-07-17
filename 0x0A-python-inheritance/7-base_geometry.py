#!/usr/bin/python3
"""Defines a base Geometry class of base geometry."""


class BaseGeometry:
    """this is a class that defines a base geometry"""

    def area(self):
        """method for the class implementes yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate as an interger
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} `must be greater than 0".format(name))
