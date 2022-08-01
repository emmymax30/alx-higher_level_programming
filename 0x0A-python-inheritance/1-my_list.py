#!/usr/bin/python3
""" Module that contains class of MyLists\
    Inheritd from list"""


class MyList(list):
    """Function that prints a list"""
    def print_sorted(self):
        """Fucntion that prints a sorted list"""
        print(sorted(self))
