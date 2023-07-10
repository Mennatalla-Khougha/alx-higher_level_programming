#!/usr/bin/python3
"""This Modula checks the object is subclass"""


def inherits_from(obj, a_class):
    """Define a function to checks for subclass

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked against

    Returns:
        Bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
