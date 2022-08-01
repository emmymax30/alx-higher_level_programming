#!/usr/bin/python3
""" module that makes the class BaseGeometry """


class BaseGeometry:
    """ I wanna eat. im hungry. """

    def area(self):
        """ raises error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ error checks """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
