#!/usr/bin/python3
'''This module contains: text_identation function'''


def text_indentation(text):
    '''This function prints the given text, but does 2 new lines
    after each of these characters: . ? : '''

    int_do_not_print = 0

    for index in range(0, len(text)):
        if int_do_not_print == 1:
            int_do_not_print = 0
            continue

        print(text[index], end="")

        if text[index] == '.' or text[index] == ':' or text[index] == '?':
            print()
            print()
            int_do_not_print = 1
