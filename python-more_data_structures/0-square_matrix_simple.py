#!/usr/bin/python3
"""Squares a matrix"""


def square_matrix_simple(matrix=[]):
    """Squares a matrix"""
    if not matrix:
        return []

    square_matrix = []
    for rows in range(len(matrix)):
        square_matrix.append([])
        for cols in range(len(matrix[rows])):
            square_matrix[rows].append(matrix[rows][cols] ** 2)
    return square_matrix
