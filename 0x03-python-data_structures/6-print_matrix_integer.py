#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if (len(matrix) == 0:
        return None

    for count in range(len(matrix)):
        for count1 in range(len(matrix[count])):
            print("{:d}".format(matrix[count][count1]), end="")

            if count1 != ((len(matrix) - 1)):
                print(" ", end ="")
        print()
