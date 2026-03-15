#!/usr/bin/python3
"""
Faylın sonuna mətn əlavə edən modul
"""


def append_write(filename="", text=""):
    """
    Mətni faylın sonuna əlavə edir (UTF-8) və simvolların sayını qaytarır
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
