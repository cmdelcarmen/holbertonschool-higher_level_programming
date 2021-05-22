#!/usr/bin/python3
'''prints a square'''


def print_square(size):
    '''prints a square'''

    if not type(size) is int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for count in range(0, size):
        for count2 in range(0, size):
            print("#", end="")
        print()
