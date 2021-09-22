#!/usr/bin/python3
'''
    Write a function that prints the numbers from 1 to 100 separated by a space.
'''
def fizzbuzz():

        for count in range(1, 101):
            if (count % 3) == 0 and (count % 5) == 0:
                print("FizzBuzz", end=" ")

            elif (count % 3) == 0:
                print("Fizz", end=" ")

            elif (count % 5) == 0:
                print("Buzz", end=" ")

            else:
                print("{}".format(count), end=" ")
