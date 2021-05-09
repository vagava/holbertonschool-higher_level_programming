#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    for rows in matrix:
        for columns in rows:
            if len(rows) > 1:
                print("{:d}".format(columns), end=" ")
            else:
                print("{:d}".format(columns), end="")
        print("")
