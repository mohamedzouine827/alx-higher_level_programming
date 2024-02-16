#!/bin/usr/python3

def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    result = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(round(element / div, 2))
        result.append(result_row)
    return result
