#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """
    n_matrix = []
    for cols in matrix:
        output = list(map(lambda x: x**2, cols))
        n_matrix.append(output)
    return n_matrix
