#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    for rows in matrix:
        for columns in rows:
            print("{:d}".format(columns), end=" ")
        print("")
