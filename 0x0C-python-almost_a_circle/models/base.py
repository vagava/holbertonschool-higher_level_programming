#!/usr/bin/python3
'''
Module Base
This module contains the class “base” of all other classes.
'''


class Base:
    '''
    This class will be the “base” of all other classes.
    The goal of it is to manage id attribute in all future classes.
        __nb_objects
        id
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        If id is not None, assign the public instance attribute id.
        '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

