#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for rows in range(len(matrix)):
        square_matrix.append([])
        for cols in range(len(matrix[rows])):
            square_matrix[rows].append(matrix[rows][cols] ** 2)
        return square_matrix
