#!/usr/bin/python3
'''
Module of class BaseGeometry
Aded method 'integer_validator'
'''


class BaseGeometry:
    '''
    class in construction
    class in construction
    '''
    def area(self):
        '''
        raises an Exception with the
        message area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        that validates value:
            -if value is an integer
            - if value is less or equal to 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
