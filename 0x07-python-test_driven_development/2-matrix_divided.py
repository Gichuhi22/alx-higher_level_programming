#!/usr/bin/python3
""" define matrix_divided"""


def matrix_divided(matrix, div):
    """
    divides each element of the matrix with a given value
    returns new matrix with divided values
    raises:TypeError
                    if elements of matrix are neither integers nor floats
                    sizes of rows isnt same
                    ZeroDivisionError if dividing argument is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    div = round(div, 2)

    new_matrix = []
    for item in matrix:
        newmatrix = []
        for value in item:
            res = value / div
            newmatrix.append(round(res, 2))
        new_matrix.append(newmatrix)

    return new_matrix
