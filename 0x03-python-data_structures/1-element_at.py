#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    i = 0
    for element in my_list:
        if i == idx:
            return element
        i += 1
    return None
