#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    lengthOfList = len(my_list)

    for count in reversed(range(lengthOfList)):
        print("{:d}".format(my_list[count]))
