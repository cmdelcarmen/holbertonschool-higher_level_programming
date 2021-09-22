#!/usr/bin/python3
'''
    Write a function that prints a string in uppercase followed by a new line.
'''
def uppercase(str):

    lengthOfString = len(str)

    for count in range(lengthOfString):
        if ord(str[count]) > 96:
                upperCaseLetter = chr(((ord(str[count])) - 32))
        else:
            upperCaseLetter = str[count]

        print("{}".format(upperCaseLetter), end="")

    print("")
