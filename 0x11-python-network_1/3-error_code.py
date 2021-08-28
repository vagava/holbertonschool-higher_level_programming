#!/usr/bin/python3
'''Python script that takes in a URL, sends a request tothe URL
and displays the body of the response (decoded in utf-8).'''
from urllib import request, parse
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
