#!/usr/bin/python3
"""
Mətn faylını oxuyan modulu təmsil edir
"""


def read_file(filename=""):
    """
    UTF-8 formatında olan faylı oxuyur və stdout-a çap edir
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
