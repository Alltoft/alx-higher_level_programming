#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for a in range(len(i)):
            if a == (len(i) - 1):
                print('{:d}'.format(i[a]), end='')
            else:
                print('{:d}'.format(i[a]), end=' ')
        print()
