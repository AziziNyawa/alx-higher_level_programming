#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Arguments:
        obj: object that is tto be identified
        a_class: class type

    Returns:
        True if type of object is a_class
        False, otherwise
    """
    return type(obj) is a_class
