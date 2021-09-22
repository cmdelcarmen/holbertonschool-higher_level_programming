#!/usr/bin/python3
'''
    Write a function that prints the last digit of a number.
'''
def print_last_digit(number):

    if number < 0:
        number *= -1

    print("{}".format((number % 10)), end="")
    return(number % 10)
