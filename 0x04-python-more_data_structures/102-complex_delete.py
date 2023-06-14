#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for key, val in a_dictionary.items():
        if val == value:
            continue
        new_dict[key] = val
    return new_dict
