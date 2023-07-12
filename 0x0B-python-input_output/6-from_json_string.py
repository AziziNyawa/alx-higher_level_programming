#!/usr/bin/python3
""" Module that contains a function that returns an object by
a JSON rep
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Arguments:
        my_str: JSON representation

    Raises:
        Exception: when the str can not be decoded

    """
    return json.loads(my_str)
