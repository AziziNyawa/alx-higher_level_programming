#!/usr/bin/python3
""" Module that returns the dict description with a simple
data structure for a JSON serialization of an object used
"""


def class_to_json(obj):
    """ Function that retuns the dictionary desc of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
