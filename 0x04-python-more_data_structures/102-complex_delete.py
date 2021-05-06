#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    for word in sorted(a_dictionary):
        if value == a_dictionary[word]:
            del a_dictionary[word]

    return a_dictionary
