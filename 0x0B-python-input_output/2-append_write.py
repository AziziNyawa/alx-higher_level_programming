#!/usr/bin/python3
"""This module is appends a string in utf8 in file"""


def append_write(filename="", text=""):
    """A method to append str in a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
