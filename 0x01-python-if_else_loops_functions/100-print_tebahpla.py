#!/usr/bin/python3
'''
    Write a function that computes a to the power of b and return the value.
'''
for letter in range(90, 64, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter+32)), end="")
    else:
        print("{}".format(chr(letter)), end="")
