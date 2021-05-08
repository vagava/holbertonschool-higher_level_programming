#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = (list(map(lambda lista: list(
                                            map(lambda elemento:
                                                elemento * elemento,
                                                lista)), matrix)))
    return new_matrix
