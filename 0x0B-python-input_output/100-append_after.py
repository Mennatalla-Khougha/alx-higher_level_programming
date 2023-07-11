#!/usr/bin/python3
"""This module insert a text after each line containing specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        search_string (str, optional): String to search for. Defaults to "".
        new_string (str, optional): Line of text to insert. Defaults to "".
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
