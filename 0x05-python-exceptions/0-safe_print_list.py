#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    int_numbersPrinted = 0

    for element in range(0, x):
        try:
            print(my_list[element], end="")
        except:
            break
        int_numbersPrinted = (int_numbersPrinted + 1)

    print()
    return int_numbersPrinted
