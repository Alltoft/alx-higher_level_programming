#!/usr/bin/python3
"""a function that divides all elements of a matrix
matrix must be a list of lists of integers or floats, otherwise raise a TE
Each row of the matrix must be of the same size, otherwise raise a TypeError
div must be a number (integer or float), otherwise raise a TypeError
div cant be equal to 0, otherwise raise a ZeroDivisionError
elements of the matrix should be divided by div, rounded to 2 decimal places"""


def matrix_divided(matrix, div):
    """here will devide the number
    with raising all the errors
    and returtning a new matrix"""
    new_mat = []
    for matri in range(len(matrix)):
        if not isinstance(matrix[matri], list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_row = []
        for x in range(len(matrix[matri])):
            resault = round(matrix[matri][x]/div, 2)
            new_row.append(resault)
        new_mat.append(new_row)

    return new_mat
