#!/usr/bin/python3
'''
Module write_file
function that writes a string to a text file
'''


def write_file(filename="", text=""):
    '''
    unction that writes a string to a text file (UTF8)
    and returns the number of characters written.
        - The function should create the file if doesn’t exist.
        - The function should overwrite the content of the file
        if it already exists.
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
