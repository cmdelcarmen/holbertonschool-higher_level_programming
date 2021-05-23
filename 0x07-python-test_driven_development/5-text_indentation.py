#!/usr/bin/python3
'''This module contains: text_identation function'''


def text_indentation(text):
    '''This function prints the given text, but does 2 new lines
    after each of these characters: . ? : 
    Printed lines cannot start or end with spaces'''

    int_index = 0
    int_beginning_spaces = 1

    while (int_index < len(text)):
        if int_beginning_spaces == 1:
            '''takes care of input that start with a bunch of spaces'''
            while(text[int_index] == " "):
                int_index += 1
            int_beginning_spaces = 0

        print(text[int_index], end="")

        if text[int_index] == '.' or text[int_index] == ':' or text[int_index] == '?':
                 print()
                 print()
                 if int_index < (len(text) - 1):
                     '''makes sure program is not trying to read an out of range value'''
                     if text[int_index + 1] == " ":
                        '''makes sure next printed line does not start with a space'''
                        while(text[int_index + 1] == " " and (int_index < (len(text) - 1))):
                            int_index += 1
                            if int_index >= len(text) - 1:
                                '''breaks before trying to read an out of range value'''
                                break

        int_index += 1
