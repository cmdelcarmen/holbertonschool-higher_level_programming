#!/usr/bin/python3
'''
    Write a program that prints all numbers from 0
    to 98 in decimal and in hexadecimal (as in the following example).
'''
for count in range(99):
    print("{:d} = {}".format(count, hex(count)))
