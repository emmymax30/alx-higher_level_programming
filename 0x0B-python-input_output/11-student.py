#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns class to a dictionaty"""
        return self.__dict__
