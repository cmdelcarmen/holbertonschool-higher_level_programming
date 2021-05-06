#!/usr/bin/python3


def best_score(a_dictionary):

    largestScore = 0
    largestScore_name = ""

    if a_dictionary is None:
        return None

    for key in sorted(a_dictionary):
        if a_dictionary[key] > largestScore:
            largestScore_name = key

    return largestScore_name
