#!/usr/bin/python3
"""Abstract Animal Class module"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class"""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound"""
        pass


class Dog(Animal):
    """Dog subclass inheriting from Animal"""

    def sound(self):
        """Implementation of sound for Dog"""
        return "Bark"


class Cat(Animal):
    """Cat subclass inheriting from Animal"""

    def sound(self):
        """Implementation of sound for Cat"""
        return "Meow"
