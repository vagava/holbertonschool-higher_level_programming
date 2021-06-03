#!/usr/bin/python3
'''
Module class Student

'''


class Student:
    '''
    defines a student by:
    first_name
    last_name
    age
    '''
    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation'''
        return self.__dict__
