#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    idx = len(my_list) - 1
    return(my_list[idx])
