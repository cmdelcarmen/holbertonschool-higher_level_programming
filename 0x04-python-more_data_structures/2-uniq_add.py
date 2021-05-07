#!/usr/bin/python3


def uniq_add(my_list=[]):

    total = 0
    numbersAdded = []

    total += my_list[0]
    numbersAdded.append(my_list[0])

    for number in my_list:
        if number not in numbersAdded:
            total += number
            numbersAdded.append(number)

    return total
