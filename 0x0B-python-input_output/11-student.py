#!/usr/bin/python3
"""This module write a class"""


class Student:
    """Define a Student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialize Student class

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        """retrieve a dictionary representation

        Returns:
            dict: dictionary
        """
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes of the student

        Args:
            json (dict): dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
