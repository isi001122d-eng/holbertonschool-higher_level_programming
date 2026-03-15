#!/usr/bin/python3
"""
JSON string-i Python obyektinə çevirən modul
"""
import json


def from_json_string(my_str):
    """
    JSON string-dən Python obyektini qaytarır
    """
    return json.loads(my_str)
