#!/usr/bin/python3
""" Module that contains a function that writes to a text a file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text a file

    Arguments:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
