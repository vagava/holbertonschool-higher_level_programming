#!/usr/bin/python3
'''
Module Base
This module contains the class “base” of all other classes.
'''
import json


class Base:
    '''The goal of it is to manage id attribute in all your future
        classes and to avoid duplicating the same code
        (by extension, same bugs)'''

    __nb_objects = 0

    # constructor
    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    # method validate integer
    @staticmethod
    def is_int(attr, value):
            '''validates that input is integer'''
            if type(value) is not int:
                raise TypeError('{} must be an integer'.format(attr))

    # method validate positive
    @staticmethod
    def is_positive(attr, value):
            '''validates that input is positive'''
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))

    # method validate negative
    @staticmethod
    def is_negative(attr, value):
        '''validates that input is negative'''
        if value < 0:
            raise ValueError('{} must be >= 0'.format(attr))

    # start Json
    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation '''
        if list_dictionaries is None or len(list_dictionaries) == 0 \
            or not list_dictionaries:
            return "[]"   # says "return the string" not "the empty list"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation'''
        if list_objs is None:
            list_dictionary = []
        else:
            list_dictionary = [x.to_dictionary() for x in list_objs]
        # creo un archivo nombre_de_la_clase.json en modo "write"
        # y me aseguro de cerrarlo con with
        with open(cls.__name__ + '.json', 'w') as file:
            return file.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if (cls.__name__ == "Square"):
            dummy = cls(2)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(2, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                dictionarys = cls.from_json_string(file.read())
                return [cls.create(**diction) for diction in dictionarys]
        except:
            return[]
