#!/usr/bin/python3
'''
    Complete this source code in order to print 3 times a string
    stored in the variable str, followed by its first 9 characters.
'''
str = "Holberton School"
print("{0!s}{0!s}{0!s}".format(str, str, str))
print("{:.9}".format(str))
