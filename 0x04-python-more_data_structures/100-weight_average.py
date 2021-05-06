#!/usr/bin/python3


def weight_average(my_list=[]):

    average = 0
    divisor = 0

    if len(my_list) == 0:
            return 0

    for score in my_list:
        average += (score[0] * score[1])
        divisor += score[1]

    average = (average / divisor)
    return average
