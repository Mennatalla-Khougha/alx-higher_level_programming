#!/usr/bin/python3
"""This modula return all the attribute and methods of an object"""


def lookup(obj):
    """Define a function to look up the attributes and methods

    Args:
        obj (object): object to get it's attributes 

    Returns:
        list: list of attributes and methods 
    """
    return list(dir(obj))