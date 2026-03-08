#!/usr/bin/python3
"""Abstract Animal Class module"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class definition"""

    @abstractmethod
    def speak(self):
        """Abstract method that must be implemented by subclasses"""
        pass

class Dog(Animal):
    """Dog subclass that inherits from Animal"""

    def speak(self):
        """Implementation of speak for Dog"""
        return "Woof!"

class Cat(Animal):
    """Cat subclass that inherits from Animal"""

    def speak(self):
        """Implementation of speak for Cat"""
        return "Meow!"
