#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    sorted(a_dictionary)

    for word in sorted(a_dictionary):
        if word == key:
            del a_dictionary[word]

    return a_dictionary
