#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):

    newList = []

    if len(my_list) == 0:
        return None

    newList = list(map(lambda x: x * number, my_list))

    return newList
