#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for one in matrix:
        for i, element in enumerate(one):
            if (i != 0):
                print(" ", end='')
            print("{:d}".(element), end='')
        print("")
