#!/usr/bin/python3
'''
    Write a function that finds all multiples of 2 in a list.
'''
def divisible_by_2(my_list=[]):

    if len(my_list) == 0:
        return None

    new_list = []

    for count in range(0, len(my_list)):
        if my_list[count] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
