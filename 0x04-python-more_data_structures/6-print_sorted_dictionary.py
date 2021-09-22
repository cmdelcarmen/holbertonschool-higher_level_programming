#!/usr/bin/python3
'''
    Write a function that prints a dictionary by ordered keys.
'''
def print_sorted_dictionary(a_dictionary):

    if not a_dictionary:
        return None

    for word in sorted(a_dictionary):
        print(word, end="")
        print(":", end=" ")
        print(a_dictionary[word])
