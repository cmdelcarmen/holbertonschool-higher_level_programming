#!/usr/bin/python3
'''
    This program will assign a random signed number to the variable number each time it is executed.
    Complete the source code in order to print the last digit of the number stored in the variable number.
'''
import random
number = random.randint(-10000, 10000)

isNegative = False

if number < 0:
    number *= -1
    isNegative = True

lastDigit = number % 10

if isNegative is True:
    lastDigit *= -1
    number *= -1

print("Last digit of {:d} is {:d}".format(number, lastDigit), end=" ")

if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
elif lastDigit <= 5:
    print("and is less than 6 and not 0")
