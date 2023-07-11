#!/usr/bin/python3
"""This module write a JSON into txt"""
import json


def load_from_json_file(filename):
    """Define a function that save a json into a txt file

    Args:
        my_obj (obj): object to be saved
        filename (str): name of txt file

    Returns:
        object: python object
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
