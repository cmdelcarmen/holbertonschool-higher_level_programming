#!/usr/bin/python3
'''comments'''


import json


def save_to_json_file(my_obj, filename):
    '''comments'''

    with open(filename, 'w+') as filename:
        json.dump(my_obj, filename)
