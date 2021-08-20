#!/usr/bin/python3
''' function that finds a peak in a list of unsorted integers.'''
def find_peak(list_of_integers):
    '''function that finds a peak in a list'''
    peak = None
    if list_of_integers and len(list_of_integers) > 0:
        if len(list_of_integers) == 1:
            return list_of_integers[0]
        # list > 1
        for i in range(len(list_of_integers)):
            if not list_of_integers[i - 1]:
                if list_of_integers[i + 1] <= list_of_integers[i]:
                    return list_of_integers[1]
            elif not list_of_integers[i + 1]:
                if list_of_integers[i - 1] <= list_of_integers[i]:
                    return list_of_integers[i]
            else:
                if list_of_integers[i - 1] <= list_of_integers[i] and list_of_integers[i + 1] <= list_of_integers [i]:
                    return list_of_integers[i]
        return None

