#!/usr/bin/python3
"""This modula contain a class BaseGeometry"""


class BaseGeometry:
    """A class baseGeometry
    """

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate the value of a name

        Args:
            name (str): name string
            value (int): integer value greater than 0

        Raises:
            TypeError: when value not int
            ValueError: when value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
