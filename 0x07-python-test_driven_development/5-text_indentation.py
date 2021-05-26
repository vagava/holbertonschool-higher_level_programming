#!/usr/bin/python3
'''
Module Text indentation
prints a text with 2 new lines after each of these
characters: '.', '?' and ':'
text must be a string
'''


def text_indentation(text):
    '''
    Function text_indentation
    function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'

    text: must be a string
    There should be no space at the beginning or
    at the end of each printed line.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # replace ., ?, : and add \n\n
    replace_point = text.replace('.', '.\n\n')
    replace_question = replace_point.replace('?', '?\n\n')
    replace_clon = replace_question.replace(':', ':\n\n')
    # string reconstruction
    str_ = ""
    lines = replace_clon.splitlines()
    for num_line in range(len(lines)):
        if num_line == len(lines) - 1:
            str_ += lines[num_line].strip()
        else:
            str_ += lines[num_line].strip() + '\n'
    print(str_, end="")
