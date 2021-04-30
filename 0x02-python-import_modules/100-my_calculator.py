#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    calculatedResult = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("argv total:", end=" ")
        print(len(sys.argv))
        exit(1)

    elif (sys.argv[2] == '+'):
        print(add(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '-'):
        print(sub(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '*'):
        print(mul(int(sys.argv[1]), int(sys.argv[3])))

    elif (sys.argv[2] == '/'):
        print(div(int(sys.argv[1]), int(sys.argv[3])))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
