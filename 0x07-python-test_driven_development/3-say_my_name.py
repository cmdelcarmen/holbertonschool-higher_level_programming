#!/usr/bin/python3
'''name funciton'''


def say_my_name(first_name, last_name=""):
    '''Function'''

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
