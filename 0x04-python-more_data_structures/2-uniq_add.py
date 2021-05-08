#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    add = (reduce(lambda x, y: x + y, set(my_list)))
    return add
