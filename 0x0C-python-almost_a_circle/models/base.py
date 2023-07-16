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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file

        Args:
            list_objs (list): list of base instance
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                dic = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the json string representation

        Args:
            json_string (str): json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                json_string = Base.from_json_string(file.read())
                return [cls.create(**d) for d in json_string]
        except:
            return []