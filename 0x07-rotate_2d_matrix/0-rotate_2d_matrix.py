#!/usr/bin/python3
""" A module contains a function to rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Args:
        matrix (list of list of int): 2D matrix to rotate.

    The matrix must be edited in-place.
    """

    """ Transpose the matrix """
    num = len(matrix)
    for i in range(num):
        for x in range(i + 1, num):
            matrix[i][x], matrix[x][i] = matrix[x][i], matrix[i][x]

    matrix[:] = [row[::-1] for row in matrix]
