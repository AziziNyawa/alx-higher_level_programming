#!/usr/bin/python3
def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object

    Arguments:
        object: instance of the class made

    Returns:
        List of attributes
    """

    return dir(obj)
