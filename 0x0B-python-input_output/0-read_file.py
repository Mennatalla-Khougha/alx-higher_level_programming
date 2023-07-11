#!/usr/bin/python3
"""This module read a text file"""


def read_file(filename=""):
    """Define a function to read from a text file

    Args:
        filename (str, optional): file to be read. Defaults to "".
    """
    with open(filename) as file:
        print(file.read(), end="")
