#!/usr/bin/python3
'''
Module of class BaseGeometry
Added method 'integer_validator'
Added clas Rectangle that inherits from BaseGeometry
'''


class BaseGeometry:
    '''
    Super class BaseGeometry
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


class Rectangle(BaseGeometry):
    '''
    Class that inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''
        constructor
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
