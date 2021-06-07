#!/usr/bin/python3
'''comments'''


import json


def save_to_json_file(my_obj, filename):
    '''comments'''

    new_content = json.dumps(my_obj)

    with open(filename, 'w+') as txt_file:
        txt_file.write(new_content)
