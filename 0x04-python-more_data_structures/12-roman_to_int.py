#!/usr/bin/python3


def roman_to_int(roman_string):

    romanDi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prevValue = 0
    new_roman_string = ''.join(reversed(roman_string))

    if len(new_roman_string) == 0:
        return 0

    if not isinstance(roman_string, str):
        return 0

    for romanLetter in new_roman_string:
        if romanLetter not in romanDi:
            return 0

        if romanDi[romanLetter] >= prevValue:
            integer += romanDi[romanLetter]
        else:
            integer -= romanDi[romanLetter]

        prevValue = romanDi[romanLetter]

    return integer
