#!/usr/bin/python3
"""This module create a base class for all other classes in this project"""
import json


class Base:
    """Define the class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize the class Base

        Args:
            id (int, optional): unique id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """String representation of list_dictionaries

        Args:
            list_dictionaries (dict): dict to be dumped into json

        Returns:
            str: json representation of dict
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)