#!/usr/bin/python3
"""
Module lazy_matrix_mul
Functions:
    lazy_matrix_mul(m_a, m_b)

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul()
    multiplies 2 matrices
        - m_a = matrix 1
        - m_b = matrix 2

    return new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(m_a[0]) != len(row):
            raise TypeError("each row of m_a must be of the same size")
        for columns in row:
            if not isinstance(columns, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(m_b[0]) != len(row):
            raise TypeError("each row of m_b must be of the same size")
        for columns in row:
            if not isinstance(columns, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = numpy.dot(m_a, m_b)
    return new_matrix.array()
