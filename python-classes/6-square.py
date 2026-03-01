#!/usr/bin/python3
"""
Bu modul koordinat sisteminə malik Square sinfini ehtiva edir.
"""


class Square:
    """
    Kvadrat fiqurunu təmsil edən təkmilləşdirilmiş sinif.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni bir Kvadrat yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın (x, y) koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçü üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçü üçün setter."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinat üçün getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Koordinat üçün setter. 
        Value 2 müsbət tam ədəddən ibarət tuple olmalıdır.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı koordinatlarını nəzərə alaraq çap edir.
        """
        if self.__size == 0:
            print("")
            return

        # Y koordinatı üçün boş sətirlər (Yuxarıdan məsafə)
        [print("") for i in range(self.__position[1])]

        # Kvadratın özünü çap etmək
        for i in range(self.__size):
            # X koordinatı üçün boşluqlar (Soldan məsafə)
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
