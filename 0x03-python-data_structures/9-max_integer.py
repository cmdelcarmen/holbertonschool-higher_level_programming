#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    largestNum = my_list[0]

    for count in range(0, len(my_list)):
        if largestNum < my_list[count]:
            largestNum = my_list[count]

    return largestNum
