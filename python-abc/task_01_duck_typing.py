#!/usr/bin/python3
"""
Shapes, Interfaces, and Duck Typing modulu
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class Shape: area və perimeter metodları ilə
    """
    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """
    Circle sinfi - Shape-dən miras alır
    """
    def __init__(self, radius):
        """Radiusu inisializasiya edir"""
        self.radius = radius

    def area(self):
        """Dairənin sahəsi: pi * r^2"""
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Dairənin çevrəsi: 2 * pi * r"""
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle sinfi - Shape-dən miras alır
    """
    def __init__(self, width, height):
        """Width və height-i inisializasiya edir"""
        self.width = width
        self.height = height

    def area(self):
        """Düzbucaqlının sahəsi: w * h"""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının çevrəsi: 2 * (w + h)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Duck typing istifadə edərək sahə və çevrəni çap edir
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
