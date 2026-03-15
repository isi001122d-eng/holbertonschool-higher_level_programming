#!/usr/bin/python3
"""
Basic Serialization modulu
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python l�ini JSON faylına serializasiya edir
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    JSON faylından lumatları oxuyur  Pythoni çevirir
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
