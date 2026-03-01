#!/usr/bin/python3
"""
Bu modul kvadratın sahəsini hesablayan Square sinfini ehtiva edir.
"""


class Square:
    """
    Kvadrat fiqurunu təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Kvadrat yaradır.

        Args:
            size (int): Kvadratın tərəfi (default 0).

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size < 0 olarsa.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Kvadratın cari sahəsini hesablayır və qaytarır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2
