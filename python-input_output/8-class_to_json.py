#!/usr/bin/python3
"""
Sinif obyektini lüğətə çevirən modul
"""


def class_to_json(obj):
    """
    Obyektin bütün atributlarını lüğət formatında qaytarır
    """
    return obj.__dict__
