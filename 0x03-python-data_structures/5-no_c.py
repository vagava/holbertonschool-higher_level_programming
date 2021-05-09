#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for leter in my_string:
        if leter not in (["c", "C"]):
            new_string += leter
    return new_string
