#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = (list(map(lambda x: list(map(lambda y: y * y, x)), matrix)))
    return new_matrix
