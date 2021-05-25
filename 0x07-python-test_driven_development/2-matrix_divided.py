#!/usr/bin/python3
'''
Module matix
With the modutle we can to divides all elements of a matrix
Matrix must be a list of list of integers
div: can't be equal to 0
Return a new matrix
'''


def matrix_divided(matrix, div):
    ''' function that divides all elements of a matrix.
    Usage: matrix_divided(matrix, div)
    contains the following features:
        - matrix must be a list of lists of integers or floats
        - Each row of the matrix must be of the same size
        - div must be a number (integer or float) and can’t be equal to 0
        - All elements of the matrix should be divided by div, rounded to
        2 decimal places
    '''
    if not isinstance(matrix, list) or len(matrix) < 1 or len(matrix[0]) < 1:
        raise TypeError("matrix must be a matrix (list of lists) of" +
                        " integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for columns in rows:
            if not isinstance(columns, (int, float)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
            else:
                new_row.append(round(columns/div, 2))
        new_matrix.append(new_row)
    return new_matrix
