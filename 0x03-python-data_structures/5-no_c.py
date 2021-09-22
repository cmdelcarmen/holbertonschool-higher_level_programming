#!/usr/bin/python3
'''
    Write a function that removes all characters c and C from a string.
'''
def no_c(my_string):

    new_string = ""

    for count in range(0, len(my_string)):
        if ord(my_string[count]) != ord("c"):
            if ord(my_string[count]) != ord("C"):
                    new_string = new_string + my_string[count]

    return new_string
