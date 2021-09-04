#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/stat """

if __name__ == "__main__":

    import urllib.request

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as request:
        html = request.read()
        print("Body response:")
        print("\t - type: {}".format(type(html)))
        print("\t - content: {}".format(html))
        print("\t - utf8 content: {}".format(html.decode("utf-8")))
