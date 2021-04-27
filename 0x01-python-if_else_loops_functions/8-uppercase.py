#!/usr/bin/python3
def uppercase(str):
    for position in range(len(str)):
        if 97 <= ord(str[position]) <= 122:
            letter= ord(str[position]) - 32
        else:
            letter = ord(str[position])
        print("{:c}".format(letter), end="")
    print()

