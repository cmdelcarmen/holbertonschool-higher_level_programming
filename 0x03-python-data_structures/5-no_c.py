#!/usr/bin/python3


def no_c(my_string):

    new_string = ""

    for count in range(0, len(my_string)):
        if ord(my_string[count]) != ord("c"):
            if ord(my_string[count]) != ord("C"):
                    new_string = new_string + my_string[count]

    return new_string
