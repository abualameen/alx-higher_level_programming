#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Returns: a new matrix 
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[0] * len(matrix[0]) for x in range(len(matrix))]
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            output = (matrix[i][j]) / div
            new_mat[i][j] = round(output, 2)
    return new_mat
