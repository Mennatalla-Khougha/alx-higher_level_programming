#!/usr/bin/python3
"""This module write a JSON into txt"""
import json


def save_to_json_file(my_obj, filename):
    """Define a function that save a json into a txt file

    Args:
        my_obj (obj): object to be saved
        filename (str): name of txt file

    Returns:
        object: python object
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
