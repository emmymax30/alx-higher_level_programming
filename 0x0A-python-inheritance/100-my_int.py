#!/usr/bin/python3
""" inverts not equakl and equals """


class MyInt(int):
    """ swaps the eq and ne """

    def __eq__(self, other):
        """eq means equal"""
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """ne means not equal and night elf"""
        return not self.__eq__(other)
