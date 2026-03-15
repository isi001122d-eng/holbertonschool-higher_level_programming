#!/usr/bin/python3
"""
Custom obyektlərin pickle ilə serializasiyası
"""
import pickle


class CustomObject:
    """Özəl atributları və metodları olan sinif"""

    def __init__(self, name, age, is_student):
        """Obyekti inisializasiya edir"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını tələb olunan formatda çap edir"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Cari obyekti fayla pickle formatında yazır"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Fayldan obyekti oxuyur və CustomObject instansiyası qaytarır"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
