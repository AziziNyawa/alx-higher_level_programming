#!/usr/bin/python3
"""this module defines a function that adds attributes to objects"""


def add_attribute(obj, name, value):
    """Add a new attribute t an object if its possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
