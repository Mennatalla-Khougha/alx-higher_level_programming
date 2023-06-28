#!/usr/bin/python3
"""
Define a class.
"""


import math


class MagicClass:
    """Define a class"""

    def __init__(self, radius=0):
        """Initialize the class"""
        self.radius = radius

    @property
    def radius(self):
        """Access the radius property"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) == int or type(value) == float:
            self.__radius = value
        else:
            raise TypeError("radius must be a number")

    def area(self):
        """Return the area"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius
