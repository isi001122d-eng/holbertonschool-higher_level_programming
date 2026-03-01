#!/usr/bin/python3
"""
Bu modul ekrana kvadrat çap edən Square sinfini ehtiva edir.
"""


class Square:
    """
    Kvadrat fiqurunu təmsil edən sinif.
    """

    def __init__(self, size=0):
        """Yeni bir Kvadrat yaradır."""
        self.size = size

    @property
    def size(self):
        """Ölçünü oxumaq üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təhlükəsiz təyin etmək üçün setter."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı '#' işarəsi ilə standart çıxışa (stdout) çap edir.
        Əgər ölçü 0-dırsa, sadəcə boş bir sətir çap edir.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
