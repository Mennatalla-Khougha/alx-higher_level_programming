#!/usr/bin/python3
"""
Define a class square.
"""


class Square:
    """
    A class square the defines a square.
    """

    def __init__(self, size=0):
        """
        initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
