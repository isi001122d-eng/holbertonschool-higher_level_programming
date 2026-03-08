#!/usr/bin/python3
"""Square module task"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """Initialize square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the square representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
