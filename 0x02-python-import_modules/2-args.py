#!/usr/bin/python3
from sys import argv


def argument():
    num_args = len(argv)
    if num_args == 1:
        print("{} arguments.".format(num_args - 1))
    elif num_args == 2:
        print("{:d} argument:".format(num_args - 1))
        print("{:d}: {:s}".format(num_args - 1, argv[1]))
    else:
        print("{:d} arguments:".format(num_args - 1))
        for position in range(1, num_args):
            print("{:d}: {:s}".format(position, argv[position]))

if __name__ == "__main__":
    argument()
