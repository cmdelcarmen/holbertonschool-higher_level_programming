#!/usr/bin/python3

import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("0")

    else:
        print(int(sys.argv[1]) + int(sys.argv[2]))
