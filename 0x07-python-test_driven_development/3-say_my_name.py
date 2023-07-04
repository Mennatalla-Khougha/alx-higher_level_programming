#!/usr/bin/python3
"""
This Modula print my name
"""


def say_my_name(first_name, last_name=""):
    """This function prints my name

    Args:
        first_name (str): The first name
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: if the first name is not a string
        TypeError: if the last name is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        if first_name == "":
            print("My name is {}".format(last_name))
            return
        print("My name is {} {}".format(first_name, last_name))
