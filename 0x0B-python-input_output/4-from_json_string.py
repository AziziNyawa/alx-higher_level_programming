#!/usr/bin/python3
"""This module that returns an object using json str"""


import json


def from_json_string(my_str):
    """this method that returns an object in json
    """
    return json.load(my_str)
