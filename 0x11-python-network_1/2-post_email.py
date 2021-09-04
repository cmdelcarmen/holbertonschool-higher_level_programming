#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/stat """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email).encode('utf8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8")) 
