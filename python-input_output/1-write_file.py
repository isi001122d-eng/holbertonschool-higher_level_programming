#!/usr/bin/python3
"""
Fayla yazmaq funksiyasını təmin edən modul
"""


def write_file(filename="", text=""):
    """
    Mətni fayla yazır (UTF-8) və simvolların sayını qaytarır
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
