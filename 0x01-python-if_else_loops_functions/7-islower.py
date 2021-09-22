#!/usr/bin/python3
'''
    Write a function that checks for lowercase character.
'''
def islower(c):

    if ord(c) > 96:
        return True

    if ord(c) < 91:
        return False
