#!/usr/bin/python3
'''
    Write a function that replaces or adds key/value in a dictionary.
'''
def update_dictionary(a_dictionary, key, value):

    if a_dictionary is None:
        return None

    if len(key) == 0:
        return None

    if len(a_dictionary) == 0:
        a_dictionary[key] = value

    for word in sorted(a_dictionary):
        if word == key:
            a_dictionary[word] = value
        else:
            a_dictionary[key] = value

    return a_dictionary
