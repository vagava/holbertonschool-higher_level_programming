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
    Args:
            m_a (matrix): matrix ``A``
            m_b (matrix): matrix ``B``
    Return:
            new_matrix
    """
    return numpy.dot(m_a, m_b)

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print ("__")
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
