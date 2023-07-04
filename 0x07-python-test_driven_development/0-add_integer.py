#!/usr/bin/python3
"""
This Module adds 2 ints
"""


def add_integer(a, b=98):
    """The Function adds 2 integers

    Args:
        a (int): first integer to add
        b (int, optional): second integer to add. Defaults to 98.

    Raises:
        TypeError: When a or b is not an integer or a float

    Returns:
        int: adding a to b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
