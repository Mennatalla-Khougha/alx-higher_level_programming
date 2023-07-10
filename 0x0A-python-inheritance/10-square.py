#!/usr/bin/python3
"""This is a Rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a Square subclass"""
    def __init__(self, size):
        """initialize the square

        Args:
            size (int): size of square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
