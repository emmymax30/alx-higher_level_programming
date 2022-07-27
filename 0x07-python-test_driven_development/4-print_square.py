#!/usr/bin/python3
"""
   This module prints a square(#) with specified size
   and raises exceptions when input is incorrect
"""


def print_square(size):
    """
       Prints the square with "#" character
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            print("#" * size)
