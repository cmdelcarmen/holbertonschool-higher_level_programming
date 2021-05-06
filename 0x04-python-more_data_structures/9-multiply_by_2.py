#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    new_dictionary = {}

    for num in a_dictionary:
        new_dictionary[num] = num
        new_dictionary[num] = a_dictionary[num] * 2

    return new_dictionary
