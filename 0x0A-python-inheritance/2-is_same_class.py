#!/usr/bin/python3
"""Module has function that returns true or false"""


def is_same_class(obj, a_class):
    """is the same as class?"""
    if type(obj) is a_class:
        return True
    return False
