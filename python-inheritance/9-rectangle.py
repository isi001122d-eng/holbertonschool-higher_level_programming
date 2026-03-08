#!/usr/bin/python3
"""Full rectangle module"""
# 8-rectangle.py-dən miras alırıq, lakin tapşırıq adətən 
# 7-base_geometry-dən import etməyi tələb edir
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Full rectangle class definition"""

    def __init__(self, width, height):
        """Initialize rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
