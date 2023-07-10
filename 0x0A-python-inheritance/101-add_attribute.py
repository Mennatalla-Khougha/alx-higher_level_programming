#!/usr/bin/python3
"""This Modula add new attribute"""


def add_attribute(obj, attr, value):
    """This function sets attribute to the obj

    Args:
        obj (class): class to add the attribute to
        attr (str): name of the attribute
        value (any): value of attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
