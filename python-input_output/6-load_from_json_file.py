#!/usr/bin/python3
"""
JSON faylından Python obyekti yükləyən modul
"""
import json


def load_from_json_file(filename):
    """
    JSON faylını oxuyur və Python obyektini qaytarır
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
