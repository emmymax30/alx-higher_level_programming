#!/usr/bin/python3
""" Module has class BaseGeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """I love arequipe"""

    def __init__(self, width, height):
        """Defining a rectangle and checking values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string with format"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
