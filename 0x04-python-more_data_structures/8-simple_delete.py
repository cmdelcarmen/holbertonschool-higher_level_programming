#!/usr/bin/python3
'''
    Write a function that deletes a key in a dictionary.
'''
def simple_delete(a_dictionary, key=""):

    sorted(a_dictionary)

    for word in sorted(a_dictionary):
        if word == key:
            del a_dictionary[word]

    return a_dictionary
