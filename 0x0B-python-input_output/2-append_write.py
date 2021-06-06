#!/usr/bin/python3
'''comments'''


def append_write(filename="", text=""):
    '''commments'''

    numOfCharactersAdded = len(text)

    with open(filename, 'a+') as txt_file:
        txt_file.writelines(("").join(text))

    return numOfCharactersAdded
