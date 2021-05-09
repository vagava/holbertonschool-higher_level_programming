#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_num = []
    for num in my_list:
        if num % 2 == 0:
            list_num.append(True)
        else:
            list_num.append(False)
    return list_num
