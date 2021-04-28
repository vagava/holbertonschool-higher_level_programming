#!/usr/bin/python3
from sys import argv


def sum_all():
    sum = 0
    for num in range(1, len(argv)):
        sum += int(argv[num])
    print(sum)

if __name__ == "__main__":
    sum_all()
