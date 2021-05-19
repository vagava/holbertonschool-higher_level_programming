#!/usr/bin/python3
'''class Square that defines a square'''


class Square():
    '''
    class Square that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
         Instantiation with optional size
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple or type(position[0]) != int\
                or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or type(value[0]) != int\
                or type(value[1]) != int or value[0] < 0 or value[1] < 0\
                or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        '''
        Public instance method: that returns the current
        square area.
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
        Public instance method  that prints in stdout
        the square with the character #
        '''
        if(self.__size == 0):
                print()
        else:
            if self.__position[1] > 0:
                print("\n"*self.__position[1], end="")
            for rows in range(self.__size):
                print(" "*self.__position[0]+"#"*self.__size)
