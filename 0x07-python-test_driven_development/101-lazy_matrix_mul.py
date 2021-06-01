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
    return numpy.dot(m_a, m_b)
