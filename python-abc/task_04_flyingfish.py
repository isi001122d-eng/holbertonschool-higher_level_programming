#!/usr/bin/python3
"""
Multiple Inheritance - FlyingFish modulu
"""


class Fish:
    """Fish ana sinfi"""
    def swim(self):
        """Üzmək metodu"""
        print("The fish is swimming")

    def habitat(self):
        """Yaşayış yeri metodu"""
        print("The fish lives in water")


class Bird:
    """Bird ana sinfi"""
    def fly(self):
        """Uçmaq metodu"""
        print("The bird is flying")

    def habitat(self):
        """Yaşayış yeri metodu"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Həm Fish, həm də Bird-dən miras alan sinif"""

    def fly(self):
        """Fly metodunu override edir"""
        print("The flying fish is soaring!")

    def swim(self):
        """Swim metodunu override edir"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat metodunu override edir"""
        print("The flying fish lives both in water and the sky!")
