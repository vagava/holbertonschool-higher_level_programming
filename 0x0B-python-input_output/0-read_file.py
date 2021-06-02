#!/usr/bin/python3
'''
Module Read File
function that reads a text file
'''


def read_file(filename=""):
    '''
    function that reads a text file
    and prints it to stdout
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
