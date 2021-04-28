#!/usr/bin/python3


for letter in range(90, 64, -1):
    if (letter % 2) == 0:
        print(chr(letter + 32), end="")
    if (letter % 2) != 0:
        print(chr(letter), end="")
