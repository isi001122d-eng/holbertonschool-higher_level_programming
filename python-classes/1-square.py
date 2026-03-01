#!/usr/bin/python3
"""
Kvadratları təyin edən və ölçülərini saxlayan modul.
"""


class Square:
    """
    Square sinfi bir kvadratı təsvir edir.
    """

    def __init__(self, size):
        """
        Yeni bir Kvadrat nümunəsi yaradır.

        Args:
            size (int): Kvadratın tərəfinin uzunluğu.
        """
        self.__size = size
