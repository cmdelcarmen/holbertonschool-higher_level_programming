#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        return

    lengthOfList = len(my_list)

    for count in reversed(range(lengthOfList)):
        print("{:d}".format(my_list[count]))
