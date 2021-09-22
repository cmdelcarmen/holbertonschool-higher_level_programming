#!/usr/bin/python3
'''
    Write a function that computes the square value of all integers of a matrix.
'''
def square_matrix_simple(matrix=[]):

    newMatrix = []

    for row in range(len(matrix)):
        newMatrix.append(list(map(lambda x: x ** 2, matrix[row])))

    return(newMatrix)
