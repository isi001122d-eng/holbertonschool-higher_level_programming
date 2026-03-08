#!/usr/bin/python3
"""
Şekiller, Arayüzler ve Duck Typing modülü
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    İki soyut metodu olan soyut Shape sınıfı: area ve perimeter
    """
    @abstractmethod
    def area(self):
        """Alanı hesaplayan soyut metod"""
        pass

    @abstractmethod
    def perimeter(self):
        """Çevreyi hesaplayan soyut metod"""
        pass


class Circle(Shape):
    """
    Shape sınıfından türetilen Circle sınıfı
    """
    def __init__(self, radius):
        """Yarıçapı (radius) başlatır"""
        self.radius = radius

    def area(self):
        """Dairenin alanını hesaplar: pi * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Dairenin çevresini hesaplar: 2 * pi * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Shape sınıfından türetilen Rectangle sınıfı
    """
    def __init__(self, width, height):
        """Genişlik ve yüksekliği başlatır"""
        self.width = width
        self.height = height

    def area(self):
        """Dikdörtgenin alanını hesaplar: w * h"""
        return self.width * self.height

    def perimeter(self):
        """Dikdörtgenin çevresini hesaplar: 2 * (w + h)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Duck typing kullanarak nesnenin alan ve çevresini yazdırır.
    Nesnenin tipini kontrol etmeden doğrudan area() ve perimeter() çağırır.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
