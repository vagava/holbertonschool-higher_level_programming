#!/usr/bin/python3
'''Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)'''
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    dict_ = {'email': sys.argv[1]}
    data = urllib.parse.urlencode(dict_).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
        print(the_page['email'])