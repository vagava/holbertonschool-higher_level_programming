#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list == None:
        return None
    my_list.sort()
    idx = len(my_list) - 1
    return(my_list[idx])
