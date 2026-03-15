#!/usr/bin/python3
"""
Basic Serialization modulu - Python lüğətini JSON-a çevirmək və geri qaytarmaq
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini JSON faylına serializasiya edir və yadda saxlayır
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    JSON faylından məlumatları oxuyur və Python lüğətinə deserealizasiya edir
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
