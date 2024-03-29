#!/usr/bin/python3
"""This is a module that writes an Object to atext file"""


import json


def save_to_json_file(my_obj, filename):
    """This method that writes in a file using json
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
