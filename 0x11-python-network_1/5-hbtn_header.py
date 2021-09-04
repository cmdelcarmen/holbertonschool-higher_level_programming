#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    print(requests.get(url).headers.get("X-Request-Id"))
