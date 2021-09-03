#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/stat """

import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
