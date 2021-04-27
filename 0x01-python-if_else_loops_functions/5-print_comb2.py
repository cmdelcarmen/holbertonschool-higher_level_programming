#!/usr/bin/python3

for count in range(100):
    if count < 10:
        print("0", end="")
    if count != 99:
        print("{:d}".format(count), end=", ")
    elif count == 99:
        print("{:d}".format(count))
