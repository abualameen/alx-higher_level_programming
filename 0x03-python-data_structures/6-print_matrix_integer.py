#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if j != len(matrix[0])-1:
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][j])
