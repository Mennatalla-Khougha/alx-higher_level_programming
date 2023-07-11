#!/usr/bin/python3
"""This module return a python object from JSON"""
import json


def from_json_string(my_str):
    """Define a function that convert my_str from json

    Args:
        my_str (obj): object to be converted into python object

    Returns:
        object: python object
    """
    return json.loads(my_str)
