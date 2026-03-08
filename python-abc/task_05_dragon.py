#!/usr/bin/python3
"""
Mastering Mixins - Dragon modulu
"""


class SwimMixin:
    """Üzmək bacarığı əlavə edən mixin"""
    def swim(self):
        """Üzmək mesajını çap edir"""
        print("The creature swims!")


class FlyMixin:
    """Uçmaq bacarığı əlavə edən mixin"""
    def fly(self):
        """Uçmaq mesajını çap edir"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """SwimMixin və FlyMixin-dən miras alan Dragon sinfi"""
    def roar(self):
        """Dragon-a məxsus özəl nərilti metodu"""
        print("The dragon roars!")
