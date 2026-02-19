#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = []
    total = 0
    for i in my_list:
        if i not in result:
            result.append(i)
            total += i
    return total
