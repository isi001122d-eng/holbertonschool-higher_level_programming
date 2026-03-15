#!/usr/bin/python3
"""
Student sinfini təmsil edən modul
"""


class Student:
    """
    Tələbə məlumatlarını saxlayan sinif
    """

    def __init__(self, first_name, last_name, age):
        """
        Tələbə obyektini inisializasiya edir
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Tələbənin atributlarını lüğət formatında qaytarır
        """
        return self.__dict__
