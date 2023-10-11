#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = matrix.copy()
    for i in range(len(matrix)):
        result[i] = list(map(lambda h: h ** 2, matrix[1]))
    return result
