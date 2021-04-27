#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for position in range(len(str)):
        if position != n:
            new_str += str[position]
    return new_str
