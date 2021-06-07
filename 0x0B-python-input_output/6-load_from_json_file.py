#!/usr/bin/python3
'''comments'''


import json


def load_from_json_file(filename):
    '''comments'''
    with open(filename) as txt_file:
        py_object = json.load(txt_file)

    return py_object
