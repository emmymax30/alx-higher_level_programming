#!/bin/bash/python3
"""
   module to print divide matrix
"""


def matrix_divided(matrix, div):
    """
       matrix_divided- divides all elements of a matrix and returns a new list
       Arguments:
           matrix (list): matrix elements
           div (int): divider
       Raises:
           TypeError: if div is not a float or int
           ZeroDivisionError: if div <= 0
           TypeError: if matrix value is not int or float
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif check_row(matrix):
        raise TypeError("row of the matrix must have the same size")
    elif div <= 0:
        raise ZeroDivisionError("division by zero")
    elif len(matrix) > 0:
        list = []
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        for item in matrix:
            new_list = []
            for value in item:
                if type(value) not in [int, float]:
                    raise TypeError(msg)
                else:
                    x = "{:.2f}".format(value/div)
                    new_list.append(float(x))
            list.append(new_list)
        return list


def check_row(matrix):
    length = len(matrix)
    try:
        for i in range(0, length):
            if (i + 1) != length:
                if len(matrix[i]) != len(matrix[i + 1]):
                    return True
        return False
    except TypeError:
        return True
