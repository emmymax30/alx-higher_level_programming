#!/usr/bin/python3
""" module that adds attribute """


def add_attribute(cls, attr, value):
    """ adds attributes or throws error """

    if hasattr(cls, '__dict__'):
        setattr(cls, attr, value)
    else:
        raise TypeError("can't add new attribute")
