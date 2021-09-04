#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv[1]) == 1:
        letter = sys.argv[1]
    else:
        letter = ""

    myobj = {"q": letter}
    request = request.post("http://0.0.0.0:5000/search_user ", data=myobj)

    try:
        res = request.json()

        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")

