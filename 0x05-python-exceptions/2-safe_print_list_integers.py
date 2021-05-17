#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    int_totalPrintedNums = 0

    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
            int_totalPrintedNums = int_totalPrintedNums + 1
        except:
            continue

    print()
    return int_totalPrintedNums
