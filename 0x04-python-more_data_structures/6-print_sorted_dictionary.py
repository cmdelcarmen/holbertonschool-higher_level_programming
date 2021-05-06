#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    if not a_dictionary:
        return None

    for word in sorted(a_dictionary):
        print(word, end="")
        print(":", end=" ")
        print(a_dictionary[word])
