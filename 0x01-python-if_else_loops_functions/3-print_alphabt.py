#!/usr/bin/python3
for letter in range(97, 123):
    if letter in (101, 113):
        continue
    else:
        print("{:c}".format(letter), end="")
