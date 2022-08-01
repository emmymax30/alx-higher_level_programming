#!/usr/bin/python3
""" Module has class BaseGeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """It's raining at Holberton"""

    def __init__(self, width, height):
        """Defining a rectangle and checking values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
