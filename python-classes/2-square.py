#!/usr/bin/python3
"""
Bu modul ölçüsü yoxlanılan Square sinfini ehtiva edir.
"""


class Square:
    """
    Kvadrat fiqurunu təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Kvadrat obyektini yaradır və daxil edilən ölçünü yoxlayır.

        Args:
            size (int, optional): Kvadratın tərəfi. Defolt dəyəri 0-dır.

        Raises:
            TypeError: Əgər size tam ədəd (integer) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
