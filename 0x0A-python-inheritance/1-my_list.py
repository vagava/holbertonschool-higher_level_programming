#!/usr/bin/python3
'''
module my_list
Module of class MyList that inherits from list.

'''


class MyList(list):
    '''
    Public instance method:
        def print_sorted(self):
        that prints the list, but sorted (ascending sort).
    can assume that all the elements
    of the list will be of type int
    '''
    def print_sorted(self):
        '''
        that prints the list, but sorted (ascending sort).
        '''
        new_list = self.copy()
        new_list.sort()
        print(new_list)
