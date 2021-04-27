#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        if 97 <= ord(str[letter]) <= 122:
            upper_ascii = ord(str[letter]) - 32
            print("{:c}".format(upper_ascii), end="")
        else:
            print(str[letter], end="")
    print()
