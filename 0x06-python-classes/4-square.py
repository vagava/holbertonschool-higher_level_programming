#!/usr/bin/python3
'''class Square that defines a square'''


class Square():
    '''
    class Square that defines a square
    '''
    def __init__(self, size=0):
        '''
         Instantiation with optional size
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''
        Private instance attribute: size.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Public instance method: that returns the current
        square area.
        '''
        return self.__size * self.__size
