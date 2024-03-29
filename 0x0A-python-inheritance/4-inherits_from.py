#!/usr/bin/python3
'''
Module of function that returns True if the object is
is an instance of, or if the object is an instance of
a class that inherited from,the specified class.
'''


def inherits_from(obj, a_class):
    '''
    returns True if the object is an instance of,
    or if the object is an instance of a class
    '''
    return (False if type(obj) == a_class
            else issubclass(type(obj), a_class))
