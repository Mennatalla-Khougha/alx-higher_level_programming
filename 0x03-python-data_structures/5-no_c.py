#!/usr/bin/python3
def no_c(my_string):
    chars = ['c', 'C']
    str = ''.join(c for c in my_string if c not in chars)
    return str
