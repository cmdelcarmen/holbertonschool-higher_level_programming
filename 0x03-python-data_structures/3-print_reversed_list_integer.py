#!/usr/bin/python3
'''
    Write a function that prints all integers of a list, in reverse order.
'''

def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        return

    lengthOfList = len(my_list)

    for count in reversed(range(lengthOfList)):
        print("{:d}".format(my_list[count]))
