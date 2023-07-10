#!/usr/bin/python3
"""This modula check the class of an object"""


def is_same_class(obj, a_class):
    """Define a way to check the class of an abject

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked against

    Returns:
        bool: True or False
    """
    if type(obj) == a_class:
        return True
    return False
