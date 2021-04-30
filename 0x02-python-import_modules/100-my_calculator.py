#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    calculatedResult = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif (sys.argv[2] == '+'):
        print("{} + {} = ".format(sys.argv[1], sys.argv[3]), end="")
        print(add(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '-'):
        print("{} - {} = ".format(sys.argv[1], sys.argv[3]), end="")
        print(sub(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '*'):
        print("{} * {} = ".format(sys.argv[1], sys.argv[3]), end="")
        print(mul(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '/'):
        print("{} / {} = ".format(sys.argv[1], sys.argv[3]), end="")
        print(div(int(sys.argv[1]), int(sys.argv[3])))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
