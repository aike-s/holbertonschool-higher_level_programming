#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for one in matrix:
        for element in one:
            print("{:d}".(element), end='')
        print("")
