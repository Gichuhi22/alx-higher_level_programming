#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for item in matrix:
        newmatrix = []
        for i in item:
            newmatrix.append(i**2)
        new_matrix.append(newmatrix)
    return new_matrix
