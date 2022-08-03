#!/usr/bin/python3
""" module that handles pascal traingles """


def pascal_triangle(n):
    """ helper function called by main """

    list_of_lists = []
    triangle = []

    for i in range(n):
        previous = triangle
        if i is not 0:
            triangle = [1]
        for j in range(1, i):
            triangle.append(previous[j - 1] + previous[j])
        triangle.append(1)
        list_of_lists.append(triangle)
    return list_of_lists
