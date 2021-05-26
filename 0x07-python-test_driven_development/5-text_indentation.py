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
    strip_text = text.strip()
    replace_point = strip_text.replace('.', '.\n\n')
    replace_question = replace_point.replace('?', '?\n\n')
    replace_colon = replace_question.replace(':', ':\n\n')
    final_text = replace_colon.replace('\n ', '\n')
    print(final_text, end="")
