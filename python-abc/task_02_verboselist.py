#!/usr/bin/python3
"""
Siyahı əməliyyatları üçün bildirişlər modulu
"""


class VerboseList(list):
    """
    Siyahı metodlarını override edərək bildirişlər çap edən sinif
    """

    def append(self, item):
        """Element əlavə edir və bildiriş çap edir"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Siyahını genişləndirir və bildiriş çap edir"""
        item_count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item):
        """Elementi silir (əvvəl bildiriş çap edir)"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Elementi çıxarır və bildiriş çap edir"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
