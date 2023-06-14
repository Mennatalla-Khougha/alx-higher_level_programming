#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    num = 0
    if not my_list:
        return score
    for row in my_list:
        score += (row[0] * row[1])
        num += row[1]
    score /= num
    return score
