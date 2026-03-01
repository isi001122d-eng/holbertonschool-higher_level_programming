#!/usr/bin/python3
"""
Bu modul siyahıdakı integerləri çap edən funksiyanı saxlayır.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Siyahının ilk x elementindən yalnız integer olanları çap edir.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
