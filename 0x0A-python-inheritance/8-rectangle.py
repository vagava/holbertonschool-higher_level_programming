#!/usr/bin/python3
'''
Module of class Rectangle
Added clas Rectangle that inherits from BaseGeometry
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''
        constructor
        '''
        super().integer_validator("width", width)
        super().integer_validator("width", height)
        self.__width = width
        self.__height = height
