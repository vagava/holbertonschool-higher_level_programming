#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in range(0, x+1):
            print(my_list[element], end="")
        print()
        return element
    except BaseException:
        print()
        return element
