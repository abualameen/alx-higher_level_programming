#!/usr/bin/python3
"""
this module Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """
    this function creates pascal triangle

    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        past_row = triangle[i - 1]
        for j in range(1, i):
            val = past_row[j - 1] + past_row[j]
            row.append(val)
        row.append(1)
        triangle.append(row)
    return triangle
