#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    total = 0
    for num in uniq:
        total += num
    return total
