#!/usr/bin/python3
"""Rectangle module task"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition"""

    def __init__(self, width, height):
        """Initialize rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
