#!/usr/bin/python3
'''
    Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase
    and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
'''
for letter in range(90, 64, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter+32)), end="")
    else:
        print("{}".format(chr(letter)), end="")
