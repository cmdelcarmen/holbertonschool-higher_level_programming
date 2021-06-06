#!/usr/bin/python3
'''comments'''


def write_file(filename="", text=""):
    '''comments'''

    numOfCharacters = 0

    with open(filename, 'w+') as txt_file:
        for line in text:
            numOfCharacters += 1
        txt_file.write(text)

    return numOfCharacters
