#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {key: a_dictionary[key] for key in sorted(a_dictionary.keys())}
    for key, value in new_dict.items():
        print(f"{key}: {value}")
