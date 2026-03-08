#!/usr/bin/python3
"""BaseGeometry module task"""


class BaseGeometry:
    """Improved geometry class"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
