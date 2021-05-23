#!/usr/bin/python3
'''This module contains: text_identation function'''


def text_indentation(text):
    '''This function prints the given text, but does 2 new lines
    after each of these characters: . ? : 
    Printed lines cannot start or end with spaces'''

    int_index = 0
    beginning_spaces = 1

    while (int_index < len(text)):
        if beginning_spaces == 1:
            '''takes care of input that start with a bunch of spaces'''
            while(text[int_index] == " "):
                int_index += 1
            beginning_spaces = 0

        print(text[int_index], end="")

        if text[int_index] == '.' or text[int_index] == ':' or text[int_index] == '?':
                 print()
                 print()
                 int_index+= 1

        int_index += 1
