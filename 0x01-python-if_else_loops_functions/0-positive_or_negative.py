#!/usr/bin/python3
'''
    This program will assign a random signed number to the variable number each time it is executed.
    Complete the source code in order to print whether the number stored in the variable number is positive or negative.
''''
        
import random
number = random.randint(-10, 10)

if number > 0:
    print("{:d} is positive".format(number))
if number == 0:
    print("{:d} is zero".format(number))
if number < 0:
    print("{:d} is negative".format(number))
