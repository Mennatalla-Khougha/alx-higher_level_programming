#!/usr/bin/python3
"""
This module multiply 2 matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiply 2 matrix

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        list: the resulting matrix of the multiplication
    """
    a = np.array(m_a)
    b = np.array(m_b)
    m_c = np.dot(a, b)
    return m_c
