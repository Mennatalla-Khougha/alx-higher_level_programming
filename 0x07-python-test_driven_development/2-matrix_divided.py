#!/usr/bin/python3
"""
This Modula divide all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix by  a given number

    Args:
        matrix (list): list of lists
        div (int or float): a number to divide the matrix by

    Raises:
        ZeroDivisionError: when div is 0
        TypeError: if matrix not a list of lists
        TypeError: if div not a number
        TypeError: if the matrix rows not of the same length
        TypeError: if elements of the matrix are not numbers

    Returns:
        list of lists: a new matrix
    """
    msg2 = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == [] or matrix == [[]]:
        raise TypeError(msg2)
    matrix2 = []
    len2 = len(matrix)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    msg1 = "Each row of the matrix must have the same size"
    for raw in matrix:
        if not isinstance(raw, list):
            raise TypeError(msg2)
        if len(raw) != len(matrix[0]):
            raise TypeError(msg1)
        matrix2.append(raw[:])

    for r in range(len2):
        for i in range(len(matrix[0])):
            if type(matrix2[r][i]) not in [int, float]:
                raise TypeError(msg2)
            matrix2[r][i] /= div
            matrix2[r][i] = round(matrix2[r][i], 2)
    return matrix2
