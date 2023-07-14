#!/usr/bin/python3
"""This module create a base class for all other classes in this project"""


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
