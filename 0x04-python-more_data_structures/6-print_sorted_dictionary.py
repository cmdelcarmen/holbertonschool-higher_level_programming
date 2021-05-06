#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    sorted(a_dictionary)

    for word in sorted(a_dictionary):
        print(word, ":", a_dictionary[word])
