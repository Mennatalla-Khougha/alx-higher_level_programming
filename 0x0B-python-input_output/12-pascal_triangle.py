#!/usr/bin/python3
"""This module return the pascal triangle of n"""


def pascal_triangle(n):
    """Return a list of lists of ints

    Args:
        n (int): no of rows in the triangle

    Returns:
        list: list of list of pascal triangle
    """
    if n <= 0:
        return []
    list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            ele = list[i - 1][j - 1] + list[i - 1][j]
            row.append(ele)
        row.append(1)
        list.append(row)
    return list
