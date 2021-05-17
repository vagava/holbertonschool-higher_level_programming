#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as val_err:
        print("Exception:", val_err, file=sys.stderr)
        return False
    except TypeError as type_err:
        print("Exception:", type_err, file=sys.stderr)
        return False
