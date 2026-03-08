#!/usr/bin/python3
"""Inherits from module"""


def inherits_from(obj, a_class):
    """Check subclass inheritance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
