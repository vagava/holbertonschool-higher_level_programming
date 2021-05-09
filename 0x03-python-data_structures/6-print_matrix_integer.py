#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    for rows in matrix:
        for columns in range(0, len(rows)):
            if columns == len(rows) - 1:
                print("{:d}".format(rows[columns]), end="")
            else:
                print("{:d}".format(rows[columns]), end=" ")
        print("")
