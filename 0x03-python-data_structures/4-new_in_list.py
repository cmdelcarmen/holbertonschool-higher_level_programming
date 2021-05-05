#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    newCopy_my_list = my_list[:]

    if idx < 0:
        return newCopy_my_list

    if idx > len(my_list):
        return newCopy_my_list

    newCopy_my_list[idx] = element

    return newCopy_my_list
