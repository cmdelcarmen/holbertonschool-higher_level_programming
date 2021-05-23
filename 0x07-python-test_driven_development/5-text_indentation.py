#!/usr/bin/python3
'''This module contains: text_identation function'''


def text_indentation(text):
    '''This function prints the given text, but does 2 new lines
    after each of these characters: . ? :
    Printed lines cannot start or end with spaces'''

    idx = 0
    beginning_spaces = 1

    if not type(text) is str:
        raise TypeError("text must be a string")

    while (idx < len(text)):
        if beginning_spaces == 1:
            '''takes care of input that start with a bunch of spaces'''
            while(text[idx] == " "):
                idx += 1
            beginning_spaces = 0

        print(text[idx], end="")

        if text[idx] == '.' or text[idx] == ':' or text[idx] == '?':
                print()
                print()
                if idx < (len(text) - 1):
                    '''makes sure next printed line does not start with a space
                    if statements make sure program is not trying to read
                    an out of range value'''
                    if text[idx + 1] == " ":
                        while(text[idx + 1] == " " and idx < (len(text) - 1)):
                            idx += 1
                            if idx >= len(text) - 1:
                                break

        idx += 1
