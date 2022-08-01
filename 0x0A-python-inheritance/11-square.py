#!/usr/bin/python3
"""Module has class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Initialize variables"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns area """
        return (super().area())

    def __str__(self):
        """Prints out with format"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
