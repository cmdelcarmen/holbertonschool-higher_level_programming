#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    request = requests.get(url)
    request = request.json()

    for i in range(10 if len(request) > 10 else len(request)):
        author = request[i].get('commit').get('author').get('name')
        sha = request[i].get('sha')
        print("{}: {}".format(sha, author))
