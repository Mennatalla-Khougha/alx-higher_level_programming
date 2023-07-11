#!/usr/bin/python3
"""This module append to a txt file"""


def append_write(filename="", text=""):
    """This function append to a txt file

    Args:
        filename (str, optional): File to be written into. Defaults to "".
        text (str, optional): text to be written. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
