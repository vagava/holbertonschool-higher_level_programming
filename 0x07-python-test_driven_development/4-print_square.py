#!/usr/bin/python3
'''
Module for prints a square
With this module we can to printa square wtih
the character '#'.
The square will have a certan size.
The size must be an pisitive integer

'''


def print_square(size):
    '''
    This function print a square with the character '#'
    Size: is the length of the square and must be have the
    following features:
        - size must be an integer.
        - size must be >= 0.
        - size must be an integer
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#"*size)
