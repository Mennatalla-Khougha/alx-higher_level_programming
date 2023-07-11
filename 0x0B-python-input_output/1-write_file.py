#!/usr/bin/python3
"""This module write to a txt file"""


def write_file(filename="", text=""):
    """This function write to a txt file

    Args:
        filename (str, optional): File to be written into. Defaults to "".
        text (str, optional): text to be written. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
