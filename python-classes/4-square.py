#!/usr/bin/python3
"""
Bu modul Square sinfinə Getter və Setter əlavə edir.
"""


class Square:
    """
    Kvadrat fiqurunu təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Kvadrat yaradır.
        """
        self.size = size

    @property
    def size(self):
        """
        __size dəyərini oxumaq (get) üçün metod.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        __size dəyərini təhlükəsiz şəkildə dəyişmək (set) üçün metod.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini qaytarır.
        """
        return self.__size ** 2
