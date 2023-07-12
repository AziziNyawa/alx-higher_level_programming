#!/usr/bin/python3
""" Module that creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that creates an object from JSON file

    Arguments:
        filename: textfile name

    Raises:
        Exception: when the object can not be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
