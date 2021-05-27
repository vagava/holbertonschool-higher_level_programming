#!/usr/bin/python3
'''
Module to multiplice two matrices.
To multiply two matrices is necesary that one
condition be met:
    - The 'number of columns' of the first matrix
    be equal to the 'number of rows' of the second
    matrix.
'''


def matrix_mul(m_a, m_b):
    '''
    Function to muntiply two matrices.
        - # of elements of the list in the matrix A
        must be equal to # of lists of matrix B.
    - The element that be in the row 'i' column 'j'
    of the matrix C=A*B is obtained by multipling
    the element of the row 'j' of the matrix A by
    the column 'j' of the matrix B, and adding it's
    result.
    '''
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

    matrix_res = []
    for aux in range(len(m_a)):
        row_result = []
        for i in range(len(m_b[0])):
            sum_mul = 0
            for j in range(len(m_a[0])):
                sum_mul += m_a[aux][j] * m_b[j][i]
            row_result.append(sum_mul)
        matrix_res.append(row_result)
    return matrix_res
