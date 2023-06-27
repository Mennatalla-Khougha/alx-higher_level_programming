#!/usr/bin/python3
"""
Define a class square.
"""


class Square:
    """
    A class square the defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): 2 positive int
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Access the position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position property"""
        def check_position(val):
            """
            check the input

            Args:
                value (tuple): 2 positive ints
            """
            if type(val) == tuple and len(val) == 2:
                if all(type(i) == int and i >= 0 for i in val):
                    return True
            return False

        if not check_position(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print the square with #"""
        if self.size == 0:
            print("")
        else:
            for k in range(self.position[1]):
                print("")
            for i in range(self.size):
                for n in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end="")
                print('')
