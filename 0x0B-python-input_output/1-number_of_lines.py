#!/usr/bin/python3
"""This module return numbers\
    of lines of a text file"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    with open(filename, mode="r", encoding="utf-8") as the_file:
        return sum(1 for line in the_file)
