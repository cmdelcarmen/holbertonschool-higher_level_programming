#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == "__main__":

    letter = ""

    if len(sys.argv) > 1:
        letter = sys.argv[1]

    pl = {'q': letter}
    res = requests.post('http://0.0.0.0:5000/search_user', data=pl)
    try:
        request = res.json()
        if not request:
            print("No result")
        else:
            print("[{}] {}".format(request.get('id'), request.get('name')))

    except ValueError:
        print("Not a valid JSON")
