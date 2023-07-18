#!usr/bin/python3
"""This functions to write a str to text file"""


def write_file(filename="", text=""):
    """Writes a string in a format utf8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
