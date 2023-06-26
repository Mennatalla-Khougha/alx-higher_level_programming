#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e))
        result = None
    return result
