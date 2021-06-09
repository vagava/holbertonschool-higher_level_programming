#!/usr/bin/python3
'''class Rectangle that inherits from Base'''

from models.base import Base


class Rectangle(Base):
    '''Class rectangle'''

    # child class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Child args:
            width = int
            height = int
            x = int **Horizontal length**
            y = int **Vertical length**
        Parent args **Base**:
            id = instance id
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # private variables
    @property
    def width(self):
            '''width'''
            return self.__width

    @width.setter
    def width(self, value):
            self.is_int("width", value)
            self.is_positive("width", value)
            self.__width = value

    @property
    def height(self):
        '''height'''
        return self.__height

    @height.setter
    def height(self, value):
        self.is_int("height", value)
        self.is_positive("height", value)
        self.__height = value

    @property
    def x(self):
        '''x'''
        return self.__x

    @x.setter
    def x(self, value):
        Base.is_int("x", value)
        Base.is_negative("x", value)
        self.__x = value

    @property
    def y(self):
        '''y'''
        return self.__y

    @y.setter
    def y(self, value):
        Base.is_int("y", value)
        Base.is_negative("y", value)
        self.__y = value

    def area(self):
        '''returns the area value of the instance.'''
        return self.width * self.height

    def display(self):
        '''prints in stdout the instance with the character #'''
        if self.width == 0 or self.height == 0:
            print()
            return
        row = ' ' * self.x + '#' * self.width
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(row)

    def __str__(self):
        '''string representation'''
        string = '[Rectangle] ({}) {}/{} - {}/{}'
        return string.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''assign arguments'''

        if len(args) > 0:
            attrs = ('id', 'width', 'height', 'x', 'y')
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        keys = ['id', 'width', 'height', 'x', 'y']
