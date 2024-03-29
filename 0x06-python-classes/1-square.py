#!/usr/bin/python3
'''class Square that defines a square'''


class Square():
    '''
    class Square that defines a square:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    '''
    def __init__(self, size):
        self.__size = size
