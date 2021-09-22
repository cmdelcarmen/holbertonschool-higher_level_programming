#!/usr/bin/python3
'''
    Write a program that prints the result of the addition of all arguments
'''
import sys

if __name__ == "__main__":

    sumOfAllArgv = 0

    if len(sys.argv) > 1:
        for count in range(1, (len(sys.argv))):
            sumOfAllArgv += int(sys.argv[count])

    print(sumOfAllArgv)
