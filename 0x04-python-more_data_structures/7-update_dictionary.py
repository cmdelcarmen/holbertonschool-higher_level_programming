#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):

    if not a_dictionary:
        return None

    for word in sorted(a_dictionary):
        if word == key:
            a_dictionary[word] = value
        else:
            a_dictionary[key] = value

    return a_dictionary
