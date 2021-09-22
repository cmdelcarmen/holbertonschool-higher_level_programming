#!/usr/bin/python3
'''
    Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
'''
for count in range(97, 123):
    if count != 101 and count != 113:
        print("{}".format(chr(count)), end="")
