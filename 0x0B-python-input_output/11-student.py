#!/usr/bin/python3
'''
class Student
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

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation'''
        dict_j = dict()
        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    dict_j[attr] = self.__dict__[attr]
            return dict_j
        return self.__dict__

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Student instance
        '''
        for key in json:
            self.__dict__[key] = json[key]
