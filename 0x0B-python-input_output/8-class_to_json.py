#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns the dict representation of a simple data structure
    """
    return obj.__dict__
