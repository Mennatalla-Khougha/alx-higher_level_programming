#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }
    num = 0
    prev = 0
    for c in reversed(roman_number):
        if c not in roman_dict:
            return 0
        value = roman_dict[c]
        if value >= prev:
            num += value
        else:
            num -= value
        prev = value
    return num
