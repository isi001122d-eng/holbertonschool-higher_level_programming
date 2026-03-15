#!/usr/bin/python3
"""
Obyekti JSON string-ə çevirən modul
"""
import json


def to_json_string(my_obj):
    """
    Obyektin JSON təmsilini qaytarır
    """
    return json.dumps(my_obj)
