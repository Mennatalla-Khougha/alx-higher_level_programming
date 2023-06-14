#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    k = None
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            k = key
    return k
