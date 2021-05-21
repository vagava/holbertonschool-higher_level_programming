#!/usr/bin/python3
''' Simple rectangle'''


class Rectangle:
    '''empty class Rectangle that defines a rectangle'''
    def __init__(self, width=0, height=0):
        ''' constructor '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''get value width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set value width'''
        if not isinstance(value, int):
            print(type(value))
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''get value height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set value height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
