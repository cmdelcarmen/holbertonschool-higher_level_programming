#!/usr/bin/python3
'''Contains addition function'''


def add_integer(a, b=98):
    '''Adds a and b and returns the result.
       Raises: TypeError: When non ints, and non floats are passed '''

    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
