#!/usr/bin/python3
"""Rectangle module task"""


class Rectangle:
    """Rectangle class definition"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create square instance"""
        return cls(size, size)

    def __str__(self):
        """Print rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Represent rectangle instance"""
        # Burada self.width və self.height (public) istifadə olunmalıdır
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
