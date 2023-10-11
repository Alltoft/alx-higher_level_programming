#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x : x ** 2
    result = [[square(a) for a in i] for i in matrix]
    return result
