#!/usr/bin/python3

''' Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.'''

import requests
import sys

if __name__ == "__main__":
    dict_ = {}
    if len(sys.argv) > 1:
        dict_['q'] = sys.argv[1]
    else:
        dict_['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data=dict_)
    try:
        if len(r.json()) > 0:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        else:
            print('No result')
    except BaseException:
        print('Not a valid JSON')
