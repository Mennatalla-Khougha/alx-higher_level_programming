#!/usr/bin/python3
"""This module return the dictionary description"""


def class_to_json(obj):
    """Define a function that return the dictionary description

    Args:
        obj (class): class to return it's dictionary

    Returns:
        obj dictionary: the obj dictionary
    """
    return obj.__dict__
