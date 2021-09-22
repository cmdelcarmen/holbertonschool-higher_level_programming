#!/usr/bin/python3
'''
    Write a function that replaces an element in a list at a specific
    position without modifying the original list (like in C).
'''
def new_in_list(my_list, idx, element):

    newCopy_my_list = my_list[:]

    if idx < 0:
        return newCopy_my_list

    if idx > (len(my_list) - 1):
        return newCopy_my_list

    newCopy_my_list[idx] = element

    return newCopy_my_list
