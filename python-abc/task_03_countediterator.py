#!/usr/bin/python3
"""
İterasiya sayını izləyən CountedIterator modulu
"""


class CountedIterator:
    """
    Iteratoru bürüyən (wrapper) və keçidləri sayan sinif
    """

    def __init__(self, iterable):
        """
        Iteratoru və sayğacı inisializasiya edir
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Hazırkı iterasiya sayını qaytarır
        """
        return self.counter

    def __next__(self):
        """
        Növbəti elementi qaytarır və sayğacı artırır
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Iterator obyektinin özünü qaytarır
        """
        return self
