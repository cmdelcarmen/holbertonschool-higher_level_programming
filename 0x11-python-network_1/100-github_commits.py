#!/usr/bin/python3
""" Write a Python script that takes your GitHub
    credentials (username and password) and uses the
    GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":

    owner = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    commits = requests.get(url).json()

    for index in range(0, 10):

        print(commits[index].get("sha"), end=": ")
        print(commits[index].get("commit").get("author").get("name"))
