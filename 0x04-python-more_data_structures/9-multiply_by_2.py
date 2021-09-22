#!/usr/bin/python3
'''
    Write a function that returns a new dictionary with all values multiplied by 2
'''
def multiply_by_2(a_dictionary):

    new_dictionary = {}

    for num in a_dictionary:
        new_dictionary[num] = num
        new_dictionary[num] = a_dictionary[num] * 2

    return new_dictionary
