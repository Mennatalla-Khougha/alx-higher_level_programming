#!/usr/bin/python3
def raise_exception():
    number = "Hello"
    try:
        print("{:d}".format(number))
    except ValueError:
        raise TypeError
