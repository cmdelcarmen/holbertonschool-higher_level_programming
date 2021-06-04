#!/usr/bin/python3
'''comments'''


def read_file(filename=""):
    '''comments'''

    with open(filename) as txt_file:
        lines = txt_file.read()

    print(lines)
