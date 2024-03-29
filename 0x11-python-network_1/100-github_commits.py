#!/usr/bin/python3
'''evaluates candidates applying for a back-end position'''
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'\
           .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    data = r.json()
    for i in range(len(data)):
        if i < 10:
            print('{}: {}'.format(data[i]['sha'],
                                  data[i]['commit']['author']['name']))
        else:
            break
