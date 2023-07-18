#!/usr/bin/python3
"""This module that returns a Json Representation"""
import json


def to_json_string(my_obj):
    """This a function that give a str object
    """
    return json.dumps(my_obj)
