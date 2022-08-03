#!/usr/bin/python3
"""This module reads a file"""


def read_file(filename=""):
    """Opens a file and reads it"""
    with open(filename, mode="r", encoding='utf-8') as the_file:
        print(the_file.read(), end="")
