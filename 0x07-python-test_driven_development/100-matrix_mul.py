#!/usr/bin/python3
"""
This module multiply 2 matrix
"""


def matrix_mul(m_a, m_b):
    """
    This function multiply 2 matrix

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        list: the resulting matrix of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")

    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for i in range(len(m_a)):
        m_c.append([])
        for j in range(len(m_b[0])):
            m_c[i].append(0)
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
