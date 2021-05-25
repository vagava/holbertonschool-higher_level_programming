#!/usr/bin/python3
'''
function that adds tow integers
    a : must be an integer
    b : must be an integer
if type of 'a' or 'b' is float must be casted
to integers
'''


def add_integer(a, b=98):
    '''
    add two integers
    a : must be an integer
    b : must be an integer
    if type of 'a' or 'b' is float must be casted
    to integers
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
