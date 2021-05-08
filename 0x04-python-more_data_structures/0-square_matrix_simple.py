#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[elem * elem for elem in row] for row in matrix]
