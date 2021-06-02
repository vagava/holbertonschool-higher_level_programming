#!/usr/bin/python3
'''
Module lookup
Module for write a function that returns the list
of available attributes and methods of an object.

'''


def lookup(obj):
    '''
    Return a list with available attributes and methods
    of methods
    '''
    return list(dir(obj))
