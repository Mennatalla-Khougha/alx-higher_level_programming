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
        self.size = size

    @property
    def size(self):
        """Access the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with #"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print('')
