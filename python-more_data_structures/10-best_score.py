#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_r = float('-inf')
    for key, value in a_dictionary.items():
        if value > best_r:
            best_r = value
            best_key = key
    return best_key
