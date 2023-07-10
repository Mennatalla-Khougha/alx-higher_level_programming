#!/usr/bin/python3
"""This modula checks for instance of a class"""


def is_kind_of_class(obj, a_class):
    """Define a function to checks instances of class

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked against

    Returns:
        Bool: True or False
    """
    return isinstance(obj, a_class)
