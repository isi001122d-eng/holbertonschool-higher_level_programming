#!/usr/bin/python3
"""MyList module task"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
