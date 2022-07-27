#!/usr/bin/python3
"""
   This module prints the first name and last name
   and raises exceptions if either is not string
"""


def say_my_name(first_name, last_name=""):
    """
      Prints in the format (My name is <first name>
      <last name>)
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
