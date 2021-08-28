#!/usr/bin/python3
'''Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)'''
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    data_ = urllib.parse.urlencode({'email': sys.argv[1]}).encode('ascii')
    req = urllib.request.Request(url, data_)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
