#!/usr/bin/python3
""" Module that execute a function that appends a line in a file """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a str is found

    Arguments:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
