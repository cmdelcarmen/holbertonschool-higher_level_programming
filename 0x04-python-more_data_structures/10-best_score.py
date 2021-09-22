#!/usr/bin/python3
'''
    Write a function that returns a key with the biggest integer value.
'''
def best_score(a_dictionary):

    largestScore = 0
    largestScore_name = ""

    if a_dictionary is None:
        return None

    if not a_dictionary:
        return None

    for key in a_dictionary:
        if a_dictionary[key] > largestScore:
            largestScore = a_dictionary[key]
            largestScore_name = key

    return largestScore_name
