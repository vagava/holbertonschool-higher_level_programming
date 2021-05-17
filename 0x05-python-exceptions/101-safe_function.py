#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as error:
        print("Exception:", error, file=sys.stderr)
        return None
