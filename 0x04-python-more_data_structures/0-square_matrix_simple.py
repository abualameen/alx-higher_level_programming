#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dim_row = len(matrix)
    dim_col = len(matrix[0])
    matrix1 = []
    for a in range(dim_row):
        row = []
        for b in range(dim_col):
            row.append(matrix[a][b])
        matrix1.append(row)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix1[x][y] = matrix[x][y]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j] = matrix1[i][j] * matrix1[i][j]
    return matrix1
