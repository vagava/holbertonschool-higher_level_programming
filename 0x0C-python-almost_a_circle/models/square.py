#!/usr/bin/python3
'''Module of class Square that inherits from Rectangle'''

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''

    # constructor
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Parent args **Rectangle**:
            size = int
            x = int **Horizontal length**
            y = int **Vertical length**
            id = instance id
        '''
        super().__init__(size, size, x, y, id)

    # private variables
    @property
    def size(self):
        '''size: positive int'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        ''' string representation '''
        string = '[Square] ({}) {}/{} - {}'
        return string.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        ''' args: is the list of arguments - no-keyworded arguments
            order of args: id, size, x, y'''
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            attrs = ('id', 'size', 'x', 'y')
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        '''returns the dictionary representation'''
        keys = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in keys}
